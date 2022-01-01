from Recit2 import *
from Arbre import *

def histoire_iter():
    while recit.v_courrent is not None:
        print(recit.v_courrent.valeur)
        resultat = input("")
        if resultat == "0":
            recit.v_courrent = recit.v_courrent.gauche
        elif resultat == "1":
            recit.v_courrent = recit.v_courrent.droit
    print("Fin")
    return

recit=Recit()
histoire_iter()

def taille():
    return recit.taille()

def hauteur():
    return recit.hauteur()

assert taille() >= 35, "la taille du récit doit être de 35 minimum (actuel:"+str(recit.taille())+")"
assert hauteur() >= 7, "la hauteur du récit doit être de 7 minimum (actuel:"+str(recit.hauteur())+")"
