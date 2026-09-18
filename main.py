from machine import Pin
import time
import random

boton1 = Pin(2, Pin.IN, Pin.PULL_UP)
boton2 = Pin(3, Pin.IN, Pin.PULL_UP)
boton3 = Pin(4, Pin.IN, Pin.PULL_UP)

led = Pin(25, Pin.OUT)

botones = [boton1, boton2, boton3]

puntos = 0

print("===== JUEGO DE REFLEJOS =====")
print("¡Preparado!")
time.sleep(2)

while True:

    # Elegir un botón al azar
    objetivo = random.randint(0, 2)

    print("")
    print("======================")
    print("PREPARATE...")
    time.sleep(2)

    print("¡PRESIONA EL BOTON", objetivo + 1, "!")
    print("======================")

    led.value(1)
    inicio = time.ticks_ms()

    # Esperar hasta que se presione algún botón
    while True:

        if boton1.value() == 0:
            presionado = 0
            break

        if boton2.value() == 0:
            presionado = 1
            break

        if boton3.value() == 0:
            presionado = 2
            break

        time.sleep_ms(10)

    tiempo = time.ticks_diff(time.ticks_ms(), inicio)
    led.value(0)

    # Comprobar si era el botón correcto
    if presionado == objetivo:

        puntos += 1

        print("")
        print("¡CORRECTO!")
        print("Tiempo:", tiempo, "ms")
        print("Puntos:", puntos)

    else:

        print("")
        print("¡INCORRECTO!")
        print("Debias presionar el boton", objetivo + 1)
        print("Presionaste el boton", presionado + 1)
        print("Puntos:", puntos)

    # Esperar a que suelten el botón
    while boton1.value() == 0 or boton2.value() == 0 or boton3.value() == 0:
        time.sleep_ms(20)

    time.sleep(2)