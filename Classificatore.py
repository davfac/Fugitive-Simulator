import pandas as pd
from sklearn import tree
from sklearn.model_selection import cross_val_score


#Chiede i dati all'utente per poter classificare il nuovo esempio e restituisce la previsione
def classificatore():
    età = 0
    reato = ""

    while(età < 13 or età > 100):
        try:
            età = (int)(input("Inserisci la tua età: "))
            if(età < 13 ):
                print("Non è troppo presto per commettere reati?")
                print("Vengono considerati i reati solo per persone con età da 13 a 100 anni.")
            if(età > 100):
                print("A quell'età riesci ancora a commettere crimini?")
                print("Vengono considerati i reati solo per persone con età da 13 a 100 anni.")
        except ValueError:
            print("Devi inserire l'età a numero.")
    while(reato != 'omicidio' and reato != 'rapina' and reato != 'estorsione'):
        reato = input("Inserisci il reato che hai commesso (omicidio/rapina/estorsione): ")
        if(reato != 'omicidio' and reato != 'rapina' and reato != 'estorsione'):
            print("Inserisci un reato valido")
        if(reato == 'omicidio'):
            parametroReato = 0
        if(reato == 'rapina'):
            parametroReato = 1
        if(reato == 'estorsione'):
            parametroReato = 2

    anni = classificazione(età, parametroReato)
    for i in range(len(anni)):
        print("I tuoi anni da scontare in galera saranno circa:", anni[i])

#Classificatore vero e proprio (albero di decisione)
def classificazione(età:int, reato:int):
    dataset = pd.read_csv('punizioni.csv')

    X = dataset.drop(columns=['pena'])
    y = dataset['pena']

    classificatore = tree.DecisionTreeClassifier()
    classificatore.fit(X.values, y.values)
    pena = classificatore.predict([[età, reato]])

    return pena

#Valutazione del classificatore
def valutazione():
    dataset = pd.read_csv('punizioni.csv')
    X = dataset.drop(columns=['pena'])
    y = dataset['pena']

    classificatore = tree.DecisionTreeClassifier()
    classificatore.fit(X.values, y.values)
    
    score = cross_val_score(classificatore, X.values, y.values, scoring = 'r2', cv = 6)

    print("%0.2f di accurattezza, con una deviazione standard di %0.2f" % (score.mean(), score.std()))


    

