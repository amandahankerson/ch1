import random

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = "rock"
elif random_choice == 1:
    computer_choice = "paper"
elif random_choice == 2:
    computer_choice = "scissors"

user_choice = input("Want to play a social distance game? choose ---> rock, paper or scissors: ")

if computer_choice == "paper" and user_choice == "rock":
    winner = "I am the winner! Want to quit while I'm ahead?"

elif computer_choice == "paper" and user_choice == "scissors":
    winner = "You win. Lucky guess!"

elif computer_choice == "rock" and user_choice == "scissors":
    winner = "Me me me. I crushed you!"

elif computer_choice == "rock" and user_choice == "paper":
    winner = "You got this round! Let's play again."

elif computer_choice == "scissors" and user_choice == "paper":
    winner = "Aha, I gooooot you!!!"

elif computer_choice == "scissors" and user_choice == "rock":
    winner = "You won, for now. I bet you can't do that again!"

elif computer_choice == "scissors" and user_choice == "scissors":
    winner = "Tie, tie, pie in your eye!"

elif computer_choice == "rock" and user_choice == "rock":
    winner = "Twinsies!"

elif computer_choice == "paper" and user_choice == "paper":
    winner = "Copycat!"

else:
    winner = "silly, check your spelling. you need to type either 'rock' 'paper' or 'scissors'"

print("I chose " + computer_choice + " and you chose " + user_choice + ". " + winner)



