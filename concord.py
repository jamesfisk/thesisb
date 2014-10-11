import os
import io
import json

def parse(line):
  words = line.split()
  for word in words:
    word = word.lower()
    if word.isdigit():
      words.remove(word)
  return words

def addToC(word, play, conc):
  #new word
  if not conc.has_key(word):
    conc[word] = [[play, 1]]
  #seen before
  else:
    found = False
    for elt in conc[word]:
      if elt[0] == play:
        elt[1] += 1
        found = True
    if not found:
      conc[word].append([play, 1])


def main():
  path = "/Users/jamesfisk/Desktop/thesis/allplays"
  plays  = os.listdir(path)
  plays.remove(".DS_Store")
  conc = {}

  print(plays)
  #go into each play
  for play in plays:
    print(play)
    infile = io.open(path + "/" + play, "r")
    line = infile.readline()
    print(line)

    #in each play, build concordance
    while line:
      line = infile.readline()
      words = parse(line);
      for word in words:
        addToC(word, play, conc)

  #write concordance to file
  json.dump(conc, open("concordance.txt", "w"))

main()
