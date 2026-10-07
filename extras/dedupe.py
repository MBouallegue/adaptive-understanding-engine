import random, time, sys

def dedupe(ids):
    seen = []
    for x in ids:
        if x not in seen:
            seen.append(x)
    return seen

def dedupe_set(ids):
    seen = set(); out = []
    for x in ids:
        if x not in seen:
            seen.add(x); out.append(x)
    return out

def t(fn, data, reps=1):
    best = float('inf')
    for _ in range(reps):
        s = time.perf_counter(); fn(data); best = min(best, time.perf_counter() - s)
    return best

print(sys.version)
random.seed(1)
print("--- list version, all-unique ids")
for n in (5_000, 50_000):
    data = random.sample(range(10**9), n)
    print(n, round(t(dedupe, data, reps=3 if n <= 5000 else 1), 4), "s")

print("--- list version, 50,000 items, few distinct values")
for d in (10, 100, 1000):
    data = [random.randrange(d) for _ in range(50_000)]
    print("distinct=", d, round(t(dedupe, data, reps=3), 4), "s")

print("--- set version, all-unique ids")
for n in (5_000, 50_000, 5_000_000):
    data = random.sample(range(10**9), n)
    print(n, round(t(dedupe_set, data, reps=3 if n <= 50_000 else 1), 5), "s")
