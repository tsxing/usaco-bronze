import sys
sys.stdin = open("shell.in","r")
sys.stdout = open("shell.out","w")

N = int(input())
ans = 0
shellsLoc = [0,1,2] #shell location
cnt = [0,0,0] #if it starts at cnt[0],cnt[1], or cnt[2]

for _ in range(N):
  a,b,g = map(int, input().split()) #swapped shells, guessed shell
  shellsLoc[a-1],shellsLoc[b-1] = shellsLoc[b-1],shellsLoc[a-1] #swap
  cnt[shellsLoc[g-1]]+=1 #num of times Elsie guesses the shell
print(max(cnt)) #max num of points
  
  