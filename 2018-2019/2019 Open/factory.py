import sys
sys.stdin = open("factory.in","r")
sys.stdout = open("factory.out","w")

N= int(input())
incoming = [0]*101 #incoming cows
outgoing = [0]*101 #outgoing 
for _ in range(N-1):
  a,b = map(int, input().split()) #travels only a --> b
  outgoing[a]+=1
  incoming[b]+=1

ans = -1 
for i in range(1,N+1):
  if outgoing[i]==0 and ans!= -1:
    ans = -1
    break
  if outgoing[i]==0:
    ans = i

print(ans)
