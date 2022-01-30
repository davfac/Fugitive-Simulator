import numpy as np

class Grafo:
    #Inizializza grafo
    def __init__(self, grafoDict=None, orientato=True):
        self.grafoDict = grafoDict or {}
        self.orientato = orientato
        if not orientato:
            self.conversioneNonOrientato()
    #Converte un grafo orientato in non orientato
    def conversioneNonOrientato(self):
        for a in list(self.grafoDict.keys()):
            for (b, dist) in self.grafoDict[a].items():
                self.grafoDict.setdefault(b, {})[a] = dist
    #Aggiunge un collegamento tra nodo A e B con un relativo peso, nel caso di grafo non orientato, aggiunge un ulteriore
    #collegamente da nodo B a nodo A
    def connessione(self, A, B, distanza=1):
        self.grafoDict.setdefault(A, {})[B] = distanza
        if not self.orientato:
            self.grafoDict.setdefault(B, {})[A] = distanza
    #Prende i nodi adiacenti
    def get(self, a, b=None):
        links = self.grafoDict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    #Restituisce lista di nodi
    def nodi(self):
        s1 = set([k for k in self.grafoDict.keys()])
        s2 = set([k2 for v in self.grafoDict.values() for k2, v2 in v.items()])
        nodi = s1.union(s2)
        return list(nodi)
    #Rimuove dal grafo una regione (nodo)
    def rimuovi(self, listaRegioni, nomeRegione):
        for i in range (len(listaRegioni)):
            if(self.grafoDict[listaRegioni[i].name].get(nomeRegione) != None):
               self.grafoDict[listaRegioni[i].name].pop(nomeRegione)
        self.grafoDict.pop(nomeRegione)

class Nodo:
    #Inizializza un nodo
    def __init__(self, nome:str, genitore:str):
        self.nome = nome
        self.genitore = genitore
        #Distanza da nodo iniziale
        self.g = 0
        #Distanza da nodo obiettivo
        self.h = 0
        #Costo totale delle distanze
        self.f = 0
    #Effettua comparazione tra nodi
    def __eq__(self, other):
        return self.nome == other.nome
    #Ordina i nodi in base al costo
    def __lt__(self, other):
         return self.f < other.f
    #Stampa i nodi
    def __repr__(self):
        return ('({0},{1})'.format(self.nome, self.f))


class Regione:
    # Initialize the class
    def __init__(self, name: str):
        self.name = name
        self.polizia = creaPolizia()
        self.rischio = assegnaRischio(self.polizia)


def creaPolizia():
    numeroCasuale = np.random.randint(100)

    return numeroCasuale


def assegnaRischio(polizia):
    if (polizia <= 20):
        rischio = 'moltoBasso'
    if (polizia > 20 and polizia <= 40):
        rischio = 'basso'
    if (polizia > 40 and polizia <= 60):
        rischio = 'moderato'
    if (polizia > 60 and polizia <= 80):
        rischio = 'alto'
    if (polizia > 80):
        rischio = 'moltoAlto'

    return rischio

#Calcola il costo del percorso reale da un nodo A ad un nodo B
def calcoloCostoReale(partenza, target):
    costo = (partenza + target) / 2

    return costo

#Stima il costo del percorso da un nodo A ad un nodo B
def calcoloEuristica (partenza, target):
    euristica = (partenza + target) / 2

    return euristica

#Serve per trovare il percorso da una regione A ad una regione B nel grafo
#Restituisce un vettore che mantiene tutte le euristiche per le regioni che ci sono in mezzo tra A e B
def vettoreEuristiche (regione:Regione, lista):
    euristiche = {}
    for i in range (len(lista)):
            euristiche[lista[i].name] = calcoloEuristica(regione.polizia, lista[i].polizia)
    return euristiche

#Verifica che un nodo adiacente sia stato inserito nella lista dei nodi aperti
def verificaAggiuntaNeighbour(open, neighbour):
    for node in open:
        if (neighbour == node and neighbour.f > node.f):
            return False
    return True

