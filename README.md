PwRecHotel: 
Smistamento recensioni hotel e analisi del sentiment con Machine Learning.
Questo progetto sviluppa un prototipo di sistema automatico per l’analisi e lo smistamento delle recensioni brevi di strutture ricettive (hotel, B&B). Utilizzando tecniche di Machine Learning, 
il sistema classifica ogni recensione nel reparto più pertinente (Housekeeping, Reception, F&B) e ne valuta il sentiment (positivo/negativo). L’obiettivo è facilitare la gestione delle recensioni, 
velocizzare le risposte e migliorare l’efficienza operativa, partendo da un dataset sintetico e privilegiando chiarezza e riproducibilità del codice.


Contenuti del repository:
- app.py -> script principale;
- functions.py -> contenitore di funzioni;
- preprocessing.py -> funzione di preprocessing del testo;
- reglog.py -> modello di regressione logica utilizzato offline per creare i file .pkl;
- datasetliv1.csv -> dataset completo con 1600 recensioni;
- datasetliv1_preprocessed_LSW.csv -> dataset completo preprocessato con lemmatizzazione e rimozione stopword, utilizzato per training 100% per analisi recensione singola;
- clf_dept_LSW.pkl; clf_sent_LSW.pkl; tfidf_vectorizer_LSW.pkl -> file pkl ottenuti con training 100% su datasetliv1_preprocessed.csv;
- datasetliv1_preprocessed.csv -> dataset con split 80/20 preprocessato senza lemmatizzazione e senza rimozione stopword, utilizzato per training per analisi batch;
- dataset_test20_42.csv -> dataset composto dal 20% di datasetliv1.csv preprocessato senza lemmatizzazione né senza rimozione stopword per analisi batch;
- clf_dept_80.pkl; clf_sent_80.pkl; tfidf_vectorizer_80.pkl -> file pkl ottenuti con training su datasetliv1_preprocessed.csv per test su dataset_test20_42.csv


Requisiti: versioni di Python e librerie necessarie.
Linguaggio di programmazione: Python ver. 3.14;
Librerie esterne:
- Streamlit: interfaccia web interattiva
- Pandas: gestione file .csv
- Scikit-learn: metriche di controllo
- Spacy: Natural Language Processing
- Joblib: oggetti Python complessi
- Plotly: grafici interattivi;
Ambienti di sviluppo:
- Anaconda Navigator
- Jupyter Notebook
- PyCharm


Installazione ed esecuzione:
L’applicazione è disponibile online e funzionante su Render https://pwrechotel.onrender.com/;

Se si vuole invece eseguire il codice localmente per scopi di sviluppo o modifica, è necessario:
1. Installare Python 3.8 o superiore.
2. Creare un ambiente virtuale (ad esempio con Conda o venv).
3. Installare le librerie necessarie usando il file requirements.txt con il comando: pip install -r requirements.txt
4. Scaricare il modello linguistico italiano di spaCy con: python -m spacy download it_core_news_sm
5. Avviare l’applicazione con: streamlit run app.py


Funzionalità principali:
L'applicazione permette di analizzare recensioni hotel, classificandole per reparto e sentiment usando modelli di machine learning. L'algoritmo utilizzato per l'analisi delle singole recensioni 
è stato addestrato sul 100% di un dataset di circa 1600 recensioni e fa uso di lemmatizzazione e rimozione delle stopword (modello avanzato).
Il sistema è attualmente addestrato a riconoscere recensioni di reparto Housekeeping, F&B e Reception e ogni recensione dovrebbe essere monotematica e non ambigua per garantire una classificazione affidabile.
Se il modello non è sufficientemente sicuro della classificazione, scatta la clausola di Indecision e si richiede l’intervento umano per la decisione finale.
E' anche possibile visualizzare e processare un dataset a scopo di test; in questo caso, l'algoritmo utilizzato per l'analisi è stato ottenuto con split 80/20 sul dataset di addestramento e non fa uso 
di lemmatizzazione e rimozione delle stopword (modello standard). Al termine dell'analisi vengono presentate metriche di controllo per Accuracy, F1 e Confusion Matrix.
Infine, è possibile caricare un proprio dataset per sottoporlo ad analisi e visualizzare/scaricare i risultati. Il file da processare deve essere in formato CSV con separatore | (pipe) e contenere almeno 
le colonne body, department e sentiment ( body|department|sentiment )


Link utili:
Repository GitHub: https://github.com/idseth/pwrechotel
Applicazione: https://pwrechotel.onrender.com/


Contatti:
Progetto di tesi per corso di laurea in Informatica per le aziende digitali; 
Anno accademico 2025/2026;
A cura di Ignazio Di Sarno, idseth@hotmail.com
