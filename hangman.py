def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is ", len(secretWord), "letters long"
    print "-------------"

    mistakesMade = 8
    lettersGuessed = []

    while mistakesMade >= 0:
        print "You have", mistakesMade, "guesses left"
        print "Available letters: ", getAvailableLetters(lettersGuessed)
        letter = raw_input("Please guess a letter: ")
        letter = letter.lower()
        

        if letter in lettersGuessed:
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)
            print "-------------"
        
        else:
            lettersGuessed.append(letter)
            if letter in secretWord:
               print "Good guess: ", getGuessedWord(secretWord, lettersGuessed)
               print "-------------"
            else:
                mistakesMade = mistakesMade -1
                print "Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)
                print "-------------"
                

        if isWordGuessed(secretWord, lettersGuessed) == True:
                print "Congratulations! You won the game!"
                print "-------------"
                break

        if mistakesMade == 0:
            print "Sorry, you ran out of guesses. The word was", secretWord

