import sys
sys.stdin = open("mixmilk.in","r")
sys.stdout = open("mixmilk.out","w")

c1,m1 = map(int, input().split()) #input capacities and current milk
c2,m2 = map(int, input().split())
c3,m3 = map(int, input().split())

milks = [m1,m2,m3] #milk amounts
cs = [c1,c2,c3] #capacities

#he pours as much milk as possible until either bucket a becomes empty or bucket b becomes full.

def pourAtoB(a,b):
  if milks[0]+milks[1]<=c2:
    milks[1]+=milks[0]
    milks[0]= 0
  else:
    change = milks[0]+milks[1]-c2
    milks[1] = c2 
    milks[0] = change

def pourBtoC(b,c):
  if milks[1]+milks[2]<=c3:
    milks[2]+=milks[1]
    milks[1]= 0
  else:
    change = milks[1]+milks[2]-c3
    milks[2] = c3 
    milks[1] = change
    
def pourCtoA(c,a):
  if milks[2]+milks[0]<=c1:
    milks[0]+=milks[2]
    milks[2]= 0
  else:
    change = milks[2]+milks[0]-c1
    milks[0] = c1
    milks[2] = change 

for i in range(1,34):
  pourAtoB(milks[0],milks[1])
  pourBtoC(milks[1],milks[2])
  pourCtoA(milks[2],milks[0])


pourAtoB(milks[0],milks[1])

for i in range(3):
  print(milks[i])


