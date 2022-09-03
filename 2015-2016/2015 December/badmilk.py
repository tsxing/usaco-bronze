import sys
sys.stdin = open("badmilk.in","r")
sys.stdout = open("badmilk.out","w")

N,M,D,S = map(int, input().split())

log = []

for _ in range(D):
  p,m,t = map(int, input().split())
  log.append([p-1,m-1,t]) # -1 to normalize index

for _ in range(S):
  p,t = map(int, input().split())
  log.append([p-1,-1,t])

log.sort(key=lambda x: (x[2],x[1])) #sorted by time

doses = 0
for milk in range(M):
  possible = True
  sickPeople = [False for _ in range(N)]
  for i in log:
    if i[1] == -1: #if person is sick
      if not sickPeople[i[0]]: 
        possible = False #not possible
        break
    elif i[1] == milk: #person drank the milk we're checking
      sickPeople[i[0]] = True #mark person i[0] as sick

  if possible:
    doses = max(sum(sickPeople), doses)

print(doses) 
