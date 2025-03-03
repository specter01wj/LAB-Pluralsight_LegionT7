import random

def roll_dice():
    """Simulate rolling two six-sided dice and return the total."""
    return sum(random.choices(range(1, 7), k=2))  # More scalable

def play_round(player1, player2):
    """Play a single round and determine the winner."""
    roll1 = roll_dice()
    roll2 = roll_dice()

    print(f"{player1} rolled {roll1}")
    print(f"{player2} rolled {roll2}")

    if roll1 > roll2:
        print(f"{player1} wins! 🎉")
    elif roll2 > roll1:
        print(f"{player2} wins! 🎉")
    else:
        print("It's a tie! 🤝")

def main():
    """Main game loop allowing multiple rounds."""
    player1 = input("Enter Player 1's name:\n").strip()
    player2 = input("Enter Player 2's name:\n").strip()

    if not player1 or not player2:
        print("Both players must have names! Please restart.")
        return

    while True:
        play_round(player1, player2)
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("Thanks for playing! 🎲")
            break

if __name__ == "__main__":
    main()
