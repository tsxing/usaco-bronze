import sys
sys.stdin = open("crossroad.in","r")
sys.stdout = open("crossroad.out","w")

N = int(input())
#cows = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0]]

log = []
for _ in range(N):
  id,pos = map(int, input().split()) #read inputs
  log.append([id,pos])

cnt = 0
log.sort(key=lambda x: x[0]) #sort based on cow ID

for x, y in zip(log, log[1:]):
  if x[0] == y[0]: #print out x and y to see what they are
    if x[1] != y[1]:
      cnt += 1 #increment cross road times by 1
  

print(cnt)
