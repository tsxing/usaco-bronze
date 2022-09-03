import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a,b = map(int, input().split())
c,d = map(int, input().split())


def findOverlap(a1,a2,b1,b2): #find overlap
  return max(0, min(a2, b2) - max(a1, b1))
  
if findOverlap(a,b,c,d)==0:
  print(b-a+d-c)
else:
  print(b-a+d-c - findOverlap(a,b,c,d))