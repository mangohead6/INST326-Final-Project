import random


def run_minigame(lives, max_number=5):
    """
    Runs a mingame where the player guess a number from 1 to 5. If the user 
    inputs the wrong number the lose a life. Then get to guess again as the 
    number will chance every round. If they lose all their lives the minigame
    ends.
    
    
    Args:
        lives (int): number of lives the user has to play the minigame
        max_number(int): number ceiling or the random number
    
    Returns:
        Number of rounds the user guessed the right nubmer in the var
        rounds_survived
            
    Raises:
        ValueError: if lives is less than 0
    """
    if lives <= 0:
        raise ValueError("lives must be positive")

    rounds_survived = 0

    while lives > 0:
        secret = random.randint(1, max_number)
        print(f"\nRound {rounds_survived + 1} | Lives: {lives}")
        guess_text = input(f"Guess a number from 1 to {max_number}: ")

        if not guess_text.isdigit():
            print("That's not a number. You lose a life!")
            lives -= 1
        elif int(guess_text) == secret:
            print("Correct! You survive this round.")
            rounds_survived += 1
        else:
            print(f"Wrong! It was {secret}. You lose a life.")
            lives -= 1

    print(f"\nYou died after surviving {rounds_survived} rounds.")
    return rounds_survived

if __name__ == "__main__":
    run_minigame(3)