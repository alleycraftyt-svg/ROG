import json
import os
import time
import random

# Nombre del archivo para guardar la partida en la computadora
SAVE_FILE = "partida_rog.json"

# --- FUNCIONES DE GUARDADO Y CARGA ---

def save_game(name, xp, money, lv, xp1, mana, potion):
    data = {
        "name": name, "xp": xp, "money": money, 
        "lv": lv, "xp1": xp1, "mana": mana, "potion": potion
    }
    with open(SAVE_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print("¡Partida guardada con éxito!")

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)
            print(f"\n¡Partida cargada! Bienvenido de nuevo, {data['name']}.")
            return (data["name"], data["xp"], data["money"], 
                    data["lv"], data["xp1"], data["mana"], data["potion"])
    else:
        print('¡¡¡Bienvenido a Realm Of Gorthia!!!')
        name = input('¿Cuál es tu nombre? ')
        print(f'¡Bienvenido, {name}!')
        return name, 0, 0, 1, 10, 10, 0

# --- INICIO DEL JUEGO ---

name, xp, money, lv, xp1, mana, potion = load_game()

print('\nEscribe "kill" para luchar contra monstruos, "xp" para ver tu estado, "store" para ir a la tienda y "src" para obtener el enlace del código fuente en GitHub.')
print('Usa "help" para ver comandos adicionales.')
print('--------------------------------------------------------')
print()
print(' Realm Of Gorthia (Demo 0.1.0) ')
print()
print('  POR: All3y_Sl4yer     ')
print()
print('--------------------------------------------------------')

gp = 20

while True:
    cmd = input('\n: ').strip().lower()
    yn = ""             
    store = ""

    # Comando: KILL
    if cmd == 'kill':
        if mana <= 0:
            print("¡No tienes suficiente maná para luchar! Usa una poción.")
        else:
            yn = input('Un slime se te acerca, ¿lo matas? (S/N): ').strip().lower()

    if yn == 's' or yn == 'y': 
        print(f'¡Ganaste {xp1} de xp y {gp} monedas de oro!')
        print(f'Te quedan {mana} de maná.')
        xp += xp1
        gp = random.randint(1, 40)
        money += gp
        mana -= 1

    if yn == 'n':
        print('Escapas del slime.')

    # Comando: STORE
    if cmd == 'store':
        print(f'Tu oro actual: {money}$')
        print('A: Espada lv 10 (100$)')
        print('B: Poción de maná (20$)')
        print('C: Poción de maná x10 (200$)')
        store = input('¿Qué vas a comprar? (A/B/C) o presiona ENTER para salir: ').strip().lower()

    if store == 'a':
        if money >= 100:
            print('¡Compraste la Espada! Ahora ganas más XP.')
            money -= 100
            xp1 = 20
        else:
            print("No tienes suficiente dinero.")

    if store == 'b':
        if money >= 20: 
            print('¡Compraste una poción de maná!')
            money -= 20
            potion += 1
        else:
            print("No tienes suficiente dinero.")

    if store == 'c':
        if money >= 200: 
            print('¡Compraste 10 pociones de maná!')
            money -= 200
            potion += 10
        else:
            print("No tienes suficiente dinero.")

    # Sistema automático de nivel
    if xp >= 100:
        lv += 1
        xp = 0  
        print(f'¡Felicidades! Subiste al nivel {lv}')

    # Comando: INV (Inventario)
    if cmd == 'inv':
        print(f'--- INVENTARIO ---')
        print(f'Pociones de maná: {potion}')
        print(f'Oro: {money}$')
        print(f'Te quedan {mana} de maná.')
        print('------------------')
        if potion > 0:
            use = input('Escribe "pot" para usar una poción o presiona ENTER para cerrar: ').strip().lower()
            if use == 'pot':
                cmd = 'pot'

    # Efecto de la poción
    if cmd == 'pot':
        if potion > 0:
            mana = 10
            potion -= 1
            print("¡Usaste una poción! Tu maná ha vuelto a 10.")
        else:
            print("No tienes pociones.")

    # Comando: PM (Ver Maná)
    if cmd == 'pm':
         print(f'Te quedan {mana} de maná.')

    # Comando: XP (Ver Experiencia)
    if cmd == 'xp':
         print(f'Nivel: {lv} | Tu XP actual es: {xp}/100')

    # Comando: SAVE
    if cmd == 'save':
        save_game(name, xp, money, lv, xp1, mana, potion)

    # Comando: RESTART
    if cmd == 'restart':
        confirm = input('¿Estás seguro de que deseas borrar todo tu progreso? (s/n): ').strip().lower()
        if confirm == 's' or confirm == 'y':
            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)
            print("¡Progreso eliminado de tu dispositivo!")
            name = input('¿Cuál es tu nombre esta vez? ')
            xp, money, lv, xp1, mana, potion = 0, 0, 1, 10, 10, 0
            save_game(name, xp, money, lv, xp1, mana, potion)
            print('¡Nueva partida iniciada!')

    # Comando: FRM (Farmear)
    if cmd == 'frm':
        if mana <= 0:
            print("¡No tienes suficiente maná para luchar! Usa una poción.")
        else:
            print(f'¡Encuentras un slime, lo matas y ganas {gp} monedas de oro y {xp1} de xp!')
            xp += xp1
            gp = random.randint(1, 25)
            money += gp
            mana -= 2

    # Comando: HELP 1
    if cmd == 'help':
        print('===========================================================================')
        print('1. inv: Abre el inventario para ver tus objetos y el oro disponible.')
        print('===========================================================================')
        print('2. pot: Usa una poción de tu inventario para restaurar maná (funciona también fuera del inv).')
        print('===========================================================================')
        print('3. frm: Se usa para subir de nivel más rápido, pero da menos oro y cuesta más maná.')
        print('===========================================================================')
        print('Escribe "help 2" para ver más comandos.')

    # Comando: HELP 2
    if cmd == 'help 2':
        print('===================================================================================')
        print('4. save: Guarda tu partida actual. ¡Los guardados se almacenan en formato .JSON para que puedas compartirlos!')
        print('===================================================================================')
        print('5. exit: Sale de la aplicación del juego (recuerda guardar tu progreso primero).')
        print('===================================================================================')
        print('6. restart: Borra tus archivos de guardado, útil si quieres empezar de nuevo desde cero.')
        print('===================================================================================')
        print('7. pm: Comprueba cuánto maná te queda mientras estás fuera del combate.')

    # Comando: SRC (Código fuente)
    if cmd == 'src':
        print('Con el código fuente, puedes crear mods o hacer lo que quieras :D')
        print('Enlace = https://github.com')

    # Comando: EXIT
    if cmd == 'exit':
        choice = input('¿Quieres guardar antes de salir? (s/n): ').strip().lower()
        if choice == 's' or choice == 'y':
            save_game(name, xp, money, lv, xp1, mana, potion)
        print('¡Gracias por jugar!')
        break
