from Grafo import lista

#Crea la lista delle regioni confinanti
def creaListaRegioniConfinanti():
    listaConfini = {}
    listaConfini["CampaniaBasilicata"] = True
    listaConfini["BasilicataCalabria"] = True
    listaConfini["CalabriaSicilia"] = True
    listaConfini["SiciliaSardegna"] = True
    listaConfini["PugliaBasilicata"] = True
    listaConfini["PugliaMolise"] = True
    listaConfini["MoliseAbruzzo"] = True
    listaConfini["PugliaCampania"] = True
    listaConfini["MoliseCampania"] = True
    listaConfini["MoliseLazio"] = True
    listaConfini["AbruzzoLazio"] = True
    listaConfini["CampaniaLazio"] = True
    listaConfini["AbruzzoMarche"] = True
    listaConfini["LazioToscana"] = True
    listaConfini["LazioUmbria"] = True
    listaConfini["MarcheLazio"] = True
    listaConfini["MarcheUmbria"] = True
    listaConfini["ToscanaUmbria"] = True
    listaConfini["ToscanaMarche"] = True
    listaConfini["ToscanaEmiliaRomagna"] = True
    listaConfini["MarcheEmiliaRomagna"] = True
    listaConfini["ToscanaLiguria"] = True
    listaConfini["EmiliaRomagnaLiguria"] = True
    listaConfini["PiemonteLiguria"] = True
    listaConfini["EmiliaRomagnaPiemonte"] = True
    listaConfini["EmiliaRomagnaLombardia"] = True
    listaConfini["EmiliaRomagnaVeneto"] = True
    listaConfini["PiemonteLombardia"] = True
    listaConfini["PiemonteValleAosta"] = True
    listaConfini["LombardiaTrentinoAltoAdige"] = True
    listaConfini["LombardiaVeneto"] = True
    listaConfini["VenetoTrentinoAltoAdige"] = True
    listaConfini["VenetoFriuliVeneziaGiulia"] = True

    return listaConfini


listaConfiniRegioni = creaListaRegioniConfinanti()


#Restituisce la lista con i rischi per ogni regione
def creaListaRischiRegioni():
    listaRischi = {}
    for i in range(len(lista)):
        rischio = lista[i].rischio
        stringa = (lista[i].name + "_" + rischio)
        listaRischi[stringa] = True
    return listaRischi


listaRischiRegioni = creaListaRischiRegioni()

#Trova il rischio per un determinata regione
def trovaRischioRegione(regione_rischio: str):
    if (listaRischiRegioni.get(regione_rischio) == None):
        return False
    else:
        return True

#Trova le regioni con rischio molto alto
def trovaRegioniMoltoAlto():
    listaRischioMoltoAlto = []
    # colorAssignment()
    for i in range(len(lista)):
        if (lista[i].rischio == 'moltoAlto'):
            listaRischioMoltoAlto.append(lista[i].name)
    return listaRischioMoltoAlto

#Trova le regioni con rischio alto
def trovaRegioniAlto():
    listaRischioAlto = []
    # colorAssignment()
    for i in range(len(lista)):
        if (lista[i].rischio == 'alto'):
            listaRischioAlto.append(lista[i].name)
    return listaRischioAlto

#Trova le regioni con rischio moderato
def trovaRegioniModerato():
    listaRischioModerato = []
    # colorAssignment()
    for i in range(len(lista)):
        if (lista[i].rischio == 'moderato'):
            listaRischioModerato.append(lista[i].name)
    return listaRischioModerato

#Trova le regioni con rischio basso
def trovaRegioniBasso():
    listaRischioBasso = []
    for i in range(len(lista)):
        if (lista[i].rischio == 'basso'):
            listaRischioBasso.append(lista[i].name)
    return listaRischioBasso

#Trova le regioni con rischio molto basso
def trovaRegioniMoltoBasso():
    listaRischioMoltoBasso = []
    # colorAssignment()
    for i in range(len(lista)):
        if (lista[i].rischio == 'moltoBasso'):
            listaRischioMoltoBasso.append(lista[i].name)
    return listaRischioMoltoBasso

#Restituisce la lista dei rischi che le regioni possono assumere
def creaListaRischi():
    listaRischi = []

    listaRischi.append('moltoBasso')
    listaRischi.append('basso')
    listaRischi.append('moderato')
    listaRischi.append('alto')
    listaRischi.append('moltoALto')

    return listaRischi


listaRischi = creaListaRischi()

