from __future__ import division
import io


def initArray():
  array = []
  for i in range(27):
    temp = []
    for j in range(27):
      temp.append(0)
    array.append(temp[:])
  return array

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


def readFile(filename):
  infile = io.open(filename, "r")
  text = infile.read()
  letters = parse(text)
  return letters
  
def populateNums(letters, nums):
  for i in range(len(letters) - 1):
    current = ord(letters[i]) - 97
    after = ord(letters[i + 1]) - 97

    #rows = letter in question; cols = letter that came before that letter
    nums[after][current] += 1
  return nums

def populateProb(nums, prob):
  for i in range(27):
    sumrow = 0
    for j in range(27):
      sumrow += nums[i][j]
      prob[i][j] = 0.0
    if (sumrow != 0):
      for k in range(27):
        prob[i][k] = nums[i][k] / sumrow
  return prob

def printArray(array):
  print("    "),
  for d in range(len(array)):
    print(chr(d + 97) + "     "),
  print
  m = 0
  for row in array:
    print "%s [%s]" % (chr(m + 97), ', '.join('%.3f' % i for i in row))
    m += 1
  return

def fileToProb(text):
  letters = readFile(text)
  nums = initArray()
  prob = initArray()
  populateNums(letters, nums)
  populateProb(nums, prob)
  return prob

def forward(probA, probB, fileName):
  scoreA = 0.0
  scoreB = 0.0
  letters = readFile(fileName)

  for i in range(1, len(letters)):
    index = ord(letters[i]) - 97
    scoreA += probA[index][index - 1]
    scoreB += probB[index][index - 1]
  print("Score A:  " + str(scoreA))
  print("Score B:  " + str(scoreB))


def main():
  probA = fileToProb("testmarkov.txt")
  probB = fileToProb("testmarkovB.txt")
  
  forward(probA, probB, "interrogator.txt")
  """
  print("Probability Matrix A")
  printArray(probA)
  print("Probability Matrix B")
  printArray(probB)"""

main()
