#gets testcase 3 and 11 wrong for some reason, if anyone sees where the error is, please let me know!

import sys
sys.stdin = open("notlast.in","r")
sys.stdout = open("notlast.out","w")

N = int(input())
names = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle","Maggie", "Henrietta"]
log = []
combo =[[0 for x in range(2)] for i in range(7)]

for _ in range(N):
  name,milk = map(str,input().split())
  milk = int(milk)
  log.append([name,milk])
for i in range(7):
  combo[i][0] = names[i]
for i in range(N):
  if log[i][0] =="Bessie":
    combo[names.index("Bessie")][1] += log[i][1]
  if log[i][0] =="Elsie":
    combo[names.index("Elsie")][1] += log[i][1]
  if log[i][0] =="Daisy":
    combo[names.index("Daisy")][1] += log[i][1]
  if log[i][0] =="Gertie":
    combo[names.index("Gertie")][1] += log[i][1]
  if log[i][0] =="Annabelle":
    combo[names.index("Annabelle")][1] += log[i][1]
  if log[i][0] =="Maggie":
    combo[names.index("Maggie")][1] += log[i][1]
  if log[i][0] =="Henrietta":
    combo[names.index("Henrietta")][1] += log[i][1]

combo.sort(key=lambda x: x[1])
amt = combo[0][1]

for i in range(7):
  if amt != combo[i][1]:
    print(combo[i][0])
    break
  if combo[i][0]==combo[i][1]==combo[i][2]==combo[i][3]==combo[i][4]==combo[i][5]==combo[i][6]:
    print("Tie")
