import sys
sys.stdin = open("cbarn.in","r")
sys.stdout = open("cbarn.out","w")

n = int(input())
rs= [] #required cows list
for _ in range(n):
  r = int(input())
  rs.append(r)

#We will calculate min distance for each first-opened door.
  
def shiftArray(arr): #will shift our array (to calculate min distance)
    newarr = [0]*len(arr)
    newarr[0] = arr[-1] #last element of arr is shifted to the 1st element in our new array
    for i in range(len(arr)):
        if i+1 >=len(newarr):
            break
        newarr[i+1]=arr[i]
    return newarr
  
def calculateCows(arr): #Calculate distance of current array
  temp = 0
  j = 0
  for i in range(n): #start from rs[i]. 
    temp += arr[j]*i
    j+=1
  return temp
  
lst = [] #list of distances

for i in range(n):
  rs = shiftArray(rs)
  temp = calculateCows(rs)
  lst.append(temp)
print(min(lst)) #find min distance 



  
