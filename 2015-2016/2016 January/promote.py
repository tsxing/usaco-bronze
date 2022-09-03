import sys
sys.stdin=open("promote.in","r")
sys.stdout = open("promote.out","w")

#inputs
before, after = map(int, input().split())
bronze = [before,after]
before, after = map(int, input().split())
silver = [before,after]
before, after = map(int, input().split())
gold = [before,after]
before, after = map(int, input().split())
plat = [before,after]

platPromotes = plat[1]-plat[0]
goldPromotes = platPromotes+gold[1]-gold[0]
silverPromotes = goldPromotes + silver[1]-silver[0]

#output answer
print(silverPromotes)
print(goldPromotes)
print(platPromotes)
