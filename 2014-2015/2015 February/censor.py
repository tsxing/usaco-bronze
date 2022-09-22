import sys
sys.stdin = open("censor.in","r")
sys.stdout = open("censor.out","w")

S = str(input())
T = str(input())

censored = "" #output
for i in S: #for each letter of S
  censored += i  #add letter i to output
  if censored[-len(T):] ==T: #if the ending of output is the string T we want to censor
    censored = censored[:-len(T)] #remove string T
    
print(censored)
