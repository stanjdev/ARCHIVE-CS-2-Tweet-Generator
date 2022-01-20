import sys
import random

# takes in command line keywords into a list
list_of_words = sys.argv[1:]

# randomizes that list,
# returns the words in that list 
def randomize_words():
  random.shuffle(list_of_words)
  return list_of_words


if __name__ == '__main__':
  words_randomized = randomize_words()
  print(' '.join(words_randomized))

