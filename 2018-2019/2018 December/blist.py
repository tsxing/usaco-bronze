import sys
sys.stdin = open("blist.in","r")
sys.stdout = open("blist.out","w")

N = int(input())

log = []
for _ in range(N):
  si,ti,bi = map(int, input().split())
  log.append([si,ti,bi])

maxBuckets = 0

for i in range(1,1001): #for each time 
  curBuckets = 0
  for j in range(N):
    if log[j][0]<=i<=log[j][1]: #if the time is between start and end times of a cow, increment curBuckets by the amt of buckets required 
      curBuckets += log[j][2]
  maxBuckets = max(maxBuckets, curBuckets) #find max bucket amts
print(maxBuckets)
      