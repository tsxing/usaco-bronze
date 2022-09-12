import sys
sys.stdin = open("shuffle.in","r")
sys.stdout = open("shuffle.out","w")

N = int(input())
a = [int(x) for x in input().split()]
afterShuffles = [int(x) for x in input().split()]
def reShuffle(arr):
  newArr = [0]*N
  for i in range(N):
    newArr[i] = arr[a[i]-1]
  return newArr

for i in range(3):
  reShuffle(afterShuffles)
ans = reShuffle(reShuffle(reShuffle(afterShuffles)))

for i in range(N):
  print(ans[i])


