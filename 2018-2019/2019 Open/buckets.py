import sys
sys.stdin = open("buckets.in","r")
sys.stdout = open("buckets.out","w")


layout = []
for _ in range(10):
  line = str(input())
  line = list(line)
  layout.append(line)

for i in range(10):
  for j in range(10):
    if layout[i][j]=="B":
      bX, bY = j,i
    if layout[i][j]=="R":
      rX,rY = j,i
    if layout[i][j]=="L":
      lX,lY = j,i
distance = abs(bX-lX)+abs(bY-lY) #total including/not considering endpoints and rock

if (bX==lX or bY==lY) and (abs(rX-bX)+abs(rX-lX)+abs(rY-bY)+abs(rY-lY)==distance):
  print(distance+1)
else:
  print(distance-1)


if bX==lX==rX and (bX<rX<lX or lX<bX<rX): #if lined horizontally and rock is between barn and lake
  print(distance+2)
elif bY==lY==rY and (bY<rY<lY or lY<rY<bY): #if lined vertically and rock between barn and lake
  print(distance+2)
  
    
