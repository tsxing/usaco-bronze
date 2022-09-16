cowphabet = str(input())
word = str(input())

times = 1
for i in range(len(word)-1):
  if cowphabet.index(word[i+1])<=cowphabet.index(word[i]): #if letter in word is after the next letter in word (in cowphabet)
    times += 1
print(times)
    
        



  
  
    