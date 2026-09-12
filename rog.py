# Hi
import json
import os
import time
import random

# File name to save the game on the computer
SAVE_FILE = "save_rog.json"

# --- SAVE AND LOAD FUNCTIONS ---

def save_game(name, xp, money, lv, xp1, mana, potion, mxp):
    data = {
        "name": name, "xp": xp, "money": money, 
        "lv": lv, "xp1": xp1, "mana": mana, "potion": potion, "mxp": mxp
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
                    data["lv"], data["xp1"], data["mana"], data["potion"], data.get("mxp", 100))
    else:
        print('Welcome to Realm Of Gorthia!!!')
        name = input('What is your name? ')
        print(f'Welcome, {name}!')
        return name, 0, 0, 1, 50, 20, 1, 100

# --- GAME START ---

name, xp, money, lv, xp1, mana, potion, mxp = load_game()

print('\nType "kill" to fight mobs, "xp" to see your status, "store" for the shop, and "src" to get the GitHub source code link.')
print('Use "help" to see additional commands.')
print('--------------------------------------------------------')
print()
print(' Realm Of Gorthia (Beta 0.2.0) Open Source!! ')
print()
print('  BY: All3y_Sl4yer     ')
print()
print('--------------------------------------------------------')

print('save your game before you exit using "save" command...')

mob = 'slime'
gp = 20
xpg = 20

print('use "zone" to change the zone')
while True:
    cmd = input('\n: ').strip().lower()

    # Command: KILL
    if cmd == 'kill':
        if mana <= 0:
            print("You don't have enough mana to fight! Use a potion.")
        else:
            yn = input(f'A {mob} approaches you, do you kill it? (Y/N): ').strip().lower()
            if yn in ['y', 's']: # Supports both 'y' for English and 's' for Spanish speakers
                time.sleep(0.2)
                gp = random.randint(1, 35)
                print(f'You won {xpg} of xp and {gp} of gold!')
                xp += xpg
                money += gp
                mana -= 1
                print(f'You have {mana} mana left.')
            elif yn == 'n':
                print(f'You escape from the {mob}.')

    # Command: STORE
    elif cmd == 'store':
        print(f'Your current gold: {money} GP')
        print('A: Mana potion      (20 GP)')
        print('B: Mana potion x10  (200 GP)')
        print('C: Chocolate Cake   (10 GP)')
        store = input('What are you going to buy? (A/B/C) or press ENTER to exit: ').strip().lower()

        if store == 'a':
            if money >= 20: 
                print('You bought a mana potion!')
                money -= 20
                potion += 1
            else:
                print("You don't have enough money.")

        elif store == 'b':
            if money >= 200: 
                print('You bought 10 mana potions!')
                money -= 200
                potion += 10
            else:
                print("You don't have enough money.")

        elif store == 'c':
            if money >= 10: 
                print('You bought a cake and you eat them,(hmmmm chocolate) +5 mana!')
                money -= 10
                mana += 5
            else:
                print("You don't have enough money.")

    # Command: INV (Inventory)
    elif cmd == 'inv':
        print(f'--- INVENTORY ---')
        print(f'Mana potions: {potion}')
        print(f'Gold: {money} GP')
        print(f'You have {mana} mana left.')
        print('------------------')
        if potion > 0:
            use = input('Type "pot" to use a potion or press ENTER to close: ').strip().lower()
            if use == 'pot':
                cmd = 'pot'

    # Potion effect (Se ejecuta si se teclea 'pot' o desde el inv)
    if cmd == 'pot':
        if potion > 0:
            mana = 10
            potion -= 1
            print("You used a potion! Your mana is back to 10.")
        else:
            print("You don't have any potions.")

    # Command: PM (Mana)
    elif cmd == 'pm':
         print(f'You have {mana} mana left.')

    # Command: XP
    elif cmd == 'xp':
         print(f'Level: {lv} | Your current XP is: {xp}/{mxp}')

    # Command: SAVE
    elif cmd == 'save':
        save_game(name, xp, money, lv, xp1, mana, potion, mxp)

    # Command: RESTART
    elif cmd == 'restart':
        confirm = input('Are you sure you want to wipe all your progress? (y/n): ').strip().lower()
        if confirm in ['y', 's']:
            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)
            print("Progress deleted from your device!")
            name = input('What is your name this time? ')
            xp, money, lv, xp1, mana, potion, mxp = 0, 0, 1, 50, 20, 1, 100
            save_game(name, xp, money, lv, xp1, mana, potion, mxp)
            print('New game started!')

    # Command: PT (Power Train)
    elif cmd == 'pt':
        if mana <= 0:
            print("You don't have enough mana to fight! Use a potion.")
        else:
            print(f'You find a {mob} and you kill it +{xpg} xp!')
            xp += xpg
            mana -= 1

    # Command ZONE
    elif cmd == 'zone':
        print('1. Ghoul Dungeon    (lv: 10)')
        print('2. Elf Village      (lv: 25)')
        print('3. Zombie lair      (lv: 35)')
        print('4. Skeleton Dungeon (lv: 65)')
        print('5. Goblins Cave     (lv: 75)')
        print('6. Drows Village    (lv: 125)')
        print('7. Dragons Lair     (lv: 165)')
        print('8. Werewolfs Cave   (lv: 200)')
        z = input('what zone do you choose?: ').strip()
        
        if z == '1':
            if lv >= 10:
                mob, xpg = 'ghoul', 30
            else:
                print('you dont have the required level')
        elif z == '2':
            if lv >= 25:
                mob, xpg = 'elf', 45
            else:
                print('you dont have the required level')
        elif z == '3':
           if lv >= 35:
               mob, xpg = 'zombie', 60
           else:
               print('you dont have the required level')
        elif z == '4':
           if lv >= 65:
               mob, xpg = 'skeleton', 70
           else:
               print('you dont have the required level')
        elif z == '5':
           if lv >= 75:
               mob, xpg = 'goblin', 80
           else:
               print('you dont have the required level')
        elif z == '6':
           if lv >= 125:
              mob, xpg = 'Drow', 100
           else:
               print('you dont have the required level')
        elif z == '7':
           if lv >= 165:
              mob, xpg = 'dragon', 135
           else:
               print('you dont have the required level')
        elif z == '8':
           if lv >= 200:
              mob, xpg = 'werewolf', 150
           else:
               print('you dont have the required level')

    # SETLV: Dev command out of zone block
    elif cmd == 'setlv':
        ps = input('what is the password? ')
        if ps == 'DGLV1512':
            dev = input('what level do you want? ')
            try:
                lv = int(dev)
                print(f"Level set to {lv}!")
            except ValueError:
                print("Invalid level number.")


    elif cmd == 'src':
        print('here is the source code you can do whatever do you want! :D')
        print('        https://github.com/alleycraftyt-svg/ROG')
    # Command: HELP
    elif cmd == 'help':
        print('=====================================================================')
        print('1. inv: Opens the inventory to see your items and available gold.')
        print('=====================================================================')
        print('2. pot: Uses a potion from your inventory to restore mana.')
        print('=====================================================================')
        print('3. pt: Used to level up faster, costs more mana and you cant get gold.')
        print('=====================================================================')

    # Automatic level system
    if xp >= mxp:
        lv += 1
        xp = xp - mxp # Keeps remaining XP
        print(f'Congratulations! You leveled up to level {lv}')
        if lv >= 100:
            mxp = 5000

