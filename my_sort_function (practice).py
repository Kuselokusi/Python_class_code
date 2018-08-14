import random
from array import *

x = []

for i in range(1, 20):
    x.append(random.randint(0, 30))

print(x[1])
Oldx = x
Oldx.sort()  # to sort the old x array to compare to new sort in loop to follow
print(Oldx)

for i in range(0, len(x) - 1):
    if (x[i] > x[i + 1]):
        holder = x[i + 1]
        x[i + 1] = x[i]
        x[i] = holder

print(x)  # to show if sorting algorithm from loop works works
