from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
import pandas as pd
import joblib       # Joblib è una libreria Python usata per salvare e caricare oggetti Python complessi in modo
                    # efficiente, come modelli di machine learning addestrati da file .pkl (pickle), così da
                    # non doverli riaddestrare ogni volta che si avvia l’app.


# Carica il dataset preprocessato; pd.read_csv è una funzione di pandas che legge un file CSV e lo trasforma in un DataFrame
df = pd.read_csv("C:/Users/idset/Desktop/UniPegaso/Project work/datasetliv1_preprocessed.csv", sep='|')


X = df['body_clean']        # Estrae le colonna desiderate dal dataframe
y_dept = df['department']   
y_sent = df['sentiment']    

X_train, X_test, y_dept_train, y_dept_test, y_sent_train, y_sent_test = train_test_split(    # Divide in test e train (20/80)
    X, y_dept, y_sent, test_size=0.2, random_state=42, stratify=y_dept)                      # Duplica le 3 variabili create precedentemente
                                                                                             # tenendo conto delle suddivisione 80/20 traning/test.
                                                                         # random_state=42 è il seme della suddivisione casuale in modo da ottenere
                                                                         # sempre la stessa suddivisione in caso di riesecuzione del codice;
                                                                         # stratify=y_dept fa in modo che la suddivisione mantenga la stessa 
                                                                         # proporzione delle classi di reparto sia nel training che nel test



vectorizer = TfidfVectorizer()   # Vettorizzazione TF-IDF (si può aggiungere ngram_range=(1,2) per bigrammi)
                                 # Crea un'istanza dell'oggetto TfidfVectorizer di scikit-learn, che serve a trasformare il testo 
                                 # in una rappresentazione numerica basata sulla tecnica TF-IDF. Prende in input testi (stringhe) 
                                 # e li trasforma in vettori(array) numerici, dove ogni dimensione rappresenta una parola (o un n-gramma)
                                 # Ogni valore è il punteggio TF-IDF, che indica l'importanza relativa di quella parola nel documento rispetto 
                                 # all'intero corpus. Ad esempio, in un dataset di 1500 recensioni, dopo quest'operazione avrò 1500 vettori/array.
                                 # Ogni vettore rappresenta la recensione corrispondente in forma numerica, con tante dimensioni quante sono  
                                 # le parole uniche nel vocabolario costruito dal corpus (dataset).
                                 # Si otterrà quindi una matrice di dimensione 1500 x (numero di parole uniche), dove ogni riga è il vettore TF-IDF 
                                 # di una recensione.
                                 # Il punteggio TF-IDF misura quanto una parola è importante in una recensione rispetto a tutte le recensioni:
                                 # TF (Term Frequency): conta quante volte la parola appare nel testo. Più appare, più è importante in quel testo.
                                 # IDF (Inverse Document Frequency): dà meno peso alle parole molto comuni che appaiono in quasi tutti i testi 
                                 # (come "il", "e", "ma") e più peso alle parole rare e specifiche.
                                 # Il vettore finale avrà forma di questo tipo: [0.3, 0.5, 0.0, 0.2, 0.1, 0.4, 0.1, 0.3, 0.2, 0.3, 0.0, 0.2]
                                 # dove i numeri sono valori TF-IDF ipotetici. Le parole più frequenti e specifiche avranno valori più alti,
                                 # mentre Le parole comuni o assenti avranno valori bassi o zero.


##### APPROFONDIMENTO sul calcolo di TF e IDF:

# TF = (numero di volte che la parola appare nella singola recensione) / (numero totale di parole in quella recensione)
# IDF = logaritmo inverso della frequenza della parola in tutto il dataset (più la parola è rara, più alto è il valore) = log(N/(1+n(t)))
# Dove N = è il numero totale di recensioni nel dataset (tutte le 1500 recensioni)
# n(t) è il numero di recensioni in cui compare il termine t
# Il "+1" nel denominatore serve a evitare divisioni per zero se la parola non compare in nessun documento (caso particolare che può verificarsi
# se si lavora con sottoinsiemi o filtri particolari del dataset. Il "+1" inoltre garantisce stabilità numerica e regolarizzazione, evitando
# che l’IDF diventi infinito o troppo grande se una parola compare in pochissimi documenti (es. solo uno).
# Questa tecnica è una forma di "smoothing" (levigatura) che rende il calcolo più robusto e meno sensibile a casi limite.

# In pratica, l’IDF misura quanto una parola è rara nel dataset:
# Se una parola compare in molti documenti, 𝑛(t) è grande e quindi l’IDF è basso (la parola è comune, poco discriminante);
# Se una parola compare in pochi documenti, 𝑛(t) è piccolo e quindi l’IDF è alto (la parola è rara e più significativa).
# Il TF e l'IDF vengono poi moltiplicati per ottenere il valore TF-IDF. Questa formula aiuta a dare più peso alle parole 
# che sono importanti per distinguere un documento dagli altri, riducendo il peso delle parole troppo comuni.

# Il valore TF-IDF subisce poi la normalizzazione L2 che serve a "scalare" i valori numerici in modo che la lunghezza complessiva del 
# vettore sia sempre pari a 1 per rendere i vettori confrontabili tra loro, anche se i testi hanno lunghezze e valori TF-IDF molto diversi.
# La normalizzazione del vettore è calcolata come la radice quadrata della somma dei quadrati di tutti i numeri che compongono il vettore:
# Normalizzare il vettore significa dividere ogni numero del vettore per questa lunghezza, così che la lunghezza totale diventi 1.
# Questo evita che testi più lunghi (con più parole o con valori TF-IDF più alti) abbiano vettori con valori numerici molto più grandi, 
# bilanciando quindi l'importanza relativa delle parole indipendentemente dalla lunghezza del testo. Di conseguenza, anche parole con 
# frequenze simili possono avere valori TF-IDF leggermente diversi dopo la normalizzazione, perché il vettore viene "ridimensionato" 
# nel suo insieme. Questo processo rende i vettori confrontabili tra loro, anche se i testi hanno lunghezze molto diverse.


