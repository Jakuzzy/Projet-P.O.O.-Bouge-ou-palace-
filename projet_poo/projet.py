import comptes_bancaires as cb
import random as r
import blackjack as b

class Chambre :
    """
    Chaque instance de Chambre possède comme attributs :
    -	Un numéro
    -	Un étage
    -	Une capacité (de 1 à 3 personnes)
    -	Un état de propreté (ménage fait ou non)
    -	Un état d’occupation (libre ou non)
    -	Un tarif
    -	Une vue mer ou non

    La classe Chambre est pourvue des méthodes suivantes :
    -	nettoyer()
    -	prendre()
    -	liberer()
    -	payer()
    -	Des méthodes permettant d’accéder à chacun des attributs.
    """
    def __init__(self, numero:int, etage:int, capacite:int, tarif:float, a_vue_mer:bool=False) :
        """Créer une nouvelle Chambre()"""
        self.numero = numero
        self.etage = etage
        self.capacite = max(min(capacite,3),1)
        self.est_propre = True
        self.est_occupee = False
        self.tarif = tarif
        self.a_vue_mer = a_vue_mer

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

    def nettoyer(self) :
        """Déclare la chambre propre"""
        self.est_propre = True
        return None

    def	prendre(self) :
        """Déclare la chambre occupée"""
        self.est_occupee = True
        return None

    def	liberer(self) :
        """Déclare la chambre non-occupée"""
        self.est_occupee = False
        self.est_propre = False
        return None



class Hotel :
    """
    Chaque instance de Hotel possède comme attributs :
    -	Un nom
    -	Une ville
    -	Une adresse
    -	Des chambres
    -	Une piscine ou non
    -	Un casino ou non

    La classe est pourvue des méthodes suivantes :
    -	get_dispo() qui renvoie le nombre de chambres disponibles.
    -	nettoyer() qui fait le ménage dans toutes les chambres de cet hôtel.
    -	Des méthodes permettant d’accéder à chacun des attributs.
    """

    def __init__(self, nom:str, ville:str, adresse:str, chambres:list, solde_compte_hotel:int=0, a_piscine:bool=False, a_casino:bool=False):
        """Créé un nouvel Hotel()"""
        self.nom = nom
        self.ville = ville
        self.adresse = adresse
        self.chambres = chambres
        self.compte = cb.CompteBancaire('42',solde_compte_hotel)
        self.a_piscine = a_piscine
        self.a_casino = a_casino

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

    def	payer(self, numero:int, etage:int, compte):
        """Paie la chambre correspondant à l'étage et au numéro donnés avec compte"""
        chambre = self.get_chambre(numero,etage)
        if chambre:
            compte.transferer(self.compte,chambre.tarif)
        return None

    def jouer_blackjack(self, compte, mise:int=0):
        if self.a_casino:
            argent_perdu, argent_gagne = b.blackjack(mise)
            compte.verser(argent_gagne)
            compte.retirer(argent_perdu)
        else:
            print("Cet hôtel ne possède pas de casino.")



def test_hotel():
    liste_chambres = []
    for etage in range(3):
        for numero in range(10):
            liste_chambres.append(Chambre(numero,etage,2,78.50,False))

    mon_hotel = Hotel('Hotel California','Vesoul','40 rue du Général',liste_chambres,150000,True,True)

    for _ in range(10):
        chambre = r.choice(mon_hotel.chambres)
        chambre.prendre()
    print("Nombre de chambres d'hotel :",mon_hotel.nb_chambres())
    print('Chambres disponibles :',mon_hotel.get_dispo())

    mon_compte = cb.CompteBancaire('1234',7500)
    print("Solde hotel avant paiement d'une chambre :",mon_hotel.get_compte().get_solde())

    mon_hotel.payer(7,2,mon_compte)
    print("Solde hotel après paiement d'une chambre :",mon_hotel.get_compte().get_solde())

    nouv_liste_chambres = []
    for numero in range(5):
        nouv_liste_chambres.append(Chambre(numero,3,1,62,False))
    mon_hotel.add_chambres(nouv_liste_chambres)
    print("Nombre de chambres d'hotel après ajout de 5 :",mon_hotel.nb_chambres())

    print("Solde avant partie de blackjack :",mon_compte.get_solde())
    mon_hotel.jouer_blackjack(mon_compte,10)
    print("Solde après partie de blackjack :",mon_compte.get_solde())

test_hotel()
