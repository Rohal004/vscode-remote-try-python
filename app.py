#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------


#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def hello():
 #   return app.send_static_file("index.html")

import random

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please enter your choice again.")
        user_choice = input("(rock/paper/scissors): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'You win!'
    else:
        return 'Computer wins!'

def play_game():
    player_score = 0
    computer_score = 0
    play_again = 'yes'
    while play_again.lower() == 'yes':
        user_choice = get_user_choice()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if 'win' in result:
            player_score += 1
        elif 'lose' in result:
            computer_score += 1
        print(f"Your score: {player_score}, Computer's score: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thanks for playing!")
    print(f"Final Score - Your score: {player_score}, Computer's score: {computer_score}")

# Start the game
play_game()
