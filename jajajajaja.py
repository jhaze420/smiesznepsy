from random import Random

a = []
r = Random()
for i in range(100):
        a.append(r.randint(0,1001))
print(a)
print(len(a))

print(a[::2])
print(len(a[::2]))
