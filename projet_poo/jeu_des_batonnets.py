import random

class Jeu_des_Batonnets:
    def __init__(self):
        self.baton = 21
        self.last = None
        print("| "*self.baton,"("+str(self.baton)+") bâtonnets restant(s) (VOUS COMMENCEZ)")
        self.joueur()

    def joueur(self):
        nb = int(input("Enlever baton"))
        if nb > 3:
            self.baton -= 3
        elif nb < 1:
            self.baton -= 1
        else:
            self.baton -= nb
        self.last = "Joueur"

        if self.baton <= 0:
            print(self.last,"A PERDU !")
            exit()
        else:
            print("| "*self.baton,"("+str(self.baton)+") bâtonnets restant(s) (JOUEUR)")
            self.maitre()

    def maitre(self):
        self.last = "Maitre"

        if self.baton > 17:
            nb = self.baton-17
            if nb > 3:
                self.baton -= 3
            else:
                self.baton -= nb
        elif self.baton > 13:
            nb = self.baton-13
            if nb > 3:
                self.baton -= 3
            else:
                self.baton -= nb
        elif self.baton > 9:
            nb = self.baton-9
            if nb > 3:
                self.baton -= 3
            else:
                self.baton -= nb
        elif self.baton > 5:
            nb = self.baton-5
            if nb > 3:
                self.baton -= 3
            else:
                self.baton -= nb
        elif self.baton > 1:
            nb = self.baton-1
            if nb > 3:
                self.baton -= 3
            else:
                self.baton -= nb

        if self.baton <= 0:
            print(self.last,"A PERDU !")
            exit() ##fermer le jeu
        else:
            print("| "*self.baton,"("+str(self.baton)+") bâtonnets restant(s) (MAITRE)")
            self.joueur()

Jeu_des_Batonnets()
