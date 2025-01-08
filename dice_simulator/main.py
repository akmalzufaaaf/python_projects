from random import randint

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = randint(1, 6)
        rolls.append(random_roll)
    
    return rolls

def main():
    total_dice_roll = 0
    while True:
        try:
            user_input: str = input("How many dice would you like to roll? ")
            
            if user_input.lower() == "exit":
                print("Thank you for playing!")
                break
            elif user_input.lower() == "sum":
                print(total_dice_roll)
                continue
            
            total_dice_roll += int(user_input)
            print(*roll_dice(int(user_input)), sep=', ')
        
        except ValueError:
            print("Please enter valid number.")
        
if __name__ == "__main__":
    main()