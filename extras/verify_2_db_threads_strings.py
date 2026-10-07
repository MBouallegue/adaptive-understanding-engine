import time, sys, random, sqlite3, threading
random.seed(7)
def T(f, *a):
    s = time.perf_counter(); r = f(*a); return time.perf_counter() - s, r

print("[K] sqlite index (sqlite", sqlite3.sqlite_version, ")")
def build(n_idx):
    c = sqlite3.connect(":memory:")
    c.execute("create table orders(id integer primary key, customer_id int, status text, amount int, city int, sku int)")
    for i in range(n_idx):
        col = ["customer_id", "status", "amount", "city", "sku"][i]
        c.execute(f"create index ix_{col} on orders({col})")
    rows = [(random.randrange(20000), random.choice("abcd"), random.randrange(1000), random.randrange(500), random.randrange(5000)) for _ in range(200_000)]
    t, _ = T(lambda: (c.executemany("insert into orders(customer_id,status,amount,city,sku) values (?,?,?,?,?)", rows), c.commit()))
    return c, t
c0, t0 = build(0); c5, t5 = build(5)
print(f"  insert 200,000 rows: no indexes {t0:.2f}s, five indexes {t5:.2f}s")
q = "select count(*), sum(amount) from orders where customer_id = ?"
print("  plan without index:", c0.execute("explain query plan " + q, (5,)).fetchall()[0][3])
print("  plan with index   :", c5.execute("explain query plan " + q, (5,)).fetchall()[0][3])
ids = [random.randrange(20000) for _ in range(200)]
print(f"  200 lookups: no index {T(lambda: [c0.execute(q,(i,)).fetchone() for i in ids])[0]:.3f}s, index {T(lambda: [c5.execute(q,(i,)).fetchone() for i in ids])[0]:.4f}s")
c0.execute("create index ix_cs on orders(customer_id, status)")
for label, sql in (("customer_id = ?", "select * from orders where customer_id = 5"),
                   ("customer_id = ? and status = ?", "select * from orders where customer_id = 5 and status = 'a'"),
                   ("status = ?  (second column only)", "select * from orders where status = 'a'")):
    print(f"  composite (customer_id,status), where {label}: ", c0.execute("explain query plan " + sql).fetchall()[0][3])
c0.execute("analyze")
print("  ...same second-column query after ANALYZE:", c0.execute("explain query plan select * from orders where status = 'a'").fetchall()[0][3])
print("  function on column, where abs(customer_id) = 5:", c5.execute("explain query plan select * from orders where abs(customer_id) = 5").fetchall()[0][3])

print("\n[R] N+1 queries, counted with a trace callback")
c = sqlite3.connect(":memory:")
c.execute("create table author(id integer primary key, name text)"); c.execute("create table book(id integer primary key, author_id int, title text)")
c.executemany("insert into author(name) values (?)", [(f"a{i}",) for i in range(100)])
c.executemany("insert into book(author_id,title) values (?,?)", [(random.randrange(1,101), f"b{i}") for i in range(1000)])
n = [0]; c.set_trace_callback(lambda s: n.__setitem__(0, n[0] + 1))
for (aid, name) in c.execute("select id, name from author").fetchall():
    c.execute("select title from book where author_id = ?", (aid,)).fetchall()
print("  loop version: statements executed =", n[0])
n[0] = 0; c.execute("select a.name, b.title from author a join book b on b.author_id = a.id").fetchall()
print("  join version: statements executed =", n[0])

print("\n[M] race on a shared counter, 4 threads x 200,000 increments (expected 800,000)")
import time as _t
def run(body):
    g = {"counter": 0}
    def w():
        for _ in range(200_000): body(g)
    ts = [threading.Thread(target=w) for _ in range(4)]
    [t.start() for t in ts]; [t.join() for t in ts]
    return g["counter"]
def inc(g): g["counter"] += 1
def split(g):
    tmp = g["counter"]; g["counter"] = tmp + 1
def noop(): pass
def split_call(g):
    tmp = g["counter"]; noop(); g["counter"] = tmp + 1
for name, b in (("counter += 1", inc), ("tmp = counter; counter = tmp + 1", split), ("read; call a function; write", split_call)):
    res = [run(b) for _ in range(3)]
    print(f"  {name}: results over 3 runs = {res}")
# the inline form inside the loop body (no helper call per iteration)
counter = 0
def w_inline():
    global counter
    for _ in range(200_000): counter += 1
for _ in range(3):
    counter = 0; ts = [threading.Thread(target=w_inline) for _ in range(4)]; [t.start() for t in ts]; [t.join() for t in ts]
    print("  inline 'global counter; counter += 1' in a for loop:", counter)
print("  switch interval:", sys.getswitchinterval())

print("\n[N] string += in a loop")
def local_concat(n):
    s = ""
    for _ in range(n): s += "x"
    return len(s)
class Box: pass
def attr_concat(n):
    b = Box(); b.s = ""
    for _ in range(n): b.s += "x"
    return len(b.s)
def join_concat(n): return len("".join("x" for _ in range(n)))
for n in (20_000, 200_000):
    print(f"  n={n}: local variable {T(local_concat,n)[0]:.4f}s | object attribute {T(attr_concat,n)[0]:.4f}s | join {T(join_concat,n)[0]:.4f}s")
print(f"  n=2,000,000 local variable: {T(local_concat,2_000_000)[0]:.3f}s")
