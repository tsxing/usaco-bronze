import sys
sys.stdin = open("breedflip.in","r")
sys.stdout = open("breedflip.out","w")

N = int(input())
A = str(input())
B = str(input())

log= [False]+[x != y for x,y in zip(A,B)] #if different, True (cows are mismatched). 

ans = 0
#now count the amount of [False,True] there are in log.
  
for x,y in zip(log,log[1:]): #compares log to (log starting from 2nd element/removes 1st element)
  if x==False and y == True:
    ans += 1
print(ans)
