#!/usr/local/bin/python

import random
from enum import Enum
from math import gcd

class CellType(Enum):
    EGG = 1
    MUD = 2
    WRONG = 3

def separate():
    print('='*100 + '\n')

def print_matrix(matrix, curr, total):
    print(f"({curr}/{total})\n")
    for row in matrix:
        for i in row:
            if i.egg == CellType.EGG:
                if i.found:
                    print("🥚", end='')
                else:
                    print("🟫", end='')
            elif i.egg == CellType.MUD:
                print("🟫", end='')
            else:
                print("❌", end='')
        print()
    print()

class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.egg = CellType.MUD # no egg
        self.found = False

    def bury_egg(self):
        self.egg = CellType.EGG

    def dig(self) -> bool:
        if self.egg == CellType.EGG:
            if not self.found:
                print("You find an egg!\n")
                self.found = True
                return True
            else:
                print("You already hunted it!\n")
                return False
        else:
            print("No egg here. Try again!\n")
            self.egg = CellType.WRONG
            return False

def generate_matrix(m: int, n: int, egg: int):
    # generates a matrix of size mxn.
    # There will be eggs randomly generated
    matrix = [[Cell(x, y) for y in range(n)] for x in range(m)]
    all_eggs = []
    while len(all_eggs) < egg:
        row = random.randint(0, m-1)
        col = random.randint(0, n-1)
        if [row, col] in all_eggs:
            continue
        all_eggs.append([row, col])
        matrix[row][col].bury_egg()
    return matrix, all_eggs

LEVEL1 = True
LEVEL2 = False
LEVEL3 = False
LEVEL4 = False
LEVEL5 = False

FLAG = "vsctf{Congratulations!You_hunted_the_VS_eggs,please_enjoy_the_chocolate_flags---Yummy!}"


print('Welcome to the annual View Source Egg Hunt event. There are five levels in the game and you need to \
hunt all the eggs so I shall give you the flag.\n\nRemember: Happy hunting!\n')

while LEVEL1:
    separate()
    print('LEVEL1\n\nWe will start with a warmup. You are given a grid of 10 x 10 cells. An egg is buried under exactly one of the cells, and your goal is to find it! Here is what you can do:\n')
    print('(D)ig: You can dig a particular cell to see if there is an egg buried underneath :)')
    print('(S)ubmit: Submit the egg you have found and end the game. Be careful: you will fail the game if you don\'t finding the egg!')
    print('(Q)uit: Please don\'t quit this game ₍₍ ◝(●˙꒳˙●)◜ ₎₎')
    print("\nNote that submitting also counts as one attempt. As the warmup, I will offer you 42 chances to find the egg. Easy win, isn't it?\n")

    matrix, all_eggs = generate_matrix(10, 10, 1)
    # print(all_eggs)

    chances = 42
    hunted_eggs = 0
    while chances > 0:
        print_matrix(matrix, chances, 42)
        option = input("Your choice: ").strip().lower()
        if option == "d" or option == "dig":
            coord = input("Enter the row and column of the cell you want to dig (0-based index separated by space): ").strip().split()
            try:
                if matrix[int(coord[0])][int(coord[1])].dig():
                    hunted_eggs += 1
            except:
                print("Wrong format. Try again!\n")
        elif option == "s" or option == "submit":
            if hunted_eggs == 1:
                print("Nice, you passed Level 1, moving to Level 2...\n")
                LEVEL1 = False
                LEVEL2 = True
                break
            else:
                print("Don't submit if you didn't find any egg :(\n")
                exit(1)
        elif option == "q" or option == "quit":
            print("Sorry to see you go. See you next time!")
            exit(1)
        else:
            print("Oops, you just wasted a chance!\n")
        chances -= 1

    if chances == 0:
        print("Sorry but no more chances, unfortunately you failed the Egg Hunt. Try again next year!")
        exit(1)

while LEVEL2:
    separate()
    print('LEVEL2\n\nEgg hunt isn\'t always that easy. In this level I have prepared a total of 1,000 boxes where exactly one of the boxes contains an egg. The boxes are labelled from 1 to 1000. Here is what you can do:\n')
    print('(P)ick: You can pick a number between 1 and 1000 and I will open the box for you. If there\'s no egg inside I will kindly tell you if your pick is bigger or smaller than the box with egg :)')
    print('(Q)uit: I hope you don\'t quit this game ₍₍ ◝(●˙꒳˙●)◜ ₎₎')
    print("\nYou automatically win upon picking the box with egg. However, to make it more challenging, you only have 10 chances to hunt it. Moreover, I need to ensure you are not winning by pure luck, so we will play 20 rounds to prove you know the strategy. Let's give it a go!\n")

    success = 0
    while success < 20:
        egg_label = random.randint(1, 1000)
        # print(egg_label)
        guess = 10
        print(f"{success}/20\n")
        while guess > 0:
            option = input("Your choice: ").strip().lower()
            if option == "p" or option == "pick":
                coord = input("Please enter the box label (1-1000): ").strip()
                try:
                    coord = int(coord)
                    if coord < 1 or coord > 1000:
                        guess -= 1
                        print(f"Please pick between 1 and 1000. {guess}/10")
                    elif int(coord) == egg_label:
                        print("You found the egg.")
                        success += 1
                        break
                    elif int(coord) > egg_label:
                        guess -= 1
                        print(f"Your guess is too big. {guess}/10")
                    else:
                        guess -= 1
                        print(f"Your guess is too small. {guess}/10")
                except:
                    guess -= 1
                    print(f"Wrong format. Try again! {guess}/10")
            elif option == "q" or option == "quit":
                print("Sorry to see you go. See you next time!")
                exit(1)
            else:
                guess -= 1
                print(f"Wrong format. Try again! {guess}/10")
        if guess == 0:
            print("Sorry but no more chances, unfortunately you failed the Egg Hunt. Try again next year!")
            exit(1)
    
    # succeeded
    print("Nice, you passed Level 2, moving to Level 3...\n")
    LEVEL2 = False
    LEVEL3 = True
    
