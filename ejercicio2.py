import random

contador_jugador = 0
contador_cpu = 0

manos = ["piedra", "papel", "tijera"]

while contador_jugador not in manos:
    jugador = input("Ingresa tu opción: (piedra, papel o tijera) o salir: ").lower()
    if jugador == "salir":
        break
    cpu = random.choice(manos)

    print(f"Jugador : {jugador}  vs CPU : {cpu}")

    if (jugador == "piedra" and cpu == "tijera") or(jugador == "tijera" and 
    cpu == "papel") or  (jugador == "papel" and cpu == "piedra"):
        print("Ganaste")
        contador_jugador +=1
    elif jugador == cpu:
        print("Empataron")
    else:
        print("Perdiste")
        contador_cpu +=1
    print(f"Marcador: jugador {contador_jugador} V/S cpu {contador_cpu}")
