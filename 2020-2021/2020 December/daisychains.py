N = int(input())
p = [int(x) for x in input().split()]
photos = 0
for i in range(N):
  for j in range(i,N):
    totPedals =0
    for k in range(i,j+1):
      totPedals += p[k]
    for k in range(i,j+1):
      if p[k]*(j-i+1) == totPedals:
        photos +=1
        break

print(photos)
