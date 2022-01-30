import BaseConoscenza as KB
import Classificatore as clas
import Grafo as grf

def menu(inputUtente):


    if(inputUtente == "classificazione"):
        clas.classificatore()
    elif(inputUtente == "valutazioneClassificatore"):
        clas.valutazione()
    elif(inputUtente == "trovaRegioniRischioMoltoBasso"):
        lista = KB.trovaRegioniMoltoBasso()
        print(lista)
    elif(inputUtente == "trovaRegioniRischioBasso"):
        lista = KB.trovaRegioniBasso()
        print(lista)
    elif(inputUtente == "trovaRegioniRischioModerato"):
        lista = KB.trovaRegioniModerato()
        print(lista)
    elif(inputUtente == "trovaRegioniRischioAlto"):
        lista = KB.trovaRegioniAlto()
        print(lista)
    elif(inputUtente == "trovaRegioniRischioMoltoAlto"):
        lista = KB.trovaRegioniMoltoAlto()
        print(lista)
    elif(inputUtente == "visualizzaListaRischi"):
        lista = KB.creaListaRischi()
        print(lista)
    elif(inputUtente == "trovaPercorso"):
        regionePartenza = input("Inserisci la regione da dove vuoi partire (es. Puglia): ")
        regioneArrivo = input("Inserisci la regione in cui vuoi arrivare (es. Puglia): ")
        grf.trovaPercorso(regionePartenza, regioneArrivo)
    elif(inputUtente == "verificaPassaggio"):
        regionePartenza = input("Inserisci la regione da dove vuoi partire (es. Puglia): ")
        regioneArrivo = input("Inserisci la regione in cui vuoi arrivare (es. Puglia): ")
        KB.domandaPassaggio(regionePartenza, regioneArrivo)
    elif(inputUtente == "verificaRischioRegione"):
        regione = input("Inserisci le regione di cui vuoi verificare il rischio (es. Puglia): ")
        rischio = input("Scegli il rischio da provare (moltoBasso/basso/moderato/alto/moltoAlto): ")
        KB.domandaRischioregione(regione, rischio)
    elif(inputUtente == "esci"):
        print("Sto uscendo...")
        return 0

if __name__ == '__main__':
    print("Benvenuto \n")

    inputUtente = None
    while(inputUtente != "esci"):
        inputUtente = input("Digita il comando che ti interessa: ")
        menu(inputUtente)

