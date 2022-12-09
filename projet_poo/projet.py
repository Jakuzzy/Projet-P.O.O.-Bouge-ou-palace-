import comptes_bancaires as cb
import random as rd
import blackjack as bj
import jeu_batonnets as jb



class Client:
    """Classe défini par :
            - son nom
            - son adresse
            - son compte bancaire
            - ses jetons de casino"""

    def __init__(self, nom:str, adresse:str, solde_compte:int):
        """Créer un nouveau Client()"""
        self.nom = nom
        self.adresse = adresse
        self.compte = cb.CompteBancaire('',solde_compte)
        self.jetons = 0

    def get_nom(self):
        """Obtenir le nom du client"""
        return self.nom

    def get_adresse(self):
        """Obtenir l'adresse du client"""
        return self.adresse

    def get_compte(self):
        """Obtenir le compte du client"""
        return self.compte

    def get_jetons(self):
        """Obtenir le nombre de jetons de casino du client"""
        return self.jetons



class Chambre :
    """Chaque instance de Chambre possède comme attributs :
    -	Un numéro
    -	Un étage
    -	Une capacité (de 1 à 3 personnes)
    -	Un état de propreté (ménage fait ou non)
    -	Un état d’occupation (libre ou non)
    -	Un tarif
    -	Une vue mer ou non"""

    def __init__(self, numero:int, etage:int, capacite:int, tarif:float, a_vue_mer:bool=False) :
        """Créer une nouvelle Chambre()"""
        self.numero = numero
        self.etage = etage
        self.capacite = max(min(capacite,3),1)
        self.est_propre = True
        self.est_occupee = False
        self.tarif = tarif
        self.a_vue_mer = a_vue_mer
        self.client = None

    def get_numero(self):
        """Renvoie le numéro de la chambre"""
        return self.numero

    def get_etage(self):
        """Renvoie l'étage de la chambre"""
        return self.etage

    def get_capacite(self):
        """Renvoie la capacité d'accueil de la chambre"""
        return self.capacite

    def get_est_propre(self):
        """Renvoie si la chambre est propre ou pas"""
        return self.est_propre

    def get_est_occupee(self):
        """Renvoie si la chambre est occupée ou pas"""
        return self.est_occupee

    def get_tarif(self):
        """Renvoie le tarif de la chambre"""
        return self.tarif

    def get_a_vue_mer(self):
        """Renvoie si la chambre a une vue sur la mer ou pas"""
        return self.a_vue_mer

    def get_client(self):
        """Renvoie le client de la chambre"""
        return self.client

    def nettoyer(self) :
        """Déclare la chambre propre"""
        self.est_propre = True
        return None

    def	prendre(self, client) :
        """Déclare la chambre occupée"""
        self.est_occupee = True
        self.client = client
        return None

    def	liberer(self) :
        """Déclare la chambre non-occupée"""
        self.est_occupee = False
        self.est_propre = False
        self.client = None
        return None



class Casino:
    """Classe défini par :
            - le fait qu'elle possède une table de blackjack
            - le fait qu'elle possède le "jeu des batonnets" """

    def __init__(self, a_blackjack:bool=False, a_jeu_batonnets:bool=False):
        """Créer un nouveau Client()"""
        self.a_blackjack = a_blackjack
        self.a_jeu_batonnets = a_jeu_batonnets

    def ajouter_jetons(self, client, nb:int):
        """Ajoute un nombre de jetons nb à client"""
        if nb >= 0:
            client.jetons += nb

    def retirer_jetons(self, client, nb:int):
        """Retire un nombre de jetons nb à client"""
        if nb >= 0:
            client.jetons -= nb

    def obtenir_jetons(self, client, nb:int):
        """Echange de l'argent contre des jetons"""
        if nb >= 0:
            client.compte.retirer(nb)
            self.ajouter_jetons(client, nb)

    def echange_jetons(self, client, nb:int):
        """Echange des jetons contre de l'argent"""
        if nb >= 0:
            self.retirer_jetons(client, nb)
            client.compte.verser(nb)

    def jouer_machine(self, client, mise:int=0):
        """Permet de jouer à une machine à sous, si vous avez 2 chiffres identiques vous remportez 2 fois la mise, si vous en avez 3, vous remportez 10 fois la mise, sinon vous ne remportez rien"""
        if mise >= 0 and mise <= client.jetons:
            elt_1, elt_2, elt_3 = rd.randint(1,9), rd.randint(1,9), rd.randint(1,9)
            print("Résultat :")
            print("╔═════╦═════╦═════╗")
            print("║  "+str(elt_1)+"  ║  "+str(elt_2)+"  ║  "+str(elt_3)+"  ║")
            print("╚═════╩═════╩═════╝")
            if elt_1 == elt_2 == elt_3:
                print("Félicitations, vous gagnez 10 fois votre mise !")
                self.ajouter_jetons(client, 10*mise)
            elif elt_1 == elt_2 or elt_2 == elt_3 or elt_3 == elt_1:
                print("Vous gagnez 2 fois votre mise !")
                self.ajouter_jetons(client, 2*mise)
            else:
                print("Vous avez perdu.")
                self.retirer_jetons(client, mise)
        else:
            print("Votre mise n'est pas valable.")

    def jouer_blackjack(self, client, mise:int=0):
        """Permet de jouer au blackjack si le casino possède une table de blackjack"""
        if self.a_blackjack:
            if mise >= 0 and mise <= client.jetons:
                jetons_perdu, jetons_gagne = bj.blackjack(mise)
                ajouter_jetons(self, client, jetons_gagne)
                retirer_jetons(self, client, jetons_perdu)
            else:
                print("Votre mise n'est pas valable.")
        else:
            print("Ce casino ne possède pas de table de blackjack.")

    def jouer_batonnets(self):
        """Permet de jouer au "jeu des batonnets" si le casino le possède"""
        jb.JeuBatonnets()



