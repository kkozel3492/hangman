import sys
import hangmanArt

import hangmanFunc

stillPlaying = "y"

while stillPlaying != 'n':
    print(hangmanArt.logo)
    word = hangmanFunc.getRandWord()
    empty = hangmanFunc.buildHangman(word)

    #Create a readable version of the word
    prntWord = ""
    for char in word:  # parse the list
        prntWord += char  # add to empty string

    #Gather Variables
    gameOver = "false"
    i = 0  # Counter variable
    usrLives = 5
    takeLife = "true"
    guessList = []
    stage = 0

    while gameOver != "true":
        if usrLives != 0:
            usrGuess = input("Guess a Letter\n")
            usrGuess = usrGuess.lower()
            guessList.append(usrGuess)
            i = 0  # Counter variable
            takeLife = "true"
            if usrLives >= 0:
                for letter in word:  # Check each letter to see if it is comparable to user choice
                    i += 1  # Count index for each iteration
                    if usrGuess == letter:  # If the user selects the correct word
                        empty[i - 1] = usrGuess  # Set the visualy empty string to the user guess
                        takeLife = "false"  # Set the take life variable to false
                if takeLife != "false":
                    usrLives -= 1
                    stage += 1
                #Create a more readable string for the user
                prntEmpty = "" #Create an empty string
                for c in empty: #parse the list
                    prntEmpty += c #add to empty string
                #print(f"You have {usrLives} lives left")
                #print(prntEmpty)


                #If the user guessed the right word, the game is set ot over
                if empty == word:
                    gameOver = "true"

                print(F"You have guessed the letters  {guessList}" )
                print(f"You have {usrLives} lives left")
                print(prntEmpty)
                print(hangmanArt.stages[stage])
        else:
                gameOver = "true"


    print(f"\nThe word was {prntWord}!")
    stillPlaying = input("Do you want to play again? 'y' or 'n'\n")

sys.exit("Thank you for playing")




