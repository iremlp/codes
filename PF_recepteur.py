from microbit import *
import radio
radio.on()
p = 0
g = 0

while True:
    incoming = radio.receive()

    if incoming == 'p':
        p += 1
    if incoming == 'g':
        g += 1
    # le 'tuple' de valeur (p,g) est envoyé vers l'ordinateur pour affichage
    # dans le graphique
    print((p, g))
    sleep(10)