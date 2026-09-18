from machine import Pin
import time
import random

boton1 = Pin(2, Pin.IN, Pin.PULL_UP)
boton2 = Pin(3, Pin.IN, Pin.PULL_UP)
boton3 = Pin(4, Pin.IN, Pin.PULL_UP)

led = Pin(25, Pin.OUT)

puntos_jugador = 0
puntos_maquina = 0

print("===== PIEDRA, PAPEL O TIJERA =====")
print("Boton 1 = Piedra")
print("Boton 2 = Papel")
print("Boton 3 = Tijera")
print("")

while True:

    print("======================")
    print("ELIGE UNA OPCION:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("======================")

    # Esperar una pulsacion
    while True:

        if boton1.value() == 0:
            jugador = 1
            break

        if boton2.value() == 0:
            jugador = 2
            break

        if boton3.value() == 0:
            jugador = 3
            break

        time.sleep_ms(20)

    # Eleccion de la maquina
    maquina = random.randint(1, 3)

    nombres = ["", "Piedra", "Papel", "Tijera"]

    print("Tu elegiste:", nombres[jugador])
    print("La maquina eligio:", nombres[maquina])

    # Comparar resultados
    if jugador == maquina:

        print("EMPATE")

    elif (jugador == 1 and maquina == 3) or \
         (jugador == 2 and maquina == 1) or \
         (jugador == 3 and maquina == 2):

        print("¡GANASTE!")
        puntos_jugador += 1
        led.value(1)
        time.sleep(0.5)
        led.value(0)

    else:

        print("GANO LA MAQUINA")
        puntos_maquina += 1

    print("Puntos tuyos:", puntos_jugador)
    print("Puntos de la maquina:", puntos_maquina)
    print("")

    # Esperar a soltar el boton
    while boton1.value() == 0 or boton2.value() == 0 or boton3.value() == 0:
        time.sleep_ms(20)

    time.sleep(2)