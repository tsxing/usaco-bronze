import sys
sys.stdin = open("lifeguards.in","r")
sys.stdout = open("lifeguards.out","w")

N = int(input())
log = []

for _ in range(N):
  start,end = map(int, input().split())
  log.append([start,end])

time = 0 #time covered
maxTime = 0 #ans
for i in range(N):
  time = 0 #reset time covered to 0
  for t in range(1,1001):
    for j in range(N):
      if i!=j: #fire a lifeguard
        if log[j][0]<=t<log[j][1]: #the lifeguard's shift
          time += 1
          break

  maxTime = max(maxTime, time)
print(maxTime)
    



