#doesn't pass on test case 6

correct = []
guess = []

for _ in range(3):
  correct.append(str(input()))
for _ in range(3):
  guess.append(str(input()))

green = 0
for i in range(3):
  for j in range(3):
    if correct[i][j]==guess[i][j]:
      green += 1

  
total = 0
yellow = 0
timesCorrect,timesGuessed = 0,0

usedLetters = []
for i in range(3):
  for j in range(3):

    if correct[i][j] not in usedLetters:
      timesCorrect += sum(x.count(correct[i][j]) for x in correct)
      timesGuessed += sum(x.count(correct[i][j]) for x in guess)
      usedLetters.append(correct[i][j])


  minValforLetter = min(timesCorrect,timesGuessed)
  
  total += minValforLetter
  timesCorrect,timesGuessed = 0,0 #reset
  
print(green)
print(total-green)
