import sys
import random

# random.randint()
# OR, can randomly select 7 indexes, pull those out of the list and return those

def read_file():
  # f = open('words.txt', 'r')
  f = open('/usr/share/dict/words', 'r')
  words = f.readlines()
  f.close()
  # list_of_words = words.split(" ")
  return words

def randomize_file_words(list_of_words):
  random.shuffle(list_of_words)
  return list_of_words

if __name__ == '__main__':
  if len(sys.argv) > 1:
    number_of_words = int(sys.argv[1])
  else:
    print('Enter a number!')
    exit(0)
  shuffled_words = randomize_file_words(read_file())
  print(''.join(shuffled_words[0:number_of_words]))



