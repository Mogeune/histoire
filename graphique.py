from tkinter import *
from tkinter import ttk
from Recit import *
from functools import partial

class InterfaceGraphique:

    def __init__(self):
        self.recit=None
        self.bouton0=None
        self.bouton1=None
        self.text=None
        self.root=None
        self.frm=None
        self.quitter=None

    def recommencer(self):
        self.recit=Recit()
        self.text.set(self.recit.current.valeur)
        if (self.bouton0 == None):
            self.bouton0=ttk.Button(self.frm, text="0", command=partial(self.choisi_option, 0))
            self.bouton0.grid(column=0, row=1)
            self.bouton1=ttk.Button(self.frm, text="1", command=partial(self.choisi_option, 1))
            self.bouton1.grid(column=1, row=1)
        
        if (self.quitter != None):
            self.quitter.grid_forget()
            self.quitter = None

        self.text.set(self.recit.current.valeur)


    def choisi_option(self, choix):
        textStr = "-- FIN -- "
        if (choix == 0):
            self.recit.current = self.recit.current.gauche
        elif (choix == 1):
            self.recit.current = self.recit.current.droit

        if (self.recit.current is not None):
            textStr = self.recit.current.valeur
        else:
            self.bouton0.grid_forget()
            self.bouton0 = None
            self.bouton1.grid_forget()
            self.bouton1 = None
            self.quitter=ttk.Button(self.frm, text="Quitter", command=self.root.destroy)
            self.quitter.grid(column=0, row=3)

        self.text.set(textStr)

    def afficher(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        can1 = Canvas(self.root, width = 500, height = 500, bg = 'white')
        background_image=PhotoImage(file = "image.jpg")
        item = can1.create_image(300, 300, image = background_image)
        can1.grid()

        self.text=StringVar()

        ttk.Label(self.frm, textvariable=self.text).grid(column=0, row=0)

        self.recommencer()

        bouttonRecommencer=ttk.Button(self.frm, text="Recommencer", command=self.recommencer)
        bouttonRecommencer.grid(column=0, row=2)

        self.root.mainloop()

InterfaceGraphique().afficher()