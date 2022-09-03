import sys

sys.stdin = open("speeding.in","r")
sys.stdout = open("speeding.out","w")


N,M = map(int, input().split())

road = [0]*100
bes = [0] *100

roadInfo = []
bessieInfo = []

for _ in range(N):
  length,speedLimit = map(int, input().split())
  roadInfo.append([length,speedLimit])
  
for _ in range(M):
  bessieLength,bessieSpeed = map(int, input().split())
  bessieInfo.append([bessieLength,bessieSpeed])
  
segment = 0
for i in range(N):
  for j in range(roadInfo[i][0]):
    road[segment] = roadInfo[i][1]
    segment += 1
    
segment = 0
for i in range(M):
  for j in range(bessieInfo[i][0]):
    bes[segment] = bessieInfo[i][1]
    segment += 1


ans = 0
diff = 0 #difference in speed
for i in range(100):
  if road[i]<bes[i]:
    diff = bes[i]-road[i]
  ans = max(diff,ans)
print(ans)
    