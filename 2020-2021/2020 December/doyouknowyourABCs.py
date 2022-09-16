ints = [int(x) for x in input().split()]

ints.sort()
a,b = ints[0],ints[1]
c = ints[-1]-a-b
print(a,b,c)
