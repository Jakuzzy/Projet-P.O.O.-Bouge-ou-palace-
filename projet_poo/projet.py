import comptes_bancaires as cb

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
    def __init__(self, numero:int, etage:int, capacite:int, tarif:float, a_vue_mer:bool) :
        """Créer une nouvelle Chambre()"""
        self.numero = numero
        self.etage = etage
        self.capacite = max(min(capacite,3),1)
        self.est_propre = True
        self.est_occupee = False
        self.tarif = tarif
        self.a_vue_mer = a_vue_mer

    def get_numero(self):
        return self.numero

    def get_etage(self):
        return self.etage

    def get_capacite(self):
        return self.capacite

    def get_est_propre(self):
        return self.est_propre

    def get_est_occupee(self):
        return self.est_occupee

    def get_tarif(self):
        return self.tarif

    def get_a_vue_mer(self):
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
        return None

##    def	payer(self) :
##        """"""
##        pass
##        return None



class Hotel :
    """
    Chaque instance de Hotel possède comme attributs :
    -	Un nom
    -	Une ville
    -	Une adresse
    -	Des chambres
    -	Une piscine ou non

    La classe est pourvue des méthodes suivantes :
    -	get_dispo() qui renvoie le nombre de chambres disponibles.
    -	nettoyer() qui fait le ménage dans toutes les chambres de cet hôtel.
    -	Des méthodes permettant d’accéder à chacun des attributs.
    """

    def __init__(self, nom:str, ville:str, adresse:str, a_piscine:bool=False):
        """Créé un nouvel Hotel()"""
        self.nom = nom
        self.ville = ville
        self.adresse = adresse
        self.chambres = []
        self.a_piscine = a_piscine

    def get_nom(self):
        return self.nom

    def get_ville(self):
        return self.ville

    def get_adresse(self):
        return self.adresse

    def get_chambres(self):
        return self.chambres

    def get_a_piscine(self):
        return self.a_piscine

    def get_dispo(self):
        chambres_non_occupee = 0
        for chambre in self.chambres:
            if not chambre.get_est_occupee():
                chambres_non_occupee +=1
        return chambres_non_occupee

    def	nettoyer(self) :
        """Fait le ménage dans toutes les chambres de cet hôtel"""
        for chambre in self.chambres:
            chambre.nettoyer()
        return None