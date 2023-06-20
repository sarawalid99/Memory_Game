import random
import os
from time import sleep

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
random.shuffle(letters)

num1 = 0
num2 = 0
count = 0
score_1 = 0
score_2 = 0

def player_turn(player_num):
    global score_1, score_2, count
    print(f"Welcome : {numbers}")
    print(f"Player {player_num} - Score: {score_1 if player_num == 1 else score_2}")

    num1 = get_valid_number("Enter the first number: ")
    num2 = get_valid_number("Enter the second number: ")

    i1 = num1 - 1
    i2 = num2 - 1

    num_let = numbers[:]
    num_let[i1] = letters[i1]
    num_let[i2] = letters[i2]

    print(f"Welcome : {num_let}")
    sleep(5)
    os.system('cls')

    if letters[i1] == letters[i2]:
        if player_num == 1:
            score_1 += 1
        else:
            score_2 += 1

        numbers[i1] = '*'
        numbers[i2] = '*'
        count += 2


def get_valid_number(prompt):
    while True:
        num = int(input(prompt))
        if 1 <= num <= 20:
            return num
        else:
            print("Invalid number. Please choose another one.")

def determine_winner():
    if score_1 > score_2:
        print("Player 1 is the winner")
    elif score_2 > score_1:
        print("Player 2 is the winner")
    else:
        print("No winner")

while count != 20:
    player_turn(1)
    player_turn(2)
else:
    determine_winner()