#Ricerca A*
def ricercaAStar(grafo, euristiche, partenza: Regione, arrivo: Regione):

    open = []
    closed = []
    nodoPartenza = Nodo(partenza.name, None)
    nodoArrivo = Nodo(arrivo.name, None)
    open.append(nodoPartenza)

    while len(open) > 0:
        open.sort()
        nodoCorrente = open.pop(0)
        closed.append(nodoCorrente)

        if nodoCorrente == nodoArrivo:
            path = []
            while nodoCorrente != nodoPartenza:
                path.append(nodoCorrente.nome)
                nodoCorrente = nodoCorrente.genitore
            path.append(nodoPartenza.nome)
            return path[::-1]
        neighbours = grafo.get(nodoCorrente.nome)
        for key, value in neighbours.items():
            neighbour = Nodo(key, nodoCorrente)
            if (neighbour in closed):
                continue
            neighbour.g = (nodoCorrente.g + grafo.get(nodoCorrente.nome, neighbour.nome)) / 2
            neighbour.h = euristiche.get(neighbour.nome)
            neighbour.f = (neighbour.g + neighbour.h) / 2
            if (verificaAggiuntaNeighbour(open, neighbour) == True):
                open.append(neighbour)
    return None

lista = []
ValleAosta = Regione("ValleAosta")
lista.append(ValleAosta)
Piemonte = Regione("Piemonte")
lista.append(Piemonte)
Lombardia = Regione("Lombardia")
lista.append(Lombardia)
Liguria = Regione("Liguria")
lista.append(Liguria)
EmiliaRomagna = Regione("EmiliaRomagna")
lista.append(EmiliaRomagna)
Veneto = Regione("Veneto")
lista.append(Veneto)
TrentinoAltoAdige = Regione("TrentinoAltoAdige")
lista.append(TrentinoAltoAdige)
FriuliVeneziaGiulia = Regione("FriuliVeneziaGiulia")
lista.append(FriuliVeneziaGiulia)
Toscana = Regione("Toscana")
lista.append(Toscana)
Marche = Regione("Marche")
lista.append(Marche)
Umbria = Regione("Umbria")
lista.append(Umbria)
Lazio = Regione("Lazio")
lista.append(Lazio)
Abruzzo = Regione("Abruzzo")
lista.append(Abruzzo)
Campania = Regione("Campania")
lista.append(Campania)
Molise = Regione("Molise")
lista.append(Molise)
Puglia = Regione("Puglia")
lista.append(Puglia)
Basilicata = Regione("Basilicata")
lista.append(Basilicata)
Calabria = Regione("Calabria")
lista.append(Calabria)
Sardegna = Regione("Sardegna")
lista.append(Sardegna)
Sicilia = Regione("Sicilia")
lista.append(Sicilia)

