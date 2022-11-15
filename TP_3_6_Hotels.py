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
    def __init__(self, numero, etage, capacite, est_propre, est_occupee, tarif, a_vue_mer) :
        self.numero = numero
        self.etage = etage
        self.capacite = capacite
        self.est_propre = est_propre
        self.est_occupee = est_occupee
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
        """déclare la chambre propre"""
        self.est_propre = True
        return None

    def	prendre(self) :
        """déclare la chambre occupée"""
        self.est_occupee = True
        return None

    def	liberer(self) :
        """déclare la chambre non-occupée"""
        self.est_occupee = False
        return None

    def	payer(self) :
        """"""
        pass
        return None

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

    def __init__(self, nom, ville, adresse, chambres, a_piscine):
        self
