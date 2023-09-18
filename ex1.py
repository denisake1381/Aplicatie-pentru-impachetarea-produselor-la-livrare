# Tema L33 Python
# 1. Implementati o aplicatie pentru impachetarea produselor la livrare. Aplicatia defineste
# conceptele de Cutie, Produs si Comanda. Fiecare comanda contine numele clientului si o lista de
# produse comandate. Produsul contine pretul si numele produsului iar Cutia contine unul sau mai
# multe produse.

class Produs:
    def __init__(self, nume, pret):
        self.nume = nume
        self.pret = pret

class Cutie:
    def __init__(self):
        self.produse = []

    def adauga_produs(self, produs):
        self.produse.append(produs)

    def calculeaza_total(self):
        total = 0
        for produs in self.produse:
            total += produs.pret
        return total

class Comanda:
    def __init__(self, nume_client):
        self.nume_client = nume_client
        self.produse_comandate = []

    def adauga_produs(self, produs):
        self.produse_comandate.append(produs)

    def calculeaza_total(self):
        total = 0
        for produs in self.produse_comandate:
            total += produs.pret
        return total

    def impacheteaza(self):
        cutii = []
        cutie_curenta = Cutie()
        capacitate_maxima = 100  

        for produs in self.produse_comandate:
            if cutie_curenta.calculeaza_total() + produs.pret <= capacitate_maxima:
                cutie_curenta.adauga_produs(produs)
            else:
                cutii.append(cutie_curenta)
                cutie_curenta = Cutie()
                cutie_curenta.adauga_produs(produs)

        if cutie_curenta.produse:
            cutii.append(cutie_curenta)

        return cutii

produs1 = Produs("Telefon", 1000)
produs2 = Produs("Tableta", 700)
produs3 = Produs("Casti", 150)

comanda = Comanda("Denis Pavel")
comanda.adauga_produs(produs1)
comanda.adauga_produs(produs2)
comanda.adauga_produs(produs3)

cutii = comanda.impacheteaza()
for i, cutie in enumerate(cutii):
    print(f"Cutie {i+1}: Total = {cutie.calculeaza_total()}")


