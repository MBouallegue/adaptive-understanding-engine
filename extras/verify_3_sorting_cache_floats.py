import time, sys, random, threading, math
random.seed(7)
def T(f, *a):
    s = time.perf_counter(); r = f(*a); return time.perf_counter() - s, r

print("[O] insertion sort vs merge sort (both pure Python), time per sort")
def ins_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        x = a[i]; j = i - 1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]; j -= 1
        a[j+1] = x
    return a
def merge_sort(a):
    if len(a) <= 1: return a
    m = len(a) // 2; l = merge_sort(a[:m]); r = merge_sort(a[m:])
    out = []; i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]: out.append(l[i]); i += 1
        else: out.append(r[j]); j += 1
    out += l[i:]; out += r[j:]; return out
for n in (4, 8, 16, 32, 64, 128, 512, 2048):
    reps = max(3, 20000 // n)
    arrs = [[random.random() for _ in range(n)] for _ in range(reps)]
    ti = T(lambda: [ins_sort(a) for a in arrs])[0] / reps
    tm = T(lambda: [merge_sort(a) for a in arrs])[0] / reps
    print(f"  n={n:5d}: insertion {ti*1e6:9.1f} us   merge {tm*1e6:9.1f} us   -> {'insertion' if ti < tm else 'merge'} faster")

print("\n[P] built-in sort: comparisons on sorted vs shuffled input (n=100,000)")
class C:
    n = 0
    __slots__ = ("v",)
    def __init__(self, v): self.v = v
    def __lt__(self, o): C.n += 1; return self.v < o.v
for label, vals in (("already sorted", list(range(100_000))), ("shuffled", random.sample(range(100_000), 100_000))):
    C.n = 0; sorted(C(v) for v in vals); print(f"  {label}: {C.n:,} comparisons")
print(f"  (n*log2(n) = {100_000*math.log2(100_000):,.0f})")

print("\n[T] dict lookup time vs dict size (random existing int keys)")
for size in (1_000, 100_000, 3_000_000):
    d = {i: i for i in range(size)}
    keys = [random.randrange(size) for _ in range(1_000_000)]
    t, _ = T(lambda: [d[k] for k in keys])
    tb, _ = T(lambda: [k for k in keys])
    print(f"  size={size:>9,}: {(t - tb) / 1e6 * 1e9:6.1f} ns per lookup")
    del d

print("\n[Q] floats")
print("  0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3, "| 0.1 + 0.2 =", repr(0.1 + 0.2))
print("  sum([0.1]*10) == 1.0 ->", sum([0.1]*10) == 1.0, "| math.fsum ->", math.fsum([0.1]*10) == 1.0)

print("\n[M2] race with an explicit yield between read and write, 4 threads x 20,000 (expected 80,000)")
def run():
    g = {"c": 0}
    def w():
        for _ in range(20_000):
            tmp = g["c"]; time.sleep(0); g["c"] = tmp + 1
    ts = [threading.Thread(target=w) for _ in range(4)]
    [t.start() for t in ts]; [t.join() for t in ts]
    return g["c"]
print("  results over 5 runs:", [run() for _ in range(5)])
def run_lock():
    g = {"c": 0}; lock = threading.Lock()
    def w():
        for _ in range(20_000):
            with lock:
                tmp = g["c"]; time.sleep(0); g["c"] = tmp + 1
    ts = [threading.Thread(target=w) for _ in range(4)]
    [t.start() for t in ts]; [t.join() for t in ts]
    return g["c"]
print("  with a lock around read-yield-write:", run_lock())

print("\n[S] stable sort, two passes")
people = [("dana", "ops"), ("amir", "eng"), ("chen", "ops"), ("bela", "eng")]
by_name = sorted(people, key=lambda p: p[0]); print("  by name, then by team:", sorted(by_name, key=lambda p: p[1]))

print("\n[U] aliasing and mutable default")
a = [1, 2]; b = a; b.append(3); print("  b = a; b.append(3); a ->", a)
def add(x, acc=[]):
    acc.append(x); return acc
print("  add(1), add(2) with default acc=[] ->", add(1), add(2))
