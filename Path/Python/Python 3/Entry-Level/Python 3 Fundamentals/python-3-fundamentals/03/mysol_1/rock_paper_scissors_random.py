import sys
import random

computer_choice = random.choices(
    population=['rock', 'paper', 'scissors'],
    weights=[0.7, 0.2, 0.1]  # probabilities must sum to 1.0
)[0]

while True:
    user_input = input("Choose rock (R), paper (P), or scissors (S):\n").strip().lower()

    # Convert single-letter shortcuts to full words
    if user_input == 'r':
        user_choice = 'rock'
    elif user_input == 'p':
        user_choice = 'paper'
    elif user_input == 's':
        user_choice = 'scissors'
    else:
        # Check if they typed the full word
        if user_input in ['rock', 'paper', 'scissors']:
            user_choice = user_input
        else:
            # Invalid choice, ask if user wants to retype or exit
            while True:
                print("Invalid choice!")
                retype_or_exit = input("Press 1 to retype, or 2 to exit: ").strip()

                if retype_or_exit == '1':
                    # Go back to the top of the outer loop to retype
                    break
                elif retype_or_exit == '2':
                    print("Exiting...")
                    sys.exit(0)
                else:
                    # If the user enters something else (e.g., '3'), ask again
                    print("Invalid option. Try again.")

            # After 'break' from the inner loop, continue the outer loop
            continue
    break  # If we got here, user_choice is valid; break out of the loop

# From this point on, user_choice has a valid value: "rock", "paper", or "scissors"
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('WIN')





    
else:
    print('You lose :( Computer wins :D')

