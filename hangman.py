import random
import time

wordList = ("Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Luxembourg", "Malta", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden")

def mainStr():
   global word, Space, tempWord, countWrong, game, outputStr, Tab, Tab2, Tab3
   word = random.choice(wordList).upper()
   Space = list("-"*len(word))
   tempWord = list(word)
   countWrong = 0
   game = True
   outputStr = ""
   Tab = round(16-len(word)/2)*" "
   Tab2 = 4*" * "
   Tab3 = 11*" "
mainStr()

line1 = "    __________    "
line2 = "    | /           "
line3 = "    |/            "
line4 = "    |             "
line5 = "    |             "
line6 = "    |             "
line7 = "   _|____________ "

addLine0 = "    __________   "
addLine1 = "    | /     |    "
addLine2 = "    |/      O    "
addLine3 = "    |      /T\   "
addLine4 = "    |       |    "
addLine5 = "    |      / \   "
addLine6 = "   _|____________"

introLines = (line1, line2, line3, line4, line5, line6, line7) 
addIntroLines = (addLine1, addLine2, addLine3, addLine4, addLine5, addLine6)

def drawHangman():
   Hangman = introLines[0:1] + addIntroLines[0:countWrong] + introLines[countWrong+1:7]
   for line in Hangman:
      print(line)
      time.sleep(0.1)

def inputLetter():
   global game, countWrong, inLetter
   inLetter = input("Your choice: ").upper()
   if inLetter in tempWord:
      print("\n")
      drawHangman()
      print("\n")
      return inLetter
   elif len(inLetter) > 1:
      print("You have to insert only one letter!!!")
      inputLetter()
   elif len(inLetter) == 0:
      print("\nBe careful! You can die.\n")
      inputLetter()
   else:
      print(f"\n{Tab2}Wrong letter!!!{Tab2}")
      time.sleep(0.5)
      countWrong += 1
      print(f"{Tab3}{countWrong}/5 steps to die!{Tab3}\n")
      time.sleep(0.5)
      drawHangman()
      if countWrong == 5:
         print("\n\nYou're dead!!!\n")
         print(f"The name of country is: {word}\n\n")
         playAgain()

def playAgain():
   global game
   runAgain = input("Do you wanna play again? (Y/N): ").lower()
   if runAgain == "y":
      mainStr()
      mainGame()
   elif runAgain == "n":
      game = False
      return runGame()
   else:
      print("No correct option!")
      playAgain()

def mainGame():
   introHeader = ("""

          Welcome to game:
             'HANGMAN'

    Try to guess name of country.
 You have only 5 wrong tries to save
             your LIFE!.
       """)
   for i in introHeader:
     print(i, end="")
     time.sleep(0.05)
   SpaceIntro = " ".join(Space)
   print(f"\n{Tab}{SpaceIntro}\n\n")

   def findLetter():
      inputLetter()
      global tempWord, Space, outputStr
      count = 0
      for letter in tempWord:
         count += 1
         if letter == inLetter:
            count -= 1
            Space[count] = inLetter
            outputStr = " ".join(Space)
            tempWord[count] = "-"
            return tempWord

   i = "-"
   while i in Space:
      findLetter()
      print(f"\n{Tab}{outputStr}\n\n")

   if i not in Space:
      print("\n\nCongratulation.\nYou're survivor!!!\n\n")
      time.sleep(1)
      playAgain()


def runGame():
   if game == True:
      mainGame()
      mainStr()
   elif game == False:
      endGame = """
        Thank you for playing game.
               'HANGMAN'.

                          """
      for i in endGame:
        print(i, end="")
        time.sleep(0.05)
      exit()
runGame()
