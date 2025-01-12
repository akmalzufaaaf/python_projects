from random import choice

def run_game():
    word: str = choice(['Apple', 'Pinapple', 'Durian'])
    
    username: str = input("What is your name? ")
    
    tries: int = 3
    guessed: str = ""
    
    print(f"Welcome to hangman, {username}.")
    print(word)
    
    while tries > 0:
        blanks: int = 0
        
        print("Word: ", end='')
        for char in word.lower():
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1
                
        print()
        
        if blanks == 0:
            print("You got it!")
            break
        
        guess: str = input("Enter a letter: ").lower()
        
        if len(guess) > len(word):
            print("Only enter less or equal with the letter.")
            continue
        else:
            if guess in guessed:
                print(f"You already used: {guess}. Please try another letter!")
                continue
            
            guessed += guess
            
            if guess not in word.lower():
                tries -= 1
                print(f"Sorry, that was wrong... ({tries} tries remaining)")
                
                if tries == 0:
                    print("No more tries remaining... You lose.")
                    break
            
if __name__ == '__main__':
    run_game()
