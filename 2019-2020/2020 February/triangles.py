from itertools import permutations
import sys
sys.stdin = open("triangles.in","r")
sys.stdout = open("triangles.out","w")

N = int(input())
points = []
for _ in range(N):
  x,y = map(int, input().split())
  points.append([x,y])

allPermutations = permutations(points,3) #generate all permutations with size 3

area = 0
for i in allPermutations:
  if i[0][1] == i[1][1] and i[1][0] == i[2][0]: 
    #first condition  checks if it's parallel to x-axis. They have equal y values. vice versa for y-axis.
    area = max(area,abs(i[0][0]-i[1][0])*abs(i[1][1]-i[2][1]))

print(area)

#problem notes:
#note how to generate permutations with itertools 
