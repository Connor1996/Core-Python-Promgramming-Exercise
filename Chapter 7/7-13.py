import random

Aset = set()
Bset = set()

temp = random.randint(1, 10)
for i in range(temp):
    Aset.add(random.randint(0, 9))
temp = random.randint(1, 10)
for i in range(temp):
    Bset.add(random.randint(0, 9))

print Aset | Bset
print Aset & Bset