class Hotel :
    """Chaque instance de Hotel possède comme attributs :
    -	Un nom
    -	Une ville
    -	Une adresse
    -	Des chambres
    -	Une piscine ou non
    -	Un casino ou non"""

    def __init__(self, nom:str, ville:str, adresse:str, chambres:list, solde_compte:int=0, a_piscine:bool=False, casino=False):
        """Créé un nouvel Hotel()"""
        self.nom = nom
        self.ville = ville
        self.adresse = adresse
        self.chambres = chambres
        self.compte = cb.CompteBancaire('',solde_compte)
        self.a_piscine = a_piscine
        self.casino = casino

    def get_nom(self):
        """Renvoie le nom de l'hôtel"""
        return self.nom

    def get_ville(self):
        """Renvoie la ville de l'hôtel"""
        return self.ville

    def get_adresse(self):
        """Renvoie l'adresse de l'hôtel"""
        return self.adresse

    def get_chambres(self):
        """Renvoie la liste de chambres de l'hôtel"""
        return self.chambres

    def get_compte(self):
        """Renvoie le compte bancaire de l'hôtel"""
        return self.compte

    def get_a_piscine(self):
        """Renvoie si l'hôtel a une piscine ou pas"""
        return self.a_piscine

    def get_chambre(self, numero:int, etage:int):
        """Renvoie la chambre correspondant au numéro et à l'étage donnés"""
        for chambre in self.chambres:
            if chambre.numero == numero and chambre.etage == etage:
                return chambre
        return False

    def get_dispo(self):
        """Renvoie le nombre de chambres disponibles"""
        chambres_non_occupee = 0
        for chambre in self.chambres:
            if not chambre.get_est_occupee():
                chambres_non_occupee +=1
        return chambres_non_occupee

    def add_chambres(self, chambres:list):
        """Ajoute chambres à la liste de chambres de l'hôtel"""
        self.chambres += chambres

    def nb_chambres(self):
        """Renvoie le nombre de chambres de l'hotel"""
        return len(self.chambres)

    def	nettoyer_chambres(self) :
        """Fait le ménage dans toutes les chambres de l'hôtel"""
        for chambre in self.chambres:
            chambre.nettoyer()
        return None

    def	payer(self, numero:int, etage:int):
        """Paie la chambre correspondant à l'étage et au numéro donnés avec compte"""
        chambre = self.get_chambre(numero,etage)
        if chambre and chambre.client != None:
            client = chambre.client
            client.compte.transferer(self.compte,chambre.tarif)
        return None



def test_hotel(): #incomplet et marche pas forcément pour tout
    liste_chambres = []
    for etage in range(3):
        for numero in range(10):
            liste_chambres.append(Chambre(numero,etage,2,78.50,False))

    mon_casino = Casino(True)

    mon_hotel = Hotel('Hotel California','Vesoul','40 rue du Général',liste_chambres,150000,True,mon_casino)

    client_test = Client('Allan','Saint-Rogatien',7500)

    for _ in range(10):
        chambre = rd.choice(mon_hotel.chambres)
        chambre.prendre(client_test)
    print("Nombre de chambres d'hotel :",mon_hotel.nb_chambres())
    print('Chambres disponibles :',mon_hotel.get_dispo())

    mon_compte = cb.CompteBancaire('1234',7500)
    print("Solde hotel avant paiement d'une chambre :",mon_hotel.get_compte().get_solde())

    mon_hotel.payer(7,2)
    print("Solde hotel après paiement d'une chambre :",mon_hotel.get_compte().get_solde())

    nouv_liste_chambres = []
    for numero in range(5):
        nouv_liste_chambres.append(Chambre(numero,3,1,62,False))
    mon_hotel.add_chambres(nouv_liste_chambres)
    print("Nombre de chambres d'hotel après ajout de 5 :",mon_hotel.nb_chambres())

    mon_casino.obtenir_jetons(client_test,100)
    print("Nombre de jetons avant partie de blackjack :",client_test.get_jetons())
    mon_casino.jouer_blackjack(client_test,10)
    print("Nombre de jetons après blackjack :",client_test.get_jetons())

##test_hotel()