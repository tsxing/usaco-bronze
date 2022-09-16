import sys #this gets 10th test case wrong for some reason
sys.stdin = open("whereami.in","r")
sys.stdout = open("whereami.out","w")

N = int(input())
s = str(input())
ans = 1 #start at 1

def check(len):
  x = ""
  for i in range(N-len+1): 
    if x.count(s[i:i+len])>0:
      return True
    x= x+s[i:i+len] #for string s, from i, take "len" amount of elements
  return False


while check(ans)==True:
  ans +=1 #ans is K

print(ans)
    