#Controlla se esiste il rischio
def controlloRischio(rischio: str):
    for i in range(len(listaRischi)):
        if (listaRischi[i] == rischio):
            return True
    return False

#Verifica che una regione non abbia rischio molto alto
def notRischioMoltoAlto(regione: str):
    if (listaRischiRegioni.get(regione + "_moltoAlto") == None):
        return True
    else:
        return False

#Verifica che l'esistenza di una regione
def regioneEsiste(regione: str):
    for i in range(len(lista)):
        if (lista[i].name == regione):
            return True
    return False

#Verifica un determinato rischio per una determinata regione
def domandaRischioregione(regione: str, rischio: str):

    verifica = False

    if (not regioneEsiste(regione)):
        print("La regione inserita non esiste, inserire una regione valida")
        return
    if (not controlloRischio(rischio)):
        print("Il rischio inserito non esiste, inserire un rischio valido")
        return

    stringa = regione + "_" + rischio
    risposta = trovaRischioRegione(stringa)
    if (risposta):
        print("YES")
    else:
        print("NO")

    regione = regione.capitalize()
    while (verifica == False and rispostaUtente.lower() != "how"):
        rispostaUtente = input("Digitare (how) per la spiegazione o (esci) per terminare: ")
        if (rispostaUtente.lower() == "esci"):
            verifica = True
        if (rispostaUtente.lower() == "how"):
            print("rischio(" + regione + "," + rischio + ") <=> " + stringa)
            while (verifica == False and rispostaUtente.lower() != "how 1"):
                rispostaUtente = input("Per entrare nel dettaglio, digita (how i), con i numero dell'atomo"
                                        ", oppure digita (esci) per terminare: ")
                if (rispostaUtente.lower() == "esci"):
                    verifica = True
                if (rispostaUtente.lower() == 'how 1'):
                    print(stringa + " <=> ", risposta)
                elif (rispostaUtente.lower() != "how 1" and rispostaUtente.lower() != "esci"):
                    print("Attento: dovresti digitare (how 1) o (esci) se vuoi terminare.")
        elif (rispostaUtente.lower() != "how" and rispostaUtente.lower() != "esci"):
            print("Attento: dovresti digitare (how) o (esci) se vuoi terminare.")

