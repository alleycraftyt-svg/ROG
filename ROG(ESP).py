import json
import os
import time
import random

# Nombre del archivo para guardar la partida en el ordenador
ARCHIVO_GUARDADO = "save_rog.json"

# --- FUNCIONES DE GUARDADO Y CARGA ---

def guardar_partida(nombre, xp, money, lv, xp1, mana, potion):
    datos = {
        "nombre": nombre, "xp": xp, "money": money, 
        "lv": lv, "xp1": xp1, "mana": mana, "potion": potion
    }
    with open(ARCHIVO_GUARDADO, "w") as archivo:
        json.dump(datos, archivo, indent=4)
    print("¡Partida guardada correctamente!")

def cargar_partida():
    if os.path.exists(ARCHIVO_GUARDADO):
        with open(ARCHIVO_GUARDADO, "r") as archivo:
            datos = json.load(archivo)
            print(f"\n¡Partida cargada! Bienvenido de nuevo, {datos['nombre']}.")
            return (datos["nombre"], datos["xp"], datos["money"], 
                    datos["lv"], datos["xp1"], datos["mana"], datos["potion"])
    else:
        print('Bienvenido a Realm Of Gorthia!!!')
        nombre = input('Como te llamas? ')
        print(f'¡Bienvenido, {nombre}!')
        return nombre, 0, 0, 1, 10, 10, 0

# --- INICIO DEL JUEGO ---

name, xp, money, lv, xp1, mana, potion = cargar_partida()

print('\nEscribe "kill" para matar mobs, "xp" para ver tu xp, "store" para la tienda y ¨src¨ para obtener el link de github del codigo fuente,')
print('usa help para ver los comandos adicionales.')
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

    # Comando: KILL
    if cmd == 'kill':
        if mana <= 0:
            print("¡No tienes suficiente mana para pelear! Usa una poción.")
        else:
            yn = input('Un slime se acerca a ti, ¿lo matas? (S/N): ').strip().lower()

    if yn == 's':
        print(f'¡Has ganado {xp1} de xp y {gp} de oro!')
        print(f'Te queda {mana} de mana.')
        xp += xp1
        gp = random.randint(1, 40)
        money += gp
        mana -= 1

    if yn == 'n':
        print('Escapas del slime.')

    # Comando: STORE (Tienda)
    if cmd == 'store':
        print(f'Tu oro actual: {money}$')
        print('A: Espada lv 10 (100$)')
        print('B: Pocion de mana (20$)')
        print('C: Pocion de mana x10 (200$)')
        store = input('¿Qué vas a comprar? (A/B) o ENTER para salir: ').strip().lower()

    if store == 'a':
        if money >= 100:
            print('¡Compraste la Espada! Ahora ganas más XP.')
            money -= 100
            xp1 = 20
        else:
            print("No tienes suficiente dinero.")

    if store == 'b':
        if money >= 5:
            print('¡Compraste una poción de mana!')
            money -= 20
            potion += 1
        else:
            print("No tienes suficiente dinero.")


    if store == 'c':
        if money >= 5:
            print('¡Compraste 10 pociones de mana!')
            money -= 200
            potion += 10
        else:
            print("No tienes suficiente dinero.")

    # Sistema de nivel automático
    if xp >= 100:
        lv += 1
        xp = 0  
        print(f'¡Felicidades! Has subido al nivel {lv}')

    # Comando: INV (Inventario)
    if cmd == 'inv':
        print(f'--- INVENTARIO ---')
        print(f'Pociones de mana: {potion}')
        print(f'Oro: {money}$')
        print(f'Te queda {mana} de mana.')
        print('------------------')
        if potion > 0:
            usar = input('Escribe "pot" para usar una poción o ENTER para cerrar: ').strip().lower()
            if usar == 'pot':
                cmd = 'pot'

    

    # Efecto de la poción
    if cmd == 'pot':
        if potion > 0:
            mana = 10
            potion -= 1
            print("¡Has usado una poción! Tu mana vuelve a 10.")
        else:
            print("No tienes pociones.")

    # Comando: PM (Mana)
    if cmd == 'pm':
         print(f'Te queda {mana} de mana.')

    # Comando: XP
    if cmd == 'xp':
         print(f'Nivel: {lv} | Tu XP actual es: {xp}/100')

    # Comando: GUARDAR
    if cmd == 'save':
        guardar_partida(name, xp, money, lv, xp1, mana, potion)

    # Comando: REINICIAR (Corregido directamente aquí en el bucle)
    if cmd == 'restart':
        confirmar = input('¿Seguro que quieres borrar todo tu progreso? (s/n): ').strip().lower()
        if confirmar == 's':
            if os.path.exists(ARCHIVO_GUARDADO):
                os.remove(ARCHIVO_GUARDADO)
            print("¡Progreso borrado de tu dispositivo!")
            name = input('Como te llamas de nuevo? ')
            xp, money, lv, xp1, mana, potion = 0, 0, 1, 10, 10, 0
            guardar_partida(name, xp, money, lv, xp1, mana, potion)
            print('¡Nueva partida iniciada!')

    if cmd == 'frm':
        print('encuentras un slime y lo matas y ganas {gp} y {xp1} de xp')
        xp += xp1
        gp = random.randint(1, 25)
        money += gp
        mana -= 2

    if cmd == 'help':
        print('===========================================================================')
        print('1. inv: abre el inventario para ver tus objetos y oro disponible')
        print('===========================================================================')
        print('2. pot: usa pociones en el inventario para regenerar mana tambien sirve fuera del inventario')
        print('===========================================================================')
        print('3. frm: sirve para subir de nivel rapido pero da menos oro y gasta mas mana')
        print('===========================================================================')
        print('escribe help 2 para mas ayuda')


    if cmd == 'help 2':
        print('===================================================================================')
        print('4. save: sirve para guardar partida, las partidas se guardan en .JSON puedes compartirlas si quieres!!')
        print('===================================================================================')
        print('5. exit: como su nombre lo dice sirve para salir y ya(el comando guarda tu partida usalo)')
        print('===================================================================================')
        print('6. restart: borra tus datos util si quieres volver a empezar')
        print('===================================================================================')
        print('7. pm: sirve para saber cuanto mana tienes, si no estas peleando')


    if cmd == 'src':
        print('con el codigo fuente puedes crear mods o hacer lo que quieras :D')
        print('Link = https://github.com/alleycraftyt-svg/ROG')

    # Comando: EXIT (Salir)
    if cmd == 'exit':
        opcion = input('¿Quieres guardar antes de salir? (s/n): ').strip().lower()
        if opcion == 's':
            guardar_partida(name, xp, money, lv, xp1, mana, potion)
        print('¡Gracias por jugar!')
        break