X_train_tfidf = vectorizer.fit_transform(X_train)  # Analizza le recensioni di addestramento (X_train) e costruisce la matrice dei valori TF-IDF;
                                                   # Fit costruisce il vocabolario delle parole uniche presenti in tutto il training set e le salva
                                                   # come attributi interni dell'oggetto vectorizer (vectorizer.vocabulary_ e vectorizer.idf_);
                                                   # Transform converte in un vettore numerico TF-IDF, dove ogni dimensione corrisponde a una 
                                                   # parola del vocabolario e il valore è il peso TF-IDF di quella parola nella recensione

X_test_tfidf = vectorizer.transform(X_test)        # Trasforma i testi di test (X_test) in vettori TF-IDF usando il vocabolario e i pesi IDF 
                                                   # già calcolati durante il fit sul training setnon costruisce un nuovo vocabolario né ricalcola 
                                                   # i pesi, ma usa quelli già calcolati sul training set garantendo che le caratteristiche (parole)
                                                   # siano le stesse e che ilmodello non "impari" dai dati di test.



clf_dept = LogisticRegression(max_iter=1000, random_state=42)  # Modello Logistic regression, con 1000 iterazioni massime e 42 di seme casuale. 
                                                               # clf_dept è un’istanza della classe LogisticRegression di scikit-learn.
                                                               # Contiene un oggetto modello di Logistic Regression non ancora addestrato
                                                               # perché non è stato ancora chiamato il metodo .fit()


##### APPROFONDIMENTO ##### - (fonte: https://it.wikipedia.org/wiki/Modello_logit)
# A grandi linee, il modello di logistic_regression funziona in questo modo:

#   1 - Ad ogni valore presente nella matrice TF-IDF viene assegnato un peso, inizialmente 0, prossimo a 0 o comunque molto piccolo 
#       (calcolato a partire dal random_state=42). Questo significa che il modello non dà ancora importanza a nessuna parola.
#   2 - Per ogni recensione, si calcola la combinazione lineare data dalla somma di tutti i valori TF-IDF * i pesi appena assegnati 
#       + un valore "b" (di bias), anch'esso assegnato inizialmente molto piccolo ed anch'esso soggetto ad ottimizzazione in base alle 
#       reiterazioni successive. I valori ottenuti da queste somme vengono normalizzati per essere compresi tra 0 e 1.
#   3 - Si confrontano i valori così ottenuti con le etichette reali (reparto e sentiment presenti nel dataset di addestramento).
#       La differenza tra predizione e realtà è misurata da una funzione di perdita.
#   4 - L’algoritmo calcola il gradiente della funzione di perdita rispetto ai pesi, cioè la direzione in cui modificare i pesi per 
#       ridurre l’errore. I pesi vengono aggiornati di una piccola quantità in quella direzione (passo di discesa del gradiente).
#   5 - Questo processo (calcolo predizioni -> errore -> aggiornamento pesi) si ripete per ogni iterazione. Ad ogni iterazione i pesi 
#       si aggiustano un po’ per migliorare la capacità del modello di predire correttamente tutte le recensioni.
#   6 - Il parametro max_iter=1000 indica che l’algoritmo può fare fino a 1000 cicli di aggiornamento pesi. Se converge prima (cioè 
#       se i pesi non cambiano più significativamente), si ferma prima.
#
#       In sintesi, il modello parte da pesi zero, calcola predizioni, misura l’errore, aggiorna i pesi per ridurre l’errore, e ripete 
#       questo ciclo fino a convergenza o al massimo numero di iterazioni.
#       Spesso 1000 iterazioni sono più che sufficienti per dataset di questa dimensione, ma se il modello non converge (cioè i pesi
#       non si stabilizzano), si può aumentare questo valore. In molti framework (come scikit-learn), quando chiami il metodo fit, 
#       puoi ricevere un messaggio di warning se il modello non converge entro il numero massimo di iterazioni.


clf_dept.fit(X_train_tfidf, y_dept_train)    # Inizio apprendimento vero e prorpio; all'interno di questa chiamata, il modello L-R esegue il
                                             # processo di ottimizzazione iterativa: calcola le predizioni, valuta l’errore, aggiorna i pesi
                                             # e il bias, e ripete finché i pesi si stabilizzano o si raggiunge il numero massimo di iterazioni.
                                                
y_dept_pred = clf_dept.predict(X_test_tfidf)   # applica il modello addestrato ai dati di test per fare previsioni.
                                               # Restituisce un array y_dept_pred con le etichette predette (es. Housekeeping, Reception, F&B) 
                                               # per ogni recensione di test.



clf_sent = LogisticRegression(max_iter=1000, random_state=42)   # Effettua le stesse 3 operazioni precedenti ma sul Sentiment
clf_sent.fit(X_train_tfidf, y_sent_train)
y_sent_pred = clf_sent.predict(X_test_tfidf)




joblib.dump(vectorizer, "C:/Users/idset/Desktop/UniPegaso/Project work/tfidf_vectorizer.pkl")  # Salvataggio del vettorizzatore TF-IDF
joblib.dump(clf_dept, "C:/Users/idset/Desktop/UniPegaso/Project work/clf_dept.pkl")  # Salvataggio del modello di classificazione reparto
joblib.dump(clf_sent, "C:/Users/idset/Desktop/UniPegaso/Project work/clf_sent.pkl")  # Salvataggio del modello di classificazione sentiment

print("Modelli e vettorizzatore salvati correttamente in file .pkl")