import sys
import random
from histogram import read_file, histogram_dict

file = str(sys.argv[1])

if __name__ == '__main__':
  words_list = read_file(file).split()
  index = random.randint(0, len(words_list) - 1)

  print(words_list[index])





""" 
Stochastic Sampling, 
Accumulate word count through list
where a uniform random number splits it

Distillation (values of)
fenceposts, denoting where the certain words occur

If I roll a 3, ask "what is number greater than and what's the next fencepost?"


1 2 3 4 5 6 7 8
|       | | | |
one     fish, etc.. 


 """





