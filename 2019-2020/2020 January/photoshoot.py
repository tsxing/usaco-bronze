import sys
sys.stdin = open("photo.in","r")
sys.stdout = open("photo.out","w")

N = int(input()) #read inputs
b = [int(x) for x in input().split()]
#set a1 to i. i = 1-N

a = [] #initialize list
def checkFunc(arr): #check if our array first the requirements
  if len(set(arr))!=len(arr): #has duplicates
    return False
  else:
    for i in arr:
      if i<1 or i>N: #if i not in range [1,N]
        return False
        break
  return True
             
for i in range(1,N+1):
  a=[]
  a.append(i)
  for i in range(1,N):
    a.append(b[i-1]-a[i-1])
  #print(a)
  if checkFunc(a): #it's true
    break

for i in a:
  if a.index(i) ==N-1: #last element
    print(i)
  else:
    print(i,end=" ")
