import time, sys, random, bisect, heapq
random.seed(7)
def T(f, *a):
    s = time.perf_counter(); r = f(*a); return time.perf_counter() - s, r
print("python", sys.version.split()[0])

print("\n[B] constant-hash keys in a dict")
class K:
    eq_calls = 0
    def __init__(self, v): self.v = v
    def __hash__(self): return 1
    def __eq__(self, o): K.eq_calls += 1; return self.v == o.v
for n in (500, 5000):
    K.eq_calls = 0
    t, _ = T(lambda: {K(i): i for i in range(n)})
    print(f"  n={n}: __eq__ calls={K.eq_calls:,}  time={t:.3f}s")
t, _ = T(lambda: {i: i for i in range(5000)}); print(f"  normal int keys n=5000: time={t:.5f}s")

print("\n[C] list.append vs list.insert(0, x)")
def app(n):
    a = []
    for i in range(n): a.append(i)
def ins(n):
    a = []
    for i in range(n): a.insert(0, i)
for n in (5000, 50000):
    print(f"  n={n}: append={T(app,n)[0]:.4f}s  insert(0)={T(ins,n)[0]:.4f}s")
a = []; last = sys.getsizeof(a); steps = []
for i in range(70):
    a.append(i); s = sys.getsizeof(a)
    if s != last: steps.append(len(a)); last = s
print("  list reallocates when len reaches:", steps)

print("\n[D] fib call counts")
calls = 0
def fib(n):
    global calls; calls += 1
    return n if n < 2 else fib(n-1) + fib(n-2)
t, r = T(fib, 30); print(f"  naive fib(30)={r}: calls={calls:,} time={t:.2f}s")
calls = 0; memo = {}
def fibm(n):
    global calls; calls += 1
    if n in memo: return memo[n]
    memo[n] = n if n < 2 else fibm(n-1) + fibm(n-2); return memo[n]
t, r = T(fibm, 30); print(f"  memo  fib(30)={r}: calls={calls:,} time={t:.6f}s")

print("\n[E] binary search on unsorted data")
data = [5, 1, 4, 2, 3]
for x in (4, 1, 5):
    i = bisect.bisect_left(data, x)
    print(f"  search {x} in {data}: index={i}, found={i < len(data) and data[i] == x}, actually present={x in data}")

print("\n[F] BFS vs weighted shortest path")
G = {'A': {'D': 10, 'B': 1}, 'B': {'C': 1}, 'C': {'D': 1}, 'D': {}}
from collections import deque
def bfs(G, s, t):
    prev = {s: None}; q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for v in G[u]:
            if v not in prev: prev[v] = u; q.append(v)
    p = []; u = t
    while u: p.append(u); u = prev[u]
    p.reverse(); return p, sum(G[a][b] for a, b in zip(p, p[1:]))
def dij_lazy(G, s):
    dist = {s: 0}; pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float('inf')): continue
        for v, w in G[u].items():
            if d + w < dist.get(v, float('inf')):
                dist[v] = d + w; heapq.heappush(pq, (d + w, v))
    return dist
def dij_visited(G, s):
    dist = {s: 0}; pq = [(0, s)]; done = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in done: continue
        done.add(u)
        for v, w in G[u].items():
            if v in done: continue
            if d + w < dist.get(v, float('inf')):
                dist[v] = d + w; heapq.heappush(pq, (d + w, v))
    return dist
print("  BFS path A->D:", bfs(G, 'A', 'D'), " Dijkstra dist:", dij_lazy(G, 'A')['D'])

print("\n[G] Dijkstra with a negative edge")
N = {'A': {'B': 2, 'C': 3}, 'B': {'D': 1}, 'C': {'B': -2}, 'D': {}}
print("  true shortest A->D = A,C,B,D = 3-2+1 = 2")
print("  'finalize on pop' (visited set):", dij_visited(N, 'A'))
print("  lazy-deletion variant (no visited set):", dij_lazy(N, 'A'))

print("\n[H] quicksort, first element as pivot")
cmp = 0
def qs(a):
    global cmp
    if len(a) <= 1: return a
    p, rest = a[0], a[1:]; cmp += len(rest)
    return qs([x for x in rest if x < p]) + [p] + qs([x for x in rest if x >= p])
for label, arr in (("random", random.sample(range(10**6), 500)), ("already sorted", list(range(500)))):
    cmp = 0; qs(arr); print(f"  n=500 {label}: pivot comparisons={cmp:,}")
try:
    qs(list(range(2000))); print("  n=2000 sorted: ok")
except RecursionError as e:
    print("  n=2000 already sorted: RecursionError (default limit", sys.getrecursionlimit(), ")")

print("\n[I] naive BST height")
def height_after(keys):
    root = None; h = 0
    for k in keys:
        if root is None: root = [k, None, None]; h = 1; continue
        n = root; d = 1
        while True:
            i = 1 if k < n[0] else 2; d += 1
            if n[i] is None: n[i] = [k, None, None]; break
            n = n[i]
        h = max(h, d)
    return h
ks = list(range(1000)); sh = ks[:]; random.shuffle(sh)
print(f"  1000 keys inserted in sorted order: height={height_after(ks)}; shuffled: height={height_after(sh)}")

print("\n[J] doubling dynamic array: copies")
cap, size, total, worst = 1, 0, 0, 0
for i in range(1_000_000):
    if size == cap:
        total += size; worst = max(worst, size); cap *= 2
    size += 1
print(f"  1,000,000 appends: total element copies={total:,} ({total/1e6:.2f} per append), worst single append copied {worst:,}")
