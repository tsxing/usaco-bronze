import sys
sys.stdin = open("square.in","r")
sys.stdout = open("square.out","w")

x1,y1,x2,y2 = map(int, input().split())
r2x1,r2y1,r2x2,r2y2 = map(int, input().split())

if abs(max(r2y2,y2)-min(r2y1,y1))>abs(max(r2x2,x2)-min(r2x1,x1)):
  print(abs(max(r2y2,y2)-min(r2y1,y1))**2)
else:
  print(abs(max(r2x2,x2)-min(r2x1,x1))**2)
