from Arbre import *
from Text import *

class Recit:
    """Permet de construire l'arbre du recit"""
    def __init__(self):
        """
                                 1
                     2                       3
              4            5           6           7
           8      9     10    11    12    13    14   15
        16   17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
     32   33
   34  35
        """
        n17 = Noeud(None, Text("Text 17", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n18 = Noeud(None, Text("Text 18", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n19 = Noeud(None, Text("Text 19", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n20 = Noeud(None, Text("Text 20", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n21 = Noeud(None, Text("Text 21", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n22 = Noeud(None, Text("Text 22", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n23 = Noeud(None, Text("Text 23", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n24 = Noeud(None, Text("Text 24", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n25 = Noeud(None, Text("Text 25", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n26 = Noeud(None, Text("Text 26", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n27 = Noeud(None, Text("Text 27", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n28 = Noeud(None, Text("Text 28", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n29 = Noeud(None, Text("Text 29", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n30 = Noeud(None, Text("Text 30", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n31 = Noeud(None, Text("Text 31", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n34 = Noeud(None, Text("Text 34", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n35 = Noeud(None, Text("Text 35", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n32 = Noeud(n34, Text("Text 32", "Quel choix voulez-vous faire ? (0 ou 1)"), n35)
        n33 = Noeud(None, Text("Text 33", "Quel choix voulez-vous faire ? (0 ou 1)"), None)
        n16 = Noeud(n32, Text("Text 16", "Quel choix voulez-vous faire ? (0 ou 1)"), n33)
        n15 = Noeud(n30, Text("Text 15", "Quel choix voulez-vous faire ? (0 ou 1)"), n31)
        n14 = Noeud(n28, Text("Text 14", "Quel choix voulez-vous faire ? (0 ou 1)"), n29)
        n13 = Noeud(n26, Text("Text 13", "Quel choix voulez-vous faire ? (0 ou 1)"), n27)
        n12 = Noeud(n24, Text("Text 12", "Quel choix voulez-vous faire ? (0 ou 1)"), n25)
        n11 = Noeud(n22, Text("Text 11", "Quel choix voulez-vous faire ? (0 ou 1)"), n23)
        n10 = Noeud(n20, Text("Text 10", "Quel choix voulez-vous faire ? (0 ou 1)"), n21)
        n9 = Noeud(n18, Text("Text 9", "Quel choix voulez-vous faire ? (0 ou 1)"), n19)
        n8 = Noeud(n16, Text("Text 8", "Quel choix voulez-vous faire ? (0 ou 1)"), n17)
        n7 = Noeud(n14, Text("Text 7", "Quel choix voulez-vous faire ? (0 ou 1)"), n15)
        n6 = Noeud(n12, Text("Text 6", "Quel choix voulez-vous faire ? (0 ou 1)"), n13)
        n5 = Noeud(n10, Text("Text 5", "Quel choix voulez-vous faire ? (0 ou 1)"), n11)
        n4 = Noeud(n8, Text("Text 4", "Quel choix voulez-vous faire ? (0 ou 1)"), n9)
        n3 = Noeud(n6, Text("Text 3", "Quel choix voulez-vous faire ? (0 ou 1)"), n7)
        n2 = Noeud(n4, Text("Text 2", "Quel choix voulez-vous faire ? (0 ou 1)"), n5)
        n1 = Noeud(n2, Text("Text 1", "Quel choix voulez-vous faire ? (0 ou 1)"), n3)

        self.arbre = n1
        self.current = n1

    def taille(self):
        return self.arbre.taille()

    def hauteur(self):
        return self.arbre.hauteur()
