
N = int(input())
petals = [int(x) for x in input().split()]
cnt = 0

for i in range(N):
  for j in range(i,N):
    avg=sum(petals[i:j+1])/(j-i+1)
    for f in range(i,j+1):
      if petals[f]==avg:
        cnt += 1
        break 
print(cnt)
