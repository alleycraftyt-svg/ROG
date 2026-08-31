import json
import os
import time
import random

# File name to save the game on the computer
SAVE_FILE = "save_rog.json"

# --- SAVE AND LOAD FUNCTIONS ---

def save_game(name, xp, money, lv, xp1, mana, potion):
    data = {
        "name": name, "xp": xp, "money": money, 
        "lv": lv, "xp1": xp1, "mana": mana, "potion": potion
    }
    with open(SAVE_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print("Game saved successfully!")

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)
            print(f"\nGame loaded! Welcome back, {data['name']}.")
            return (data["name"], data["xp"], data["money"], 
                    data["lv"], data["xp1"], data["mana"], data["potion"])
    else:
        print('Welcome to Realm Of Gorthia!!!')
        name = input('What is your name? ')
        print(f'Welcome, {name}!')
        return name, 0, 0, 1, 10, 10, 0

# --- GAME START ---

name, xp, money, lv, xp1, mana, potion = load_game()

print('\nType "kill" to fight mobs, "xp" to see your status, "store" for the shop, and "src" to get the GitHub source code link.')
print('Use "help" to see additional commands.')
print('--------------------------------------------------------')
print()
print(' Realm Of Gorthia (Demo 0.1.0) ')
print()
print('  BY: All3y_Sl4yer     ')
print()
print('--------------------------------------------------------')

gp = 20

while True:
    cmd = input('\n: ').strip().lower()
    yn = ""             
    store = ""

    # Command: KILL
    if cmd == 'kill':
        if mana <= 0:
            print("You don't have enough mana to fight! Use a potion.")
        else:
            yn = input('A slime approaches you, do you kill it? (Y/N): ').strip().lower()

    if yn == 'y' or yn == 's': # Supports both 'y' for English and 's' for Spanish speakers
        print(f'You won {xp1} xp and {gp} gold!')
        print(f'You have {mana} mana left.')
        xp += xp1
        gp = random.randint(1, 40)
        money += gp
        mana -= 1

    if yn == 'n':
        print('You escape from the slime.')

    # Command: STORE
    if cmd == 'store':
        print(f'Your current gold: {money}$')
        print('A: Sword lv 10 (100$)')
        print('B: Mana potion (20$)')
        print('C: Mana potion x10 (200$)')
        store = input('What are you going to buy? (A/B/C) or press ENTER to exit: ').strip().lower()

    if store == 'a':
        if money >= 100:
            print('You bought the Sword! Now you gain more XP.')
            money -= 100
            xp1 = 20
        else:
            print("You don't have enough money.")

    if store == 'b':
        if money >= 20: # Fixed to match the store price listed above (20$)
            print('You bought a mana potion!')
            money -= 20
            potion += 1
        else:
            print("You don't have enough money.")

    if store == 'c':
        if money >= 200: # Fixed to match the store price listed above (200$)
            print('You bought 10 mana potions!')
            money -= 200
            potion += 10
        else:
            print("You don't have enough money.")

    # Automatic level system
    if xp >= 100:
        lv += 1
        xp = 0  
        print(f'Congratulations! You leveled up to level {lv}')

    # Command: INV (Inventory)
    if cmd == 'inv':
        print(f'--- INVENTORY ---')
        print(f'Mana potions: {potion}')
        print(f'Gold: {money}$')
        print(f'You have {mana} mana left.')
        print('------------------')
        if potion > 0:
            use = input('Type "pot" to use a potion or press ENTER to close: ').strip().lower()
            if use == 'pot':
                cmd = 'pot'

    # Potion effect
    if cmd == 'pot':
        if potion > 0:
            mana = 10
            potion -= 1
            print("You used a potion! Your mana is back to 10.")
        else:
            print("You don't have any potions.")

    # Command: PM (Mana)
    if cmd == 'pm':
         print(f'You have {mana} mana left.')

    # Command: XP
    if cmd == 'xp':
         print(f'Level: {lv} | Your current XP is: {xp}/100')

    # Command: SAVE
    if cmd == 'save':
        save_game(name, xp, money, lv, xp1, mana, potion)

    # Command: RESTART
    if cmd == 'restart':
        confirm = input('Are you sure you want to wipe all your progress? (y/n): ').strip().lower()
        if confirm == 'y' or confirm == 's':
            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)
            print("Progress deleted from your device!")
            name = input('What is your name this time? ')
            xp, money, lv, xp1, mana, potion = 0, 0, 1, 10, 10, 0
            save_game(name, xp, money, lv, xp1, mana, potion)
            print('New game started!')

    # Command: FRM (Farm)
    if cmd == 'frm':
        print(f'You find a slime, kill it, and earn {gp} gold and {xp1} xp!')
        xp += xp1
        gp = random.randint(1, 25)
        money += gp
        mana -= 2

    # Command: HELP 1
    if cmd == 'help':
        print('===========================================================================')
        print('1. inv: Opens the inventory to see your items and available gold.')
        print('===========================================================================')
        print('2. pot: Uses a potion from your inventory to restore mana (works outside inv too).')
        print('===========================================================================')
        print('3. frm: Used to level up faster, but gives less gold and costs more mana.')
        print('===========================================================================')
        print('Type "help 2" for more commands.')

    # Command: HELP 2
    if cmd == 'help 2':
        print('===================================================================================')
        print('4. save: Saves your current game. Saves are stored in .JSON format so you can share them!')
        print('===================================================================================')
        print('5. exit: Exits the game application (remember to save your progress first).')
        print('===================================================================================')
        print('6. restart: Wipes your save files, useful if you want to start over from scratch.')
        print('===================================================================================')
        print('7. pm: Checks how much mana you have left while outside of combat.')

    # Command: SRC (Source Code)
    if cmd == 'src':
        print('With the source code, you can create mods or do whatever you want :D')
        print('Link = https://github.com/alleycraftyt-svg/ROG')

    # Command: EXIT
    if cmd == 'exit':
        choice = input('Do you want to save before exiting? (y/n): ').strip().lower()
        if choice == 'y' or choice == 's':
            save_game(name, xp, money, lv, xp1, mana, potion)
        print('Thanks for playing!')
        break


