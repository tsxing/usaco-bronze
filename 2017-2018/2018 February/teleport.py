import sys
sys.stdin = open("teleport.in","r")
sys.stdout = open("teleport.out","w")

a,b,x,y = map(int, input().split())
print(min(abs(a-x)+abs(b-y),abs(a-y)+abs(b-x),abs(b-a))) #consider all cases, and print out minimum number
