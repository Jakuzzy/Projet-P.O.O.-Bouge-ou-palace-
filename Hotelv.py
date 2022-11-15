class Chambre:
    def __init__(self,numero,etage,capaciter,tarif,vue_mer=False):
        self.numero = numero
        self.etage = etage
        self.capaciter = capaciter
        self.etat_propreter = True
        self.etat_occupation = False
        self.tarif = tarif
        self.vue_mer = vue_mer

    def get_numero(self):
        return self.numero

    def get_etage(self):
        return self.etage

    def get_capaciter(self):
        return self.capaciter

    def get_etat_propreter(self):
        return self.etat_propreter

    def get_etat_occupation(self):
        return self.etat_occupation

    def get_tarif(self):
        return self.tarif

    def get_vue_mer(self):
        return self.vue_mer


    def nettoyer(self):
        self.etat_propreter = True

    def prendre(self):
        self.etat_occupation = True

    def liberer(self):
        self.etat_occupation = False

    def payer(self):
        pass

class Hotel:
    def __init__(self,nom,ville,adresse,chambres):
        self.nom = nom
        self.ville = ville
        self.adresse = adresse
        self.chambres = chambres
        self.piscine = True

    def get_nom(self):
        return self.nom

    def get_ville(self):
        return self.ville

    def get_adresse(self):
        return self.adresse

    def get_chambres(self):
        return self.chambres

    def get_piscine(self):
        return self.piscine


    def get_dispo(self):
        chambres_libres = 0
        for chambre in range(1,self.get_chambres()):
            if not chambre.get_etat_occupation():
                chambre_libre.append[chambre]
        return chambres_libres

    def nettoyer(self):
        for chambre in range(self.get_chambres()):
            chambre.nettoyer()

def test():
    hotel = Hotel("Bitume land Hotel","Bitume City","240 Rue du Bitume",24)

    for chambre in range(1,hotel.get_chambres()):
        chambre = Chambre(chambre,1,2,100,True)

    print(hotel.get_dispo())