#Verifica l'esistenza di un passaggio da una regione A ad una regione B
def domandaPassaggio(regionePartenza: str, regioneArrivo: str):

    if (not regioneEsiste(regionePartenza)):
        print("La regione di partenza inserita non esiste, inserire una regione valida.")
        return
    if (not regioneEsiste(regioneArrivo)):
        print("La regione di arrivo inserita non esiste, inserire una regione valida.")
        return

    dizFail = {}
    compareString_1 = regionePartenza + regioneArrivo
    compareString_2 = regioneArrivo + regionePartenza
    rispostaUtente = ""
    verifica = False

    if (listaConfiniRegioni.get(compareString_1) == None or listaConfiniRegioni.get(compareString_2) == None):
        dizFail[1] = True
    else:
        dizFail[1] = False

    dizFail[2] = notRischioMoltoAlto(regionePartenza)
    dizFail[3] = notRischioMoltoAlto(regioneArrivo)

    if (dizFail.get(1) == True and dizFail.get(2) == True and dizFail.get(3) == True):
        print("YES")
    else:
        print("NO")

    while(verifica == False and rispostaUtente.lower() != "how"):
        rispostaUtente = input("Digitare (how) per la spiegazione o (esci) per terminare: ")
        if(rispostaUtente.lower() == "esci"):
            verifica = True
        if (rispostaUtente.lower() == "how"):
            print(
                "passaggio(" + regionePartenza + "," + regioneArrivo + ") <=> confine(" + regionePartenza + ","
                + regioneArrivo + ") and notRischioMoltoAlto(" + regionePartenza + ") and notRischioMoltoAlto(" + regioneArrivo + ")")
            while(verifica == False and rispostaUtente.lower() != "how 1" and rispostaUtente.lower() != "how 2"
                        and rispostaUtente.lower() != "how 3"):
                rispostaUtente = input("Per entrare nel dettaglio, digita (how i), con i numero dell'atomo"
                                       ", oppure digita (esci) per terminare: ")
                if (rispostaUtente.lower() == "esci"):
                    verifica = True
                if (rispostaUtente.lower() == 'how 1'):
                    print("confine(" + regionePartenza + "," + regioneArrivo + ") <=>", dizFail.get(1))
                else:
                    if (rispostaUtente.lower() == 'how 2'):
                        print(
                            "notRischioMoltoAlto(" + regionePartenza + ") <=> " + regionePartenza + " rischio molto basso o " +
                            regionePartenza + "rischio basso o " + regionePartenza + " rischio moderato o " + regionePartenza + " rischio alto")
                        while(verifica == False and rispostaUtente.lower() != "how 1" and rispostaUtente.lower() != "how 2"
                        and rispostaUtente.lower() != "how 3" and rispostaUtente.lower() != "how 4"):
                            rispostaUtente = input(
                                "Per entrare nel dettaglio, digita (how i), con i numero dell'atomo"
                                ", oppure digita (esci) per terminare: ")
                            if (rispostaUtente == "esci"):
                                verifica = True
                            if (rispostaUtente.lower() == "how 1"):
                                print(regionePartenza + " rischio molto basso <=> ",
                                    trovaRischioRegione(regionePartenza + "_moltoBasso"))
                            else:
                                if (rispostaUtente.lower() == "how 2"):
                                    print(regionePartenza + "rischio basso <=> ", trovaRischioRegione(regionePartenza + "_basso"))
                                else:
                                    if (rispostaUtente.lower() == "how 3"):
                                        print(regionePartenza + "_rischio moderato <=> ",
                                            trovaRischioRegione(regionePartenza + "_moderato"))
                                    else:
                                        if (rispostaUtente.lower() == "how 4"):
                                            print(regionePartenza + "_rischio alto <=> ",
                                                trovaRischioRegione(regionePartenza + "_alto"))
                                        elif (rispostaUtente.lower() != "how 1" and rispostaUtente.lower() != "esci"
                                        and rispostaUtente.lower() != "how 2" and rispostaUtente.lower() != "how 3" and rispostaUtente.lower() != "how 4"):
                                            print("Attento: dovresti digitare (how 1) o (how 2) o (how 3) o (how 4) o (esci) se vuoi terminare.")
                    else:
                        if (rispostaUtente.lower() == 'how 3'):
                            print(
                                "notRischioMoltoAlto(" + regioneArrivo + ") <=> " + regioneArrivo + " rischio molto basso o " +
                                regioneArrivo + "rischio basso o " + regioneArrivo + " rischio moderato o " + regioneArrivo + " rischio alto")
                            while (verifica == False and rispostaUtente.lower() != "how 1" and rispostaUtente.lower() != "how 2"
                                    and rispostaUtente.lower() != "how 3" and rispostaUtente.lower() != "how 4"):
                                rispostaUtente = input(
                                    "Per entrare nel dettaglio, digita (how i), con i numero dell'atomo"
                                    ", oppure digita (esci) per terminare: ")
                                if (rispostaUtente.lower() == "esci"):
                                    verifica = True
                                if (rispostaUtente.lower() == "how 1"):
                                    print(regioneArrivo + "_rischio molto basso <=> ",
                                        trovaRischioRegione(regioneArrivo + "_moltoBasso"))
                                else:
                                    if (rispostaUtente.lower() == "how 2"):
                                        print(regioneArrivo + "_basso <=> ", trovaRischioRegione(regioneArrivo + "_basso"))
                                    else:
                                        if (rispostaUtente.lower() == "how 3"):
                                            print(regioneArrivo + "_moderato <=> ",
                                                trovaRischioRegione(regioneArrivo + "_moderato"))
                                        else:
                                            if (rispostaUtente.lower() == "how 4"):
                                                print(regioneArrivo + "_alto <=> ", trovaRischioRegione(regioneArrivo + "_alto"))
                                            elif (rispostaUtente.lower() != "how 1" and rispostaUtente.lower() != "esci"
                                            and rispostaUtente.lower() != "how 2" and rispostaUtente.lower() != "how 3" and rispostaUtente.lower() != "how 4"):
                                                print("Attento: dovresti digitare (how 1) o (how 2) o (how 3) o (how 4) o (esci) se vuoi terminare.")
                        elif (rispostaUtente.lower() != "how 1" and rispostaUtente.lower() != "esci"
                        and rispostaUtente.lower() != "how 2" and rispostaUtente.lower() != "how 3"):
                            print("Attento: dovresti digitare (how 1) o (how 2) o (how 3) o (esci) se vuoi terminare.")
        elif(rispostaUtente.lower() != "how" and rispostaUtente.lower() != "esci"):
            print(rispostaUtente)
            print("Attento: dovresti digitare (how) o (esci) se vuoi terminare.")
