import sys
sys.stdin = open("blocks.in","r")
sys.stdout = open("blocks.out","w")

N = int(input())
w1s, w2s, final = [0] * 26, [0] * 26, [0] * 26 #initialize

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for _ in range(N):
  w1,w2 = map(str,input().split())
  
  for i in w1:
    for l in range(26):
      if alphabet[l] == i:
        w1s[l]+=1
    
  for i in w2:
    for l in range(26):
      if alphabet[l] == i:
        w2s[l]+=1
        
  for i in range(26):
    final[i] += max(w1s[i],w2s[i]) #update final

  w1s, w2s = [0] * 26, [0] * 26  #reset counts for individual blocks
    
    
for i in range(26):
  print(final[i])
