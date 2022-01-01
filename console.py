from Recit import *

def histoire_rec():
    if (recit.current != None):
        print(recit.current.valeur)
        choice = input()
        if (choice == "0"):
            recit.current = recit.current.gauche
        elif (choice == "1"):
            recit.current = recit.current.droit
        histoire_rec()
    else:
        print("-- Fin --")

def histoire_iter():
    while (recit.current != None):
        print(recit.current.valeur)
        choice = input()
        if (choice == "0"):
            recit.current = recit.current.gauche
        elif (choice == "1"):
            recit.current = recit.current.droit
    print("-- Fin --")
    return

def taille():
    return recit.taille()

def hauteur():
    return recit.hauteur()

recit=Recit()

assert taille() >= 35, "la taille du récit doit être de 35 minimum (actuel:"+str(recit.taille())+")"
assert hauteur() >= 7, "la hauteur du récit doit être de 7 minimum (actuel:"+str(recit.hauteur())+")"

histoire_rec()