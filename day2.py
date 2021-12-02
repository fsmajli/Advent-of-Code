f = open("/home/fati/Desktop/input2", "r")

list = []
hor = 0
dep = 0
aim = 0
for x in f:
  if 'up' in x:
    #dep = dep - int(x[-2])
    aim = aim - int(x[-2])

  if 'down' in x:
    #dep = dep + int(x[-2])
    aim = aim + int(x[-2])

  if 'forward' in x:
    hor = hor + int(x[-2])
    dep = dep + aim * int(x[-2])


print(dep*hor)
print(hor)
