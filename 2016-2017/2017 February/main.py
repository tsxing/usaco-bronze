import sys
sys.stdin = open("circlecross.in","r")
sys.stdout = open("circlecross.out","w")

s = str(input()) #read input 

pairs = 0 #ans
#find if there's a patter like ABAB
for a in range(52): #theres 52 letters in our inputted str
  for b in range(a+1,52):
    for c in range(b+1,52):
      for d in range(c+1,52):
        if s[a]==s[c] and s[b]==s[d]:
          pairs += 1

print(pairs)
    



