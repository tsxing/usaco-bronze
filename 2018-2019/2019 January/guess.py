#this passes all but the 10th test case! (TLE)

import sys
sys.stdin = open("guess.in","r")
sys.stdout = open("guess.out","w")

N = int(input())
log = []*N

#function to find num of things in common of 2 animals
def findCommon(x,y):

  cnt = 0
  size1,size2 = len(log[x]),len(log[y])
  for i in range(size1):
    for j in range(size2):
      if log[x][i] == log[y][j]:
        cnt += 1
  return cnt
  
for _ in range(N):
  line = [str(x) for x in input().split()]
  log.append(line[2::])

ans = 0
for i in range(N):
  for j in range(i+1,N):
    ans = max(ans,findCommon(i,j))
print(ans+1)

