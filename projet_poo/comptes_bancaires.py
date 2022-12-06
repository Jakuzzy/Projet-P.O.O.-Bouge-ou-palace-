class CompteBancaire:
    """Classe défini par :
            - son numéro
            - son solde """

    def __init__(self,numero,solde=0):
        """Créer un nouveau Compte()"""
        self.solde = solde
        self.numero = numero

    def get_solde(self):
        """Obtenir le solde du compte"""
        return self.solde

    def get_numero(self):
        """Obtenir le numero du compte"""
        return self.numero

    def verser(self,nb):
        """Verser un montant sur un compte"""
        nb = max(0,nb)
        self.solde += nb

    def retirer(self,nb):
        """Retirer un montant sur un compte"""
        nb = max(0,nb)
        self.solde -= nb

    def transferer(self,compte,nb):
        """Transférer un montant d’un compte sur un autre compte"""
        nb = max(0,nb)
        self.solde -= nb
        compte.solde += nb



class ClientBanque:
    """Classe défini par :
            - son nom
            - son adresse
            - ses comptes """

    def __init__(self,nom,adresse,compte):
        """Créer un nouveau ClientBanque()"""
        self.nom = nom
        self.adresse = adresse
        self.comptes = [compte]

    def get_nom(self):
        """Obtenir le nom du client"""
        return self.nom

    def get_adresse(self):
        """Obtenir l'adresse du client"""
        return self.adresse

    def get_comptes(self):
        """Obtenir les comptes du client"""
        return self.comptes

    def update_comptes(self,nouv_compte):
        """Mettre à jour la liste des comptes"""
        self.comptes += [nouv_compte]



class Banque:
    def __init__(self):
        """Classe défini par :
            - ses clients """
        self.clients = []

    def get_clients(self):
        """Obtenir la liste des clients"""
        return self.clients

    def creer_compte(self,nom,adresse,numero_compte,solde_initial=0):
        """Créer un nouveau compte"""
        nouv_compte = CompteBancaire(numero_compte,solde_initial)
        for client in self.clients:
            if client.get_nom() == nom and client.get_adresse() == adresse:
                client.update_comptes(nouv_compte)
                break
        else:
            self.clients.append(Client(nom,adresse,nouv_compte))

    def get_client(self,nom,adresse):
        """Renvoie le client si il est client de la banque sinon False"""
        for client in self.clients:
            if client.get_nom() == nom and client.get_adresse() == adresse:
                return client
                break
        else:
            return False

    def get_liste_comptes(self,nom,adresse):
        """Renvoie la liste des comptes d'un client"""
        client = self.get_client(nom,adresse)
        if client:
            return client.get_comptes()
        else:
            return client

    def supprimer_compte(self,nom,adresse,numero_compte):
        """Fonctionne peut-être"""
        client = self.get_client(nom,adresse)
        if client:
            for i in range(len(client.comptes)):
                if client.comptes[i].numero == numero_compte:
                    client.comptes.pop(i)
                    return True
                break
        else:
            return False