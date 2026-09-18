# juegos-woki
----
juego de reflejos
----
Para realizar este juego primero tuve que aprender a utilizar Wokwi y la Raspberry Pi Pico. Al principio tuve algunas dificultades con las conexiones de los botones, porque no sabía exactamente qué patitas debía conectar a los pines y cuáles a GND. Después de revisar y corregir las conexiones, logré hacer que los botones funcionaran.
Luego hice el código en MicroPython, utilizando condicionales para detectar qué botón se estaba presionando. Después fui mejorando el juego para que no solo detectara los botones, sino que también escogiera uno al azar y me indicara cuál debía presionar.
Finalmente, agregué un sistema de puntos y tiempo, para que el juego mostrara si había presionado el botón correcto y cuánto había tardado. Aunque al principio tuve varios errores y me costó entender algunas conexiones, pude solucionarlos y terminar el juego funcionando en Wokwi.

----
papel, piedra o tijera
----
Para este juego utilicé tres botones conectados a la Raspberry Pi Pico. Cada botón representa una opción: piedra, papel o tijera. El jugador escoge una opción y la máquina selecciona otra de manera aleatoria. Después, el programa compara las dos elecciones mediante condicionales y determina quién ganó.

----
juegos de luces
----
Para realizar este juego utilicé Wokwi, una Raspberry Pi Pico, tres botones y tres LEDs. El juego consiste en observar una secuencia de luces y después repetirla presionando los botones en el mismo orden.
El programa está hecho en MicroPython y utiliza números aleatorios para crear las secuencias. Cada vez que se acierta, se pasa a un nuevo nivel y se agrega otra luz. Si se presiona un botón incorrecto, el juego termina y vuelve a comenzar.
Durante el desarrollo tuve que conectar los LEDs y hacer algunas pruebas para comprobar que todo funcionara correctamente. Con este juego pude practicar el uso de botones, LEDs, condicionales, ciclos y listas, además de aprender a relacionar el código con los componentes de la Raspberry Pi Pico.
