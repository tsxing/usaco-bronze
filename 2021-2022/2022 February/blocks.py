N = int(input())
blocks = [input() for _ in range(4)]
words = set()

#make every possible word (1-4 letters) we can make with letters in blocks. store the words to the set "words".
for a in range(4):
  for b in range(4):
    if a in [b]:
      continue
    for c in range(4):
      if c in [a,b]:
        continue
      for d in range(4):
        if d in [a,b,c]:
          continue
        for letter1 in blocks[a]:
          words.add(letter1)
          for letter2 in blocks[b]:
            words.add(letter1+letter2)
            for letter3 in blocks[c]:
              words.add(letter1+letter2+letter3)
              for letter4 in blocks[d]:
                words.add(letter1+letter2+letter3+letter4)

#check if the inputted word can be formed with blocks; i.e., check if input is in word set.
for _ in range(N):
  if input() in words:
    print("YES")
  else:
    print('NO')
            
