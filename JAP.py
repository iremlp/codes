from microbit import *
import random

p = 0
g = 0

# les images illustrant les issues d'un tirage
gagne = Image("99999:"
              "90009:"
              "90909:"
              "90009:"
              "99999:")

perd = Image("99999:"
             "90009:"
             "90009:"
             "90009:"
             "99999:")

plus0 = Image("00900:"
              "00900:"
              "99999:"
              "00900:"
              "00900:")

# les images composants l'animation
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
              
# la liste des images, permettant de donner leur ordre d'apparition
plus = [plus0, plus1, plus2, plus4, plus3, plus0]

temps = [100, 50, 50, 25]

# l'animation avant les tirages
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
            g = g + 1
        else:
            display.show(perd)
            p = p + 1
    # si on appuie sur le bouton "A",
    # l'appareil fait 25 tirages (1 LED allumée = gagné)
    if button_a.was_pressed():
        anim()
        for i in range(5):
            for j in range(5):
                if random.randint(1, 100) < 55:
                    display.set_pixel(i, j, 9)
                    g = g + 1
                else:
                    display.set_pixel(i, j, 0)
                    p = p + 1
    
    # si l'on appuie sur le bouton "B",
    # l'appareil affiche les résultats des tirages (G : gagné, P : perdu)
    if button_b.was_pressed():
        display.scroll("P: "+str(p)+" / G: "+str(g))

    # le 'tuple' de valeur (p,g) est envoyé vers l'ordinateur pour affichage
    # dans le graphique
    print((p, g))
    sleep(50)
