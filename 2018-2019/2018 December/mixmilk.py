import sys
sys.stdin = open("mixmilk.in","r")
sys.stdout = open("mixmilk.out","w")

c1,m1 = map(int, input().split())
c2,m2 = map(int, input().split())
c3,m3 = map(int, input().split())

milks = [m1,m2,m3]
c = [c1,c2,c3]

def pour(a,b,i):
  
  if milks[a] + milks[b] <= c[i]:
    milks[b] += milks[a]
    milks[a] = 0
  else:
    change = milks[b]-c[i]
    milks[b] = c[i]
    milks[a] += change

for _ in range(33):
  pour(0,1,1)
  pour(1,2,2)
  pour(2,0,0)
pour(0,1,1)

for i in milks:
  print(i)


