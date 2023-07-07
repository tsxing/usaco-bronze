import sys
sys.stdin = open("sleepy.in","r")
sys.stdout = open("sleepy.out","w")

N = int(input())
p = [int(x) for x in input().split()]
ans = 0

def solve(N,a):
  a=a[::-1]
  cnt = 1
  for i in range(1,N):
    if a[i]<a[i-1]:
      cnt+=1
    else:
      break
      
  return cnt

print(N-solve(N,p))


      

  
