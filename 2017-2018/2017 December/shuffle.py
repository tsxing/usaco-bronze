import sys
sys.stdin=open("shuffle.in","r")
sys.stdout = open("shuffle.out","w")
            
n = int(input())
a = [int(x) for x in input().split()]
ids = [int(x) for x in input().split()]

def solve(arr):
  newArr = [0]*n
  for i in range(0,n):
    newArr[i] = arr[a[i]-1]
  return newArr
  
for _ in range(3):
  ids = solve(ids)

for i in ids:
  print(i)

