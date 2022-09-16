import sys
sys.stdin = open("word.in","r")
sys.stdout = open("word.out","w")

N, K = map(int, input().split())
essay = [str(x) for x in input().split()]

formatted = "" #final answer
currLen = 0 #current Length; can't be > K

for w in essay:
  if currLen+len(w)>K: #if current Length and length of word greater than K:
    formatted = formatted[:-1] +"\n" #returns everything but last element
    currLen = 0 #reset current length
  formatted += w + " "
  currLen += len(w)
formatted = formatted[:-1]
print(formatted)