#Genera il grafo con le relative connessioni pesate tra i nodi
def generaGrafo():

    grafo = Grafo()

    grafo.connessione(ValleAosta.name, Piemonte.name, calcoloCostoReale(ValleAosta.polizia, Piemonte.polizia))
    grafo.connessione(Piemonte.name, Lombardia.name, calcoloCostoReale(Piemonte.polizia, Lombardia.polizia))
    grafo.connessione(Liguria.name, EmiliaRomagna.name, calcoloCostoReale(Liguria.polizia, EmiliaRomagna.polizia))
    grafo.connessione(Liguria.name, Toscana.name, calcoloCostoReale(Liguria.polizia, Toscana.polizia))
    grafo.connessione(Piemonte.name, Liguria.name, calcoloCostoReale(Piemonte.polizia, Liguria.polizia))
    grafo.connessione(Piemonte.name, EmiliaRomagna.name, calcoloCostoReale(Piemonte.polizia, EmiliaRomagna.polizia))
    grafo.connessione(Lombardia.name, EmiliaRomagna.name, calcoloCostoReale(Lombardia.polizia, EmiliaRomagna.polizia))
    grafo.connessione(Lombardia.name, Veneto.name, calcoloCostoReale(Lombardia.polizia, Veneto.polizia))
    grafo.connessione(Lombardia.name, TrentinoAltoAdige.name, calcoloCostoReale(Lombardia.polizia, TrentinoAltoAdige.polizia))
    grafo.connessione(TrentinoAltoAdige.name, Veneto.name, calcoloCostoReale(TrentinoAltoAdige.polizia, Veneto.polizia))
    grafo.connessione(Veneto.name, FriuliVeneziaGiulia.name, calcoloCostoReale(Veneto.polizia, FriuliVeneziaGiulia.polizia))
    grafo.connessione(Veneto.name, EmiliaRomagna.name, calcoloCostoReale(Veneto.polizia, EmiliaRomagna.polizia))
    grafo.connessione(EmiliaRomagna.name, Toscana.name, calcoloCostoReale(EmiliaRomagna.polizia, Toscana.polizia))
    grafo.connessione(EmiliaRomagna.name, Marche.name, calcoloCostoReale(EmiliaRomagna.polizia, Marche.polizia))
    grafo.connessione(Toscana.name, Marche.name, calcoloCostoReale(Toscana.polizia, Marche.polizia))
    grafo.connessione(Toscana.name, Umbria.name, calcoloCostoReale(Toscana.polizia, Umbria.polizia))
    grafo.connessione(Toscana.name, Lazio.name, calcoloCostoReale(Toscana.polizia, Lazio.polizia))
    grafo.connessione(Marche.name, Umbria.name, calcoloCostoReale(Marche.polizia, Umbria.polizia))
    grafo.connessione(Marche.name, Lazio.name, calcoloCostoReale(Marche.polizia, Lazio.polizia))
    grafo.connessione(Marche.name, Abruzzo.name, calcoloCostoReale(Marche.polizia, Abruzzo.polizia))
    grafo.connessione(Umbria.name, Lazio.name, calcoloCostoReale(Umbria.polizia, Lazio.polizia))
    grafo.connessione(Lazio.name, Abruzzo.name, calcoloCostoReale(Lazio.polizia, Abruzzo.polizia))
    grafo.connessione(Lazio.name, Molise.name, calcoloCostoReale(Lazio.polizia, Molise.polizia))
    grafo.connessione(Lazio.name, Campania.name, calcoloCostoReale(Lazio.polizia, Campania.polizia))
    grafo.connessione(Abruzzo.name, Molise.name, calcoloCostoReale(Abruzzo.polizia, Molise.polizia))
    grafo.connessione(Molise.name, Campania.name, calcoloCostoReale(Molise.polizia, Campania.polizia))
    grafo.connessione(Molise.name, Puglia.name, calcoloCostoReale(Molise.polizia, Puglia.polizia))
    grafo.connessione(Campania.name, Puglia.name, calcoloCostoReale(Campania.polizia, Puglia.polizia))
    grafo.connessione(Campania.name, Basilicata.name, calcoloCostoReale(Campania.polizia, Basilicata.polizia))
    grafo.connessione(Puglia.name, Basilicata.name, calcoloCostoReale(Puglia.polizia, Basilicata.polizia))
    grafo.connessione(Basilicata.name, Calabria.name, calcoloCostoReale(Basilicata.polizia, Calabria.polizia))
    grafo.connessione(Calabria.name, Sicilia.name, calcoloCostoReale(Calabria.polizia, Sicilia.polizia))
    grafo.connessione(Sicilia.name, Sardegna.name, calcoloCostoReale(Sicilia.polizia, Sardegna.polizia))

    grafo.conversioneNonOrientato()
    regioni = lista.copy()
    i = 0

    while (i < (len(regioni))):
        if (regioni[i].rischio == "moltoAlto"):
            grafo.rimuovi(regioni, regioni[i].name)
            regioni.pop(i)
            i = i - 1
        i = i + 1

    return grafo

#Trova percorso da nodo A a nodo B
def trovaPercorso(partenza, arrivo):
    regionePartenza = None
    regioneArrivo = None
    for i in range(len(lista)):
        if lista[i].name.lower() == partenza.lower():
            regionePartenza = lista[i]
        if lista[i].name.lower() == arrivo.lower():
            regioneArrivo = lista[i]

    if (regionePartenza == None or regioneArrivo == None):
        print("Inserimento errato!")
        return
    grafo = generaGrafo()

    euristiche = vettoreEuristiche(regioneArrivo, lista)

    percorso = ricercaAStar(grafo, euristiche, regionePartenza, regioneArrivo)
    print(percorso)