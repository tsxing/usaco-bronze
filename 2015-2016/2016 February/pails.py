import sys
sys.stdin = open("pails.in","r")
sys.stdout = open("pails.out","w")

X,Y,M = map(int, input().split()) #read inputs

maxMilk = 0 #define answer
third = 0 #milk in third pail

for i in range(1001): #M is at most 1000
  if i*X>M: #if milk pouring from X > M
    break
  for j in range(1001):
    third = i*X +j*Y #amt of milk third pail has
    if third>M: #if third pail has more milk than M can hold
      break
    maxMilk = max(third, maxMilk) 
    
print(maxMilk)


  
