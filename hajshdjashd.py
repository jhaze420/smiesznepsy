from random import Random
import statistics

a = []
r = Random()
for i in range(100):
        a.append(r.randint(0,101))
print("max", max(a))
print("min", min(a))
print("średnia", statistics.mean(a))