while LEVEL3:
    separate()
    print('LEVEL3\n\nSometimes you need to know some Maths to Egg hunt. In level 3, I have a secret number and if you can guess it in 25 tries I will give you the egg. The secret number is between 1 and 10^9 inclusive. Here is what you can do:\n')
    print('(P)ick: You can pick any two positive integers u, v. I will tell you gcd(u, secret+v) where gcd stands for greatest common divisor.')
    print('(Q)uit: I hope you don\'t quit this game ₍₍ ◝(●˙꒳˙●)◜ ₎₎')
    print("\nAt the end of 25 tries I will ask you for the secret number. Again, we will play 20 rounds to prove you know the strategy. Let's give it a go!\n")

    success = 0
    while success < 20:
        egg_label = random.randint(1, 1000000000)
        # print(egg_label)
        guess = 25
        print(f"{success}/20\n")
        while guess > 0:
            option = input("Your choice: ").strip().lower()
            if option == "p" or option == "pick":
                coord = input("Please enter u and v, separated by space: ").strip().split()
                try:
                    u, v = int(coord[0]), int(coord[1])
                    g = gcd(u, egg_label + v)
                    print(f"gcd({u}, secret + {v}) = {g}. {guess}/25")
                except:
                    print(f"Wrong format. Try again! {guess}/25")
            elif option == "q" or option == "quit":
                print("Sorry to see you go. See you next time!")
                exit(1)
            else:
                print(f"Wrong format. Try again! {guess}/25")
            guess -= 1
    
        user_guess = input("What is the secret: ").strip()
        try:
            if int(user_guess) == egg_label:
                print("Well done.")
                success += 1
            else:
                print("Unfortunately you failed the Egg Hunt. Try again next year!")
                exit(1)
        except:
            print("Unfortunately you failed the Egg Hunt. Try again next year!")
            exit(1)
    # succeeded
    print("Nice, you passed Level 3, moving to Level 4...\n")
    LEVEL3 = False
    LEVEL4 = True
    
while LEVEL4:
    separate()
    print('LEVEL4\n\nEgg Hunt on the grid strikes back. In this level, you are given a grid of 20 x 20 cells. TWO eggs are buried under different cells, and your task is to find them both! Here is what you can do:\n')
    print('(D)ig: You can dig a particular cell to see if there is an egg buried underneath :)')
    print('(P)ick: You can pick a cell (x, y). If eggs are in cells (a1, b1) and (a2, b2). I will tell you |x-a1|+|x-a2|+|y-b1|+|y-b2| where |a| is the absolute value of a.')
    print('(Q)uit: Please don\'t quit this game ₍₍ ◝(●˙꒳˙●)◜ ₎₎')
    print("\nYou automatically win upon digging all eggs. A bit challenging here: your total moves (including dig and pick) cannot exceed 8. We will only play 10 rounds because I think it's impossible to be so lucky. Good luck!\n")

    for i in range(1, 11):
        print(f"ROUND {i}\n")
        matrix, all_eggs = generate_matrix(20, 20, 2)
        # print(all_eggs)

        chances = 8
        hunted_eggs = 0
        while chances > 0:
            print_matrix(matrix, chances, 8)
            option = input("Your choice: ").strip().lower()
            if option == "d" or option == "dig":
                coord = input("Enter the row and column of the cell you want to dig (0-based index separated by space): ").strip().split()
                try:
                    if matrix[int(coord[0])][int(coord[1])].dig():
                        hunted_eggs += 1
                        if hunted_eggs == 2:
                            print("Nice, you found all eggs.\n")
                            break
                except:
                    print("Wrong format. Try again!\n")
            elif option == "p" or option == "pick":
                coord = input("Enter the row and column of the cell (0-based index separated by space): ").strip().split()
                try:
                    x, y = int(coord[0]), int(coord[1])
                    if x < 0 or y < 0 or x > 19 or y > 19:
                        print("Wrong format. Try again!\n")
                    else:
                        a1, b1 = all_eggs[0][0], all_eggs[0][1]
                        a2, b2 = all_eggs[1][0], all_eggs[1][1]
                        manhattan = abs(x - a1) + abs(x - a2) + abs(y - b1) + abs(y - b2)
                        print(f"Query result: {manhattan}")
                except:
                    print("Wrong format. Try again!\n")
            elif option == "q" or option == "quit":
                print("Sorry to see you go. See you next time!")
                exit(1)
            else:
                print("Oops, you just wasted a chance!\n")
            chances -= 1

        if chances == 0:
            print("Sorry but no more chances, unfortunately you failed the Egg Hunt. Try again next year!")
            exit(1)
    
    print("Nice, you passed Level 4, moving to Level 5...\n")
    LEVEL4 = False
    LEVEL5 = True

if LEVEL5:
    separate()
    print("LEVEL5\n\nCongratulations! You have cleared the Egg Hunt event from View Source. I hope you enjoyed the journey.")
    print(f"I would like to honor you the flag for reaching the final level. Well done!\n{FLAG}")
else:
    print("Unfortunately you failed the Egg Hunt. Try again next year!")
    exit(1)