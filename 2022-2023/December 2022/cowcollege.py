N = int(input())
c = [int(x) for x in input().split()]
c.sort(reverse=True)

best = 0
bestPrice = 0
for i in range(N):
  money = (i+1)*c[i]
  if money >= best:
    best = money
    bestPrice = c[i]

print(best,bestPrice)
