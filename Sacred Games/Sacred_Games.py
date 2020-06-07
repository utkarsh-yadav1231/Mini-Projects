#This code is written by Utkarsh Yadav
import random
def game():

    word = random.choice(["mumbai" , "delhi" , "bandra" , "hyderabad" , "punjab" , "islamabad" , "kolkata" , "chennai" , "chandigarh" , "bangalore" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("\n Hurray !  You have won this game and saved Mr. Gaitonde from commiting suicide ! \n\n")
            break

        print("\n Location Codeword :  " , main)
        guess = input("\n Input a letter : ")
        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Please, Enter a valid character between(a-z)")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left now ")
                print("  --------  ")
            if turns == 8:
                print("8 turns left now")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left now")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left now")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left now")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left now")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left now")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left, Save him he's gonna die soon")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turn left \n")
                print("Last breaths counting, Rope is ready !")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("Ah! You loose")
                print("You let a kind man die. R.I.P. Mr Gaitonde")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("\n\n Please Enter your name :  ")
print(" Welcome to the Sacred Games Season 1," , name )
print("\n ----------------------------------------------")
print(" Rules : You have to guess the below hidden word. \n")
print("\n (1)  : If you made a correct guess, all those letters present in the hidden word would be visible in that single word  ")
print("\n (2)  : If you made a wrong guess,then your attempts will decrease and if you are not able to guess the correct word then after all 10 wrong guesses made by you, our hero(Mr. Gaitonde) will attempt suicide and would die eventually.  ")

print("\n\n Try to guess the word in less than 10 attempts. ")

print("\n ----------------------------------------------\n\n")
game()
print()
