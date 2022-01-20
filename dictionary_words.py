import sys
import random

number_of_words = int(sys.argv[1:][0])

# OR, can randomly select 7 indexes, pull those out of the list and return those

f = open('words.txt', 'r')
words = f.read()
list_of_words = words.split(" ")

def randomize_file_words():
  random.shuffle(list_of_words)
  return list_of_words

if __name__ == '__main__':
  shuffled_words = randomize_file_words()
  print(' '.join(shuffled_words[0:number_of_words]))


