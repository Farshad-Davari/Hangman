import random as r
import time as t

class Hangman:
  def __init__(self, name, iteration, flag ,score=5):
    self.name = name
    self.iteration = iteration
    self.score = score
    self.flag = flag

  def greeting(self):
    self.name = input("Please enter your name: ")
    print("--------------------------------------------------------")
    t.sleep(2)
    print(f"Hello {self.name}. Welcome to hangman Game!")
    print("--------------------------------------------------------")
    print(f"{self.name}! How many round you want to play? (5/10/15)")
    self.iteration = int(input("Enter your round: "))
    if self.iteration == 5  or self.iteration == 10 or self.iteration == 15:
      self.flag = True
      print("--------------------------------------------------------")
      t.sleep(2)
      print("Lets begin the game!")
      print(f"Your current score is: {self.score}")
      print("--------------------------------------------------------")
    else:
      self.flag = False
      print("Invalid round!")

  def play(self):
    words = ["dog", "cat", "car", "human", "color", "laptop", "python", "earth", "war", "finger"]
    
    if self.flag == True:
      for i in range(self.iteration):
        word = ""
        wordsLength = len(words)
        randNum = r.randint(0, wordsLength)
        for i in range(wordsLength):
          word = words[randNum]

        currentWord = list(word)
        currentWord[1] = "_"
        incomplete = "".join(currentWord)
        print(f"Word: {incomplete}")
        userChoice = input("Guess the word: ")

        if userChoice == word:
          self.score += 5
          print(f"Congratulations {self.name}! Your score is {self.score}")
          print("--------------------------------------------------------") 
        else:
          self.score -= 5
          print(f"Shit {self.name}! Your score is {self.score}")  
          print("--------------------------------------------------------")     


  def run(self):
    self.greeting()     
    self.play()