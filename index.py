import random

# Function for batting
def bat():
    runs = 0  # Initialize runs to 0
    balls = 0  # Initialize balls to 0
    wickets = 0  # Initialize wickets to 0
    print("\nYou are batting now. Try to score as many runs as possible!")

    # Play 6 balls (1 over)
    while balls < 6 and wickets < 10:
        balls += 1  # Increase ball count after each ball
        print(f"\nBall {balls} - What shot will you play?")
        print("1. Defend (0 runs)")
        print("2. Drive (1 run)")
        print("3. Cut (2 runs)")
        print("4. Sweep (3 runs)")
        print("5. Hit for 6 (6 runs)")
        print("6. Hit for 4 (4 runs)")
        
        # Let the user pick a shot
        shot = input("Enter the shot number (1-6): ")

        # Random outcome if the shot doesn't match
        if shot == "1":
            print("You defend the ball safely. No runs.")
            outcome = 0
        elif shot == "2":
            print("You drive the ball and score 1 run.")
            outcome = 1
        elif shot == "3":
            print("You cut the ball and score 2 runs.")
            outcome = 2
        elif shot == "4":
            print("You sweep the ball and score 3 runs.")
            outcome = 3
        elif shot == "5":
            print("You hit a 6! Well done!")
            outcome = 6
        elif shot == "6":
            print("You hit a 4! Great shot!")
            outcome = 4
        else:
            print("Invalid shot choice. You defend the ball.")
            outcome = 0
        
        runs += outcome  # Add the outcome of the shot to the total runs

        # Random chance for getting out (20% chance)
        if random.randint(1, 10) > 8:
            print("\nOh no! You've been bowled out!")
            wickets += 1
            break
        
    print(f"\nYour batting innings is over! You scored {runs} runs and lost {wickets} wickets.")
    return runs, balls, wickets

# Function for bowling
def bowl():
    runs = 0  # Initialize runs for the bowler
    balls = 0  # Initialize balls for the bowler
    wickets = 0  # Initialize wickets for the bowler
    print("\nYou are bowling now. Try to get the batter out!")

    # Bowl 6 balls (1 over)
    while balls < 6 and wickets < 10:
        balls += 1  # Increase ball count after each ball
        print(f"\nBall {balls} - The batter is ready.")

        # Simulate the result of the ball
        outcome = random.randint(0, 10)

        if outcome == 0:
            print("It's a maiden over!")
        elif outcome == 1:
            print("The batter scores 1 run.")
            runs += 1
        elif outcome == 2:
            print("The batter scores 2 runs.")
            runs += 2
        elif outcome == 3:
            print("The batter scores 3 runs.")
            runs += 3
        elif outcome == 4:
            print("The batter hits a 4!")
            runs += 4
        elif outcome == 5:
            print("The batter hits a 6!")
            runs += 6
        elif outcome >= 6 and outcome < 10:
            print("You bowl a wide or no-ball!")
            runs += 1
        elif outcome == 10:
            print("WICKET! The batter is out!")
            wickets += 1
            break
        
    print(f"\nYour bowling innings is over! The batter scored {runs} runs and you took {wickets} wickets.")
    return runs, balls, wickets

# Main game function
def cricket_game():
    print("Welcome to the Simple Cricket Game!")
    print("In this game, you will either bat or bowl first, then switch roles.")
    print("Let's play!")

    # Let the player choose to bat or bowl first
    choice = input("Do you want to Bat or Bowl first? (Enter 'Bat' or 'Bowl'): ").lower()

    if choice == "bat":
        print("\nYou chose to bat first!")
        player_runs, player_balls, player_wickets = bat()  # Player bats
        print("\nNow it's your turn to bowl!")
        opponent_runs, opponent_balls, opponent_wickets = bowl()  # Player bowls
    elif choice == "bowl":
        print("\nYou chose to bowl first!")
        opponent_runs, opponent_balls, opponent_wickets = bowl()  # Player bowls first
        print("\nNow it's your turn to bat!")
        player_runs, player_balls, player_wickets = bat()  # Player bats after bowling
    else:
        print("Invalid choice. Please choose either 'Bat' or 'Bowl'.")
        return  # End the game if the user enters invalid input

    # Final score display
    print(f"\nFinal Score:")
    print(f"Your Team - Runs: {player_runs}, Balls: {player_balls}, Wickets: {player_wickets}")
    print(f"Opponent Team - Runs: {opponent_runs}, Balls: {opponent_balls}, Wickets: {opponent_wickets}")

    # Determine the winner
    if player_runs > opponent_runs:
        print("\nCongratulations! You won!")
    elif player_runs < opponent_runs:
        print("\nSorry! You lost. Better luck next time.")
    else:
        print("\nIt's a tie! Great game!")

# Run the game
if __name__ == "__main__":
    cricket_game()
