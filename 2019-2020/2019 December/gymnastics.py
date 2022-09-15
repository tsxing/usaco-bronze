import sys
sys.stdin = open("gymnastics.in","r")
sys.stdout = open("gymnastics.out","w")

K,N = map(int, input().split())
sessions = []

ans = 0
tot = 0
for _ in range(K):
  line = [int(x) for x in input().split()]
  sessions.append(line)

for i in range(N):
  for j in range(N):
    if i==j: #if the ones we're comparing is the same
      continue
    for s in sessions:
      if s.index(i+1)<s.index(j+1): #+1 because we use 0 indexing
        break
    else:
      ans += 1

print(ans)

#this solution compares elements' indexes with 3 nested for loops
    
    
