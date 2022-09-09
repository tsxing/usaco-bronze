import sys

sys.stdin = open("diamond.in","r")
sys.stdout = open("diamond.out","w")

N, K = map(int, input().split())
sizes=[]

for _ in range(N): 
  sizes.append(int(input()))

ans = 0

for i in range(N):
  cnt = 0
  for j in range(N):
    if sizes[j]>=sizes[i] and sizes[j]-sizes[i]<=K: #if difference between 2 sizes in sizes array <= K.
      cnt += 1
  ans=max(ans,cnt)
print(ans)
