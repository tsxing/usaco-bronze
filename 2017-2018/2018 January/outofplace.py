import sys
sys.stdin = open("outofplace.in","r")
sys.stdout = open("outofplace.out","w")

N = int(input())
heights = []
for _ in range(N):
  h = int(input())
  heights.append(h)

sortedHeights = sorted(heights) #create new list that contains our inputted heights, but sorted

#notice that the amt of swaps is the amt of different elements at the same positions of our lists, subtract 1.

swaps = 0
for i in range(N):
  if sortedHeights[i] != heights[i]:
    swaps += 1

print(swaps-1)

    



