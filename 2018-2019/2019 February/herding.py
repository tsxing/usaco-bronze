import sys
sys.stdin = open("herding.in","r")
sys.stdout = open("herding.out","w")

a,b,c = map(int, input().split()) #input cow positions

# we realize there's only 3 ways to find the best (min) possible way
if a+2 ==c:
  print(0)
elif c-b ==2 or b-a==2:
  print(1)
else:
  print(2)

  
#to find max, we find the worse case
print(max(b-a,c-b)-1)

#Examples (best case scenario):
#4 7 9 --> 4 5 7 --> 5 6 7 
#2 9 14 --> 9 13 14 --> 9 11 13
