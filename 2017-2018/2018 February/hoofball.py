import sys
sys.stdin= open("hoofball.in","r")
sys.stdout = open("hoofball.out","w")

N = int(input())
x = [int(x) for x in input().split()]
passes = [0]*N #list of number of passes each cow gets

ans = 0

x.sort() #sort positions

def target(i): #who does cow i pass ball to?
  if i!= 0 and i!=N-1:
    if x[i]-x[i-1]==x[i+1]-x[i]: #if equal, pass to left
      return x.index(x[i-1])
    else:
      if x[i]-x[i-1]<x[i+1]-x[i]:
        return x.index(x[i-1])
      else:
        return x.index(x[i+1])
  else:
    if i==0:
      return x.index(x[i+1])
    if i==N-1:
      return x.index(x[i-1])
  
for i in range(N):
  passes[target(i)] +=1 

for i in range(N):
  if passes[i] == 0:
    ans += 1
  if i<target(i) and target(target(i))==i and passes[i] == 1 and passes[target(i)] ==1:
    ans += 1
print(ans)
