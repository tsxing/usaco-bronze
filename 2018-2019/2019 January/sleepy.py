import sys
sys.stdin = open("sleepy.in","r")
sys.stdout = open("sleepy.out","w")

N = int(input())
p = [int(x) for x in input().split()] 
#reverse p=[i+1,i,i-1]
#        p=[i-1,i,i+1]
ans = 0
for i in range(N-1,0,-1): #reverse and find sorted elements
  if p[i]<p[i-1]:
    ans = i
    break

print(ans)

#above code searches list p in reverse. the i and i-1 are when p is reversed. p[i]<p[i-1] would mean the same as p[i]<p[i+1]. this finds the amt of sorted elements from the end of our list p.
#in p = [1,2,4,3], [3] (which is 1 element) is "sorted". so answer is N-1 = 4-1 = 3. or, 1<2 when i=3 (in reverse). ans is then 3.

#n- (amt of elements thats sorted) is the answer



  
