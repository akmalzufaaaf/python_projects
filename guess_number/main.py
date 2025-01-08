from random import randint

lower_num, higher_num = 1, 100
random_number: int = randint(lower_num, higher_num)
print(f"Guess the number in the range {lower_num} to {higher_num}.")

while True:
    try:
        user_quess: int = int(input("Guess: "))
    except ValueError as e:
        print("Please enter a valid number.")
        
    if user_quess > random_number:
        print("The number is lower")
    elif user_quess < random_number:
        print("The number is greater")
    else:
        print("You guessed it!")
        break
    

        