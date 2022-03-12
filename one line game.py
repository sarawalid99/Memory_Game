# Game 5 - One Line Memory Game - Done by : Sara Walid - ID : 20210495
import random
import os
from time import sleep
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
# To arrange letters randomly
random.shuffle(letters)
num1 = 0
num2 = 0
count = 0
score_1 = 0
score_2 = 0

# function takes from player1 two numbers and check if they hide the same letter


def player_one():
    global score_1
    global count
    print(f"Welcome : {numbers}")
    print(f"Player 1 - score : {score_1}")
    num1 = int(input())
    num2 = int(input())
    while num1 > 20 or num2 > 20 or num1 < 1 or num2 < 1:
        num1 = int(input("Invalid Number, Please Choose Another One .."))
        num2 = int(input())
    # To set the index in the list
    i1 = int(num1) - 1
    i2 = int(num2) - 1
    # Making copy from list so can make changes without changing the original list
    num_let = numbers[:]
    # Display letter of the chosen number
    num_let[i1] = letters[i1]
    num_let[i2] = letters[i2]
    print(f"Welcome : {num_let}")
    # clearing screen after player turn
    sleep(5)
    os.system('cls')
    # Checking if the letters are the same, Player get point
    if letters[i1] == letters[i2]:
        score_1 += 1
        # Replacing the number in the list with '*'
        numbers[i1] = '*'
        numbers[i2] = '*'
        # For ending game
        count += 2



player_one()

# function takes from player2 two numbers and check if they hide the same letter


def player_two():
    global score_2
    global count
    print(f"Welcome : {numbers}")
    print(f"Player 2 - score : {score_2}")
    num1 = int(input())
    num2 = int(input())
    while num1 > 20 or num2 > 20 or num1 < 1 or num2 < 1:
        num1 = int(input("Invalid Number, Please Choose Another One .."))
        num2 = int(input())
    i1 = int(num1) - 1
    i2 = int(num2) - 1
    num_let = numbers[:]
    num_let[i1] = letters[i1]
    num_let[i2] = letters[i2]
    print(f"Welcome : {num_let}")
    # clearing screen after player turn
    sleep(5)
    os.system('cls')
    if letters[i1] == letters[i2]:
        score_2 += 1
        numbers[i1] = '*'
        numbers[i2] = '*'
        count += 2


player_two()


def winner():
    if score_1 > score_2:
        print("Player 1 is the winner")
    elif score_2 > score_1:
        print("Player 2 is the winner")
    else:
        print("No winner")

# End the game when count reach 20 (that means : all list elements are '*')


while count != 20:
    player_one()
    player_two()
else:
    winner()
