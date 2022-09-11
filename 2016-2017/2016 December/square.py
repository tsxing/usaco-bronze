import sys
sys.stdin = open("square.in","r")
sys.stdout = open("square.out","w")

x1,y1,x2,y2 = map(int, input().split()) #1st rec
a1,b1,a2,b2 = map(int, input().split()) #2nd rec

horDis = max(x1,x2,a1,a2) - min(x1,x2,a1,a2)
verDis = max(y1,y2,b1,b2) - min(y1,y2,b1,b2)

print(max(horDis,verDis)**2)
