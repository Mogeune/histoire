class Noeud:
    """Un noeud d'un arbre binaire"""
    def __init__(self,g,v,d):
        self.gauche=g
        self.valeur=v
        self.droit=d

    def __str__(self):
        if self is None:
            return ""
        if self.gauche is None and self.droit is None:
            return "("+self.valeur+")"
        if self.gauche is None:
            return "("+str(self.valeur)+str(self.droit)+")"
        if self.droit is None:
            return "("+str(self.gauche)+str(self.valeur)+")"
        return "("+str(self.gauche)+str(self.valeur)+str(self.droit)+")"

    def hauteur(self):
        if self is None:
            return 0
        if self.gauche is None and self.droit is None:
            return 1
        if self.gauche is None:
            return 1+self.droit.hauteur()
        if self.droit is None:
            return 1+self.gauche.hauteur()
        return 1+max(self.gauche.hauteur(),self.droit.hauteur())

    def taille(self):
        if self is None:
            return 0
        if self.gauche is None and self.droit is None:
            return 1
        if self.gauche is None:
            return 1+self.droit.taille()
        if self.droit is None:
            return 1+self.gauche.taille()
        return 1+self.gauche.taille()+self.droit.taille()

    def __eq__(self,other):
        if other!= None:
            return self.valeur==other.valeur and self.gauche==other.gauche and self.droit==other.droit

def appartient_a(v,a):
    if a is None:
        return False
    if v>a.valeur:
        return appartient_a(v,a.droit)
    if v<a.valeur:
        return appartient_a(v,a.gauche)
    return True

def ajout(v,a):
    if a is None:
        return Noeud(None, v, None)
    if v<=a.valeur:
        return Noeud(ajout(v.gauche, v), a.valeur, a.droit)
    if v>a.valeur:
        return Noeud(a.gauche, a.valeur, ajout(v, a.droit))


