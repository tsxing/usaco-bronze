import sys
sys.stdin = open("cownomics.in","r")
sys.stdout = open("cownomics.out","w")

N,M = map(int, input().split())
tableSpotty = []
tablePlain = []
letters = ["A","C","G","T"]

for _ in range(N):
  str = input()
  tableSpotty.append(str)
for _ in range(N):
  str = input()
  tablePlain.append(str)

ans = 0

for i in range(M): #for each position
  used = False #we didn't use same letters (ACGT)
  for j in range(N): #iterate through spotty and plain cows
    for k in range(N):
      if tableSpotty[j][i]==tablePlain[k][i]: #if letter of the same "column" is equal from spotty and plain cows
        used = True #there's used letters
        break
  if used==False: #if there's no used letters after iterating
    ans += 1

print(ans)

  
  



  
  
  





