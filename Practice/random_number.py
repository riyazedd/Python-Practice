import random

max_num=int(input("Enter a number= "))

guesses=0
rand=random.randrange(max_num)

while True:
    guesses +=1
    guess=int(input("Make a guess= "))
    
    if guess>max_num:
        print("Invalid guess...Guess within the number")
        continue
    
    if guess!=rand:
        print("You guessed wrong...")
        continue
    else:
        print("You got it right...")
        break

print(f"You got it in {guesses} guesses")
        


