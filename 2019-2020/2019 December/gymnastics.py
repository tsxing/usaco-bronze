import sys
sys.stdin=open("gymnastics.in","r")
sys.stdout = open("gymnastics.out","w")

K, N = map(int, input().split())
better = [ [0]*20 for i in range(20)]
rankings=[[0]*10 for i in range(20)]
cows = []
ans = 0

for i in range(K):
  line = [int(x) for x in input().split()]
  rankings[i] = [x-1 for x in line]
  
for i in range(K): #row
  for j in range(N): #column
    for x in range(j+1,N): # "the next cow being compared"
      better[rankings[i][j]][rankings[i][x]]+=1

for i in range(N):
  for j in range(N):
    if better[i][j]==K:
      ans+=1
print(ans)
    
    
