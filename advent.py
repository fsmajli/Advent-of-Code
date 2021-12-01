import numpy as np
f = open("/home/fati/Desktop/input", "r")
y = 1000
d = 0
list = []
for x in f:

  list.append(int(x))
  if int(x) > y:
    d = d+1

  y = int(x)

sum1 = 100000
k = 0
for i in range(len(list)-2):

  sum2 = np.sum(list[i:i+3])

  if sum2 > sum1:
    k = k+1

  sum1 = sum2

print(d) # solution part 1
print(k) # solution part 2

