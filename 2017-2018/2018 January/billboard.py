import sys
sys.stdin = open("billboard.in","r")
sys.stdout = open("billboard.out","w")

x1,y1,x2,y2 = map(int, input().split())
x3,y3,x4,y4 = map(int, input().split())

x = [0,x1,x2,x3,x4]
y = [0,y1,y2,y3,y4]


if x[3]<=x[1] and x[2]<=x[4] and y[3]<=y[1] and y[4]>=y[2]:
  print(0)
elif x[3]<=x[1] and x[2]<=x[4] and y[3]<=y[1] and y[2]>y[4]:
  print((x[2]-x[1])*(y[2]-y[4]))
elif x[3]<=x[1] and x[2]<=x[4] and y[1]<y[3] and y[4]>=y[2]:
  print((x[2]-x[1])*(y[3]-y[1]))
elif y[3]<=y[1] and y[2]<=y[4] and x[1]<x[3] and x[2]<=x[4]:
  print((y[2]-y[1])*(x[3]-x[1]))
elif y[3]<=y[1] and y[2]<=y[4] and x[3]<=x[1] and x[2]>x[4]:
  print((y[2]-y[1])*(x[2]-x[4]))
else:
  print((x[2]-x[1])*(y[2]-y[1]))
