from __future__ import division
import io

class markov(object):
  def __init__(self, textfile):
    self.letters = readFile(textfile)
    self.nums = initArray()
    self.prob = initArray()
    populateNums(self.letters, self.nums)
    populateProb(self.nums, self.prob)

def readFile(self, filename):
  infile = io.open(filename, "r")
  text = infile.read()
  letters = parse(text)
  return letters

def parse(text):
  text = text.lower()
  letters = list(text)
  newletters = []
  for letter in letters:
    if ((ord(letter) == 10) or (ord(letter) == 32)):
      newletters.append('{')
    #only allow lower case letters and spaces
    elif((ord(letter) >= 97) and (ord(letter) <= 122)):
      newletters.append(letter)
  return newletters

def initArray(self):
  array = []
  for i in range(27):
    temp = []
    for j in range(27):
      temp.append(0)
    array.append(temp[:])
  return array
