from microbit import *
import random
import radio

# on créé les images illustrant les issues d'un tiragegagne = Image("99999:"
              "90009:"
              "90909:"
              "90009:"
              "99999:")

perd = Image("99999:"
             "90009:"
             "90009:"
             "90009:"
             "99999:")
# on créé les images composant l'animation
plus0 = Image("00900:"
              "00900:"
              "99999:"
              "00900:"
              "00900:")

plus1 = Image("09000:"
              "09000:"
              "99999:"
              "09000:"
              "09000:")

plus2 = Image("90000:"
              "90000:"
              "99999:"
              "90000:"
              "90000:")

plus3 = Image("00090:"
              "00090:"
              "99999:"
              "00090:"
              "00090:")

plus4 = Image("00009:"
              "00009:"
              "99999:"
              "00009:"
              "00009:")
              
# on allume la radio
radio.on()

# on initialise les variables
p = 0
g = 0

# on crée la liste des images, permettant de donner leur ordre d'apparition
plus = [plus0, plus1, plus2, plus4, plus3, plus0]

temps = [100, 50, 50, 25]

# on définie l'animation avant les tirages
def anim():
    for t in temps:
        display.show(plus, delay=t)
    display.clear()


while True:
    # si on secoue l'appareil, il fait un tirage
    if accelerometer.was_gesture("shake"):
        anim()
        if random.randint(1, 100) < 55:
            display.show(gagne)
            g += 1
            radio.send('g')
        else:
            display.show(perd)
            p += 1
            radio.send('p')
    # si on appuie sur le bouton "A",
    # l'appareil fait 25 tirages (1 LED allumée = gagné)
    if button_a.was_pressed():
        anim()
        for i in range(5):
            for j in range(5):
                if random.randint(1, 100) < 55:
                    display.set_pixel(i, j, 9)
                    g += 1
                    radio.send('g')
                    sleep(10)
                else:
                    display.set_pixel(i, j, 0)
                    p += 1
                    radio.send('p')
                    sleep(10)
    
    # si l'on appuie sur le bouton "B",
    # l'appareil affiche les résultats des tirages (G : gagné, P : perdu)
    if button_b.was_pressed():
        display.scroll("P: "+str(p)+" / G: "+str(g))
