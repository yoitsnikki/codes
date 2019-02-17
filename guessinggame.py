'''
The Guessing Game- Count the number of guesses
By Nikki Agrawal
7B D2
Mrs. Dastur
April 24, 2017
'''

MAXNUMOFGUESSES = 10

Redo = "yes"

while Redo.lower()== "yes":
    print("Hello. Welcome to the Guessing Game. If you lose, your life is mine. Good Luck.")

    guess= input("What type of guessing game would you like to play? Your choices are books, movies, subjects, teachers, sports, and colors.")

    # keeps a counter for number of incorrect guesses
    score= 0

    if guess.lower()== "books":
        favBook= input("Guess my favorite book.  ")

        while favBook.lower() != "harry potter":
            print("Incorrect! You guessed " + str(favBook) +  ". Your life is mine! Muah ha ha ha ha! Since I am nice, I will give you another chance.")
            score= score + 1
            favBook= input("Guess my favorite book.  ")

            if (score == MAXNUMOFGUESSES):
                print("I'm afraid you took to long and now you have lost. Your life is mine now! Yay! Cookies!")
                Redo= input("Would you like to play again?")
                break

            elif (score == 5):
                hint = input("Would you like a hint?")

                if hint.lower() == "yes":
                    favBook = input("This book series of 7 books is written by a woman. Try again. What is my favorite book?")

        if favBook.lower() == "harry potter":
            print("You were correct. Darn. You took " + str(score) + " guesses. I would still like your life. :)")

        Redo= input("Would you like to play again?")

    # keeps a counter for number of incorrect guesses
    score= 0
    
    if guess.lower()== "movies":
        favMovie= input("Guess my favorite movie.  ")

        while favMovie.lower() != "the hobbit":
            print("Incorrect! You guessed " + str(favMovie) +  ". Your life is mine! Muah ha ha ha ha! Since I am nice, I will give you another chance.")
            score= score + 1
            favMovie= input("Guess my favorite movie.  ")

            if (score == MAXNUMOFGUESSES):
                print("I'm afraid you took to long and now you have lost. Your life is mine now! Yay! Cookies!")
                Redo= input("Would you like to play again?")
                break

            elif (score == 5):
                hint = input("Would you like a hint?")

                if hint.lower() == "yes":
                    favMovie = input("This movie is written by a British man who is dead and involves mystical creatures and characters. Try again. What is my favorite movie?")

        if favMovie.lower() == "the hobbit":
            print("You were correct. Darn. You took " + str(score) + " guesses. I would still like your life. :)")

        Redo= input("Would you like to play again?")

    # keeps a counter for number of incorrect guesses
    score= 0

    if guess.lower()== "colors":
        favColor= input("Guess my favorite color.  ")

        while favColor.lower() != "verditer":
            print("Incorrect! You guessed " + str(favColor) +  ". Your life is mine! Muah ha ha ha ha! Since I am nice, I will give you another chance.")
            score= score + 1
            favColor= input("Guess my favorite Color.  ")

            if (score == MAXNUMOFGUESSES):
                print("I'm afraid you took to long and now you have lost. Your life is mine now! Yay! Cookies!")
                Redo= input("Would you like to play again?")
                break

            elif (score == 5):
                hint = input("Would you like a hint?")

                if hint.lower() == "yes":
                    favBook = input("This color is nearly unknown but is a shade of green. Try again. What is my favorite color?")

        if favColor.lower() == "verditer":
            print("You were correct. Darn. You took " + str(score) + " guesses. I would still like your life. :)")


        print("You were correct. Darn. You took " + str(score) + " guesses. I would still like your life. :)")
        Redo = input("Would you like to play again?")

    # keeps a counter for number of incorrect guesses
    score= 0

    if guess.lower()== "teachers":
        favTeacher= input("Guess my favorite teacher.  ")

        while favTeacher.lower() != "none":
            print("Incorrect! You guessed " + str(favTeacher) +  ". Your life is mine! Muah ha ha ha ha! Since I am nice, I will give you another chance.")
            score= score + 1
            favTeacher= input("Guess my favorite Teacher.  ")

        print("You were correct. Darn. You took " + str(score) + " guesses. I would still like your life. :)")
        Redo = input("Would you like to play again?")

     # keeps a counter for number of incorrect guesses
    score= 0

    if guess.lower()== "subjects":
        favSubject= input("Guess my favorite subject.  ")

        while favSubject.lower() != "specialty":
            print("Incorrect! You guessed " + str(favSubject) +  ". Your life is mine! Muah ha ha ha ha! Since I am nice, I will give you another chance.")
            score= score + 1
            favSubject= input("Guess my favorite subject.  ")

        print("You were correct. Darn. You took " + str(score) + " guesses. I would still like your life. :)")
        Redo = input("Would you like to play again?")

    # keeps a counter for number of incorrect guesses
    score= 0

    if guess.lower()== "sports":
        favSport= input("Guess my favorite sport.  ")

        while favSport.lower() != "skiing":
            print("Incorrect! You guessed " + str(favSport) +  ". Your life is mine! Muah ha ha ha ha! Since I am nice, I will give you another chance.")
            score= score + 1
            favSport= input("Guess my favorite subject.  ")

        print("You were correct. Darn. You took " + str(score) + " guesses. I would still like your life. :)")
        Redo = input("Would you like to play again?")

else:
    print("OK. Thank you for playing the guessing game. Type in the words, 'I am dumb' to give me your life.")
