import pwinput
import time
txt = "WELCOME TO 'GUESS THE WORD'"
cent = txt.center(130)
print("\n", cent)

def game():
    print(f"{b} should enter the below details.")
    time.sleep(0.5)
    len_word = int(input("Enter the length of the word: "))
    word = pwinput.pwinput("Enter the word: ")
    wo_rd = word.lower()
    guesses = int(input("How many guess you want to give: "))
    hint = input("Please enter some hint to guess: ")
    time.sleep(0.5)
    print(f"{c}'s Turn to guess the word")
    print(f"you have {guesses} turns left")
    print(f"The first letter of the word to guess is {wo_rd[0]} and length is {len_word}")
    print(f'hint : {hint}')
    guessed = ""

    while guesses > 0 :
        guess = input("guess the word: ")
        guessed = guess.lower()
    
        if guessed==wo_rd:
            print("YOU WON!!!")
            break

        print(f'you have {guesses-1} turns left')
        guesses -= 1

    if guessed != wo_rd:
        print("YOU LOSE.")
        
while True:
    time.sleep(0.5)
    a = input("Press 1 to Play \t Press 0 to exit\n")
    if a == "1":
        b = input("Enter the 1st player name: ")
        c = input("Enter the 2nd player name: ")
        game()
    elif a == "0":
        print("Thank you for Playing")
        break
    else:
        print("invalid entry")