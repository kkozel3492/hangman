import random
# Create a list of strings that will act as answers
#wordBank = []  # Initiate empty list

# Create a function to get a random word
def getRandWord():
    wordBank = open('hangmanList.txt', "r").read().splitlines()
    spltLst = []  # Initiate an empty list
    bankLen = len(wordBank) - 1  # Find the length of the list, subtract one to adjust index
    randNum = random.randint(0, bankLen)  # Grab a random number between 0, and the end of the list
    chosenWord = wordBank[randNum]  # Use random number to select index of word
    chosenWord = chosenWord.lower()  # Make word lower case for easy comparison
    for letter in chosenWord:  # fill the empty list with letters in the chosen word
        spltLst.append(letter)
    return spltLst


# Creating a list that will be updated with user Guesses
def buildHangman(word):
    wordLen = len(word)  # Gather the length of the word
    usrGuess = []
    for i in range(0, wordLen):
        usrGuess.append("_")
    return usrGuess