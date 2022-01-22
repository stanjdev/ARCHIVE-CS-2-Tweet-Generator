# https://makeschool.org/mediabook/oa/tutorials/tweet-generator--data-structures---probability-with-python/analyze-word-frequency-in-text/
import sys

file = str(sys.argv[1])

def read_file(filename):
  f = open(filename, 'r', encoding='utf-8-sig')
  words = f.read()
  f.close()
  return words

""" 
docstring
source_text: string
 """
def histogram_dict(source_text):
  dict = {}
  for word in source_text:
    if word in dict.keys():
      dict[word] += 1
    else:
      dict[word] = 1
  return dict



# FREEZES. Too slow? Or stuck???
def histogram_list(source_text):
  lst = []
  for word in source_text:
    if len(lst) > 0:
      for pair in lst:
        if word in pair:
          pair[1] += 1
          continue
    lst.append([word, 1])
  return lst




def histogram_tuple(source_text):
  pass


def unique_words(dict):
  return len(dict)
  # returns the total count of unique words in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.

""" 
word:
histogram: 
 """
def frequency(word, histogram):
  if type(histogram) == '':
    pass
  elif type(histogram) == '':
    pass
  elif type(histogram) == '':
    pass

  # returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.



if __name__ == '__main__':
  corpus_list = read_file(file).replace(',', '').replace('.', '').lower().split()
  
  # histogram_dictionary = histogram_dict(corpus_list)
  # print(histogram_dictionary)
  # print(unique_words(histogram_dictionary))

  histogram_list = histogram_list(corpus_list)
  print(histogram_list)


