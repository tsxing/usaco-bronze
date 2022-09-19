import sys
sys.stdin = open("blocks.in","r")
sys.stdout = open("blocks.out","w")

N = int(input())

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a1 = [0]*26
a2 = [0]*26
ans = [0]*26

for _ in range(N):
  w1,w2 = map(str,input().split())
  for i in w1:
    a1[a.index(i)]+=1
  for i in w2:
    a2[a.index(i)]+=1
    
  for i in range(26):
    ans[i]+= max(a1[i],a2[i])

  a1,a2 = [0]*26,[0]*26

for i in ans:
  print(i)
