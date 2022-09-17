N = int(input())
breedIDs = [int(x) for x in input().split()]

E, O = 0,0

ans = 0

#count # of evens and odds in breedIDs
for i in breedIDs:
  if i%2==0: #even number
    E += 1
  else: #odd 
    O += 1

#if Es = Os, then ans is N. 2 odds can become an even.
while O>E:
  O-= 2 #2 odds make an even
  E+=1 #evens increase 1, since 2 odds made an even
if E>O+1:
  E=O+1
print(E+O)
