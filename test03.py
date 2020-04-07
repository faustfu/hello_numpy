from random import randrange
import random

print(randrange(0, 100, 1)) # get random integer number between 0 and 100.

random.seed()
result = []
for i in range(100):
  result.append(random.betavariate(1,0.5))

result.sort()

for i in range(100):
  print(result[i])
