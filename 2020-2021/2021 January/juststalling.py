N = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

def count(x): #x is cow's height
  cnt = 0
  for i in b:
    if x<=i:
      cnt += 1
  return cnt
  
a.sort()
a= a[::-1] #reverse

ans = 1

for i in range(N):
  fit = count(a[i]) -i
  ans*=fit
  

print(ans)



  
        



  
  
    