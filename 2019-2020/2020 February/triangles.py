import sys
sys.stdin=open("triangles.in","r")
sys.stdout = open("triangles.out","w")
N = int(input())
pts = []
ans = 0
for _ in range(N):
  x,y = map(int, input().split())
  pts.append([x,y])

for p1 in range(N):
  for p2 in range(N):
    for p3 in range(N):
      if pts[p1][0]==pts[p2][0] and pts[p2][1]==pts[p3][1]:
        area = abs(pts[p1][1]-pts[p2][1])*abs(pts[p2][0]-pts[p3][0])
        ans = max(ans, area)

print(ans)
    
