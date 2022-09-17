import sys
sys.stdin = open("paint.in","r")
sys.stdout = open("paint.out","w")

a,b = map(int, input().split())
c,d = map(int, input().split())

def findIntersection(a,b,c,d):
  return max(min(b,d)-max(a,c),0) #to find length of overlap of 2 lines, do this

print(b-a+d-c-findIntersection(a,b,c,d))
