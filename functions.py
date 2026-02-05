import joblib               # Per salvare e caricare oggetti Python complessi in modo efficiente, come modelli di
                            # machine learning addestrati da file .pkl (pickle), così da non doverli riaddestrare
                            # ogni volta che si avvia l’app. Fondamentale per la persistenza e il riutilizzo dei
                            # modelli ML nel prototipo.
import streamlit as st
import pandas as pd
import datetime
import plotly.figure_factory as ff
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix      # Metriche di controllo



# Il decoratore @st.cache_data si applica solo alla funzione immediatamente successiva a cui è anteposto e serve a far
# sì che la lettura avvenga una sola volta per sessione o fino a quando il file o la funzione non cambiano.
# Quando l’utente esegue più azioni in app.py, i file .pkl non vengono ricaricati da disco ogni volta; Streamlit usa
# la versione in cache, rendendo l’operazione più veloce.
@st.cache_resource
def carica_modelli_single():         # Modello per singole recensioni: training 100%, lemmatizzazione e stopword (LSW)
    vectorizer = joblib.load('tfidf_vectorizer_LSW.pkl')      # Carica il vettorizzatore TF-IDF usato per trasformare
                                                              # il testo in una rappresentazione numerica.
    clf_dept = joblib.load('clf_dept_LSW.pkl')      # Carica in memoria il modello di classificazione per il reparto.
    clf_sent = joblib.load('clf_sent_LSW.pkl')      # Carica in memoria il modello di classificazione per il sentiment.
    return vectorizer, clf_dept, clf_sent


# Utilizzata per analizzare singole recensioni
def predict_single(text):
    vectorizer, clf_dept, clf_sent = carica_modelli_single()
    X = vectorizer.transform([text])                    # Trasforma il testo con il vettorizzatore caricato

    # Reparto
    dept_probs = clf_dept.predict_proba(X)[0]           # Metodo standard dei classificatori scikit-learn che, dato un
                                                        # insieme di esempi X, restituisce per ciascun esempio un array
                                                        # con le probabilità stimate di appartenenza a ciascuna classe.
    sorted_dept_indices = dept_probs.argsort()[::-1]    # Restituisce un array di indici che ordinano l’array dept_probs
                                                        # in ordine decrescente di valore [::-1]
    max_dept_prob = dept_probs[sorted_dept_indices[0]]  # Estrae la probabilità più alta stimata dal modello per il
                                                        # reparto, corrispondente alla classe più probabile.

    second_dept_prob = dept_probs[sorted_dept_indices[1]]        # Estrae dal vettore la seconda classe più probabile.
    max_class = clf_dept.classes_[sorted_dept_indices[0]]        # Estrae la prima etichetta più probabile
    second_class = clf_dept.classes_[sorted_dept_indices[1]]     # e la seconda

    if max_dept_prob < 0.5 or (max_dept_prob - second_dept_prob) < 0.1:    # Gestione delle ambiguità.
        dept_pred = "Indecision"
        dept_confidences = [(max_class, max_dept_prob), (second_class, second_dept_prob)]
    else:
        dept_pred = max_class
        dept_confidences = [(max_class, max_dept_prob)]

    # Sentiment
    sent_probs = clf_sent.predict_proba(X)[0]                   # Stessa logica utilizzata per il reparto
    sorted_sent_indices = sent_probs.argsort()[::-1]
    max_sent_prob = sent_probs[sorted_sent_indices[0]]
    max_sent_class = clf_sent.classes_[sorted_sent_indices[0]]
    if max_sent_prob < 0.55:
        sent_pred = "Indecision"
        sent_confidences = [(max_sent_class, max_sent_prob)]
    else:
        sent_pred = max_sent_class
        sent_confidences = [(max_sent_class, max_sent_prob)]

    return dept_pred, dept_confidences, sent_pred, sent_confidences


@st.cache_resource
def carica_modelli_batch():                               # Modello per analisi file .csv, con training 80% del dataset,
    vectorizer = joblib.load('tfidf_vectorizer_80.pkl')   # senza lemmatizzazione e senza rimozione delle stopword
    clf_dept = joblib.load('clf_dept_80.pkl')
    clf_sent = joblib.load('clf_sent_80.pkl')
    return vectorizer, clf_dept, clf_sent


@st.cache_data
def carica_dataset_test():
    return pd.read_csv("C:/Users/idset/Desktop/UniPegaso/Project work/dataset_test20_42.csv", sep='|')


def predict_batch(text):
    vectorizer, clf_dept, clf_sent = carica_modelli_batch()
    X = vectorizer.transform([text])

    # Predizione reparto
    dept_probs = clf_dept.predict_proba(X)[0]
    dept_pred = clf_dept.classes_[dept_probs.argmax()]
    dept_confidences = [(dept_pred, dept_probs.max())]
    # Predizione sentiment
    sent_probs = clf_sent.predict_proba(X)[0]
    sent_pred = clf_sent.classes_[sent_probs.argmax()]
    sent_confidences = [(sent_pred, sent_probs.max())]
    return dept_pred, dept_confidences, sent_pred, sent_confidences


def highlight_errors(row):
    styles = []
    for col in row.index:
        if col == 'department_pred':
            if row['department_pred'] != row['department']:
                styles.append('background-color: #ffcccc')
            else:
                styles.append('')
        elif col == 'sentiment_pred':
            if row['sentiment_pred'] != row['sentiment']:
                styles.append('background-color: #ffcccc')
            else:
                styles.append('')
        else:
            styles.append('')
    return styles






def confusion_matrix_plotly(y_true, y_pred, labels, title):
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    fig = ff.create_annotated_heatmap(
        z=cm,
        x=labels,
        y=labels,
        colorscale='Blues',
        showscale=True,
        reversescale=True
    )
    #fig.update_layout(title_text=title, title_x=0)  # Allineamento titolo (0 = sx; 0.5 = cx, 1 = dx)
    fig.update_xaxes(title_text='Predetto')
    fig.update_yaxes(title_text='Reale')
    st.plotly_chart(fig)

def mostra_metriche(y_dept_test, y_dept_pred, y_sent_test, y_sent_pred):
    labels_dept = sorted(list(set(y_dept_test)))
    labels_sent = sorted(list(set(y_sent_test)))

    st.markdown('<span style="font-weight:bold; font-size:20px;">Classificazione reparto:</span>', unsafe_allow_html=True)
    st.write("Accuracy:", accuracy_score(y_dept_test, y_dept_pred))
    st.write("F1 macro:", f1_score(y_dept_test, y_dept_pred, average='macro'))
    st.write("Confusion Matrix:")
    confusion_matrix_plotly(y_dept_test, y_dept_pred, labels_dept, "")  # "" = titolo; obbligatorio ma passato vuoto in questo caso

    st.markdown('<span style="font-weight:bold; font-size:20px;">Classificazione sentiment:</span>', unsafe_allow_html=True)
    st.write("Accuracy:", accuracy_score(y_sent_test, y_sent_pred))
    st.write("F1 macro:", f1_score(y_sent_test, y_sent_pred, average='macro'))
    st.write("Confusion Matrix:")
    confusion_matrix_plotly(y_sent_test, y_sent_pred, labels_sent, "")



def format_confidence_values_only(conf_list):
    return ", ".join([f"{prob:.2f}" for cls, prob in conf_list])
# List comprehension (metodo compatto per creare una lista).
# Per ogni elemento di conf_list (che è una tupla "cls, prob"), la list comprehension estrae prob;
# f"{prob:.2f}" è una f-string che formatta il numero prob come una stringa con 2 cifre decimali;
# join è un metodo delle stringhe che concatena tutti gli elementi di una lista di stringhe.


def format_confidence_list(conf_list):
    return ", ".join([f"{cls}: {prob:.2f}" for cls, prob in conf_list])
# serve a trasformare in modo semplice e leggibile una lista di coppie (classe, probabilità) in una stringa di testo
# Riceve in input una lista di confidenze, ad esempio: [("Housekeeping", 0.85), ("Reception", 0.10)]
# Converte ogni coppia in una stringa formattata tipo "Housekeeping: 0.85"
# Unisce tutte queste stringhe in un’unica stringa separata da virgole, ad esempio: "Housekeeping: 0.85, Reception: 0.10"
# questo permette di visualizzare i dati correttamente in un’interfaccia come Streamlit, che non gestisce bene
# strutture dati complesse come liste di tuple.
# PyArrow è una libreria software open source che fornisce un formato di memoria colonnare e strumenti per la gestione
# efficiente di dati tabellari, specialmente per l’interoperabilità tra diversi sistemi di elaborazione dati. In pratica,
# PyArrow permette di rappresentare e trasferire dati strutturati (come DataFrame di pandas) in modo molto veloce e compatto,
# facilitando operazioni come la serializzazione, la lettura/scrittura di file, e l’interscambio tra linguaggi (Python, C++, Java, ecc.).
# Nel contesto di Streamlit, PyArrow viene usato internamente per convertire i DataFrame pandas in un formato che può
# essere trasmesso e visualizzato nell’interfaccia web. Quando Streamlit chiama st.dataframe(), PyArrow converte il
# DataFrame in un formato colonnare ottimizzato per la trasmissione e il rendering. Se il DataFrame contiene tipi di
# dati complessi o non supportati (come liste di tuple), PyArrow genera errori di conversione, come quello che hai visto.
# In sintesi, PyArrow è la tecnologia che permette a Streamlit di mostrare tabelle di dati in modo efficiente, ma
# richiede che i dati siano in formati semplici e standard (numeri, stringhe, booleani) per funzionare correttamente.


def highlight_indecision(val):
    if val == "Indecision":
        return 'color: red; font-weight: bold'
    return ''



# In Python, aprire un file in modalità append crea il file se non esiste, oppure apre il file esistente senza cancellarne il contenuto.
# Quindi, alla prima invocazione, se il file non esiste, viene creato automaticamente.
# Alle invocazioni successive, il file viene aperto e i nuovi dati vengono aggiunti in coda, senza sovrascrivere il contenuto precedente.
# Questo meccanismo è gestito internamente da Python e non serve specificarlo nel codice.
# testo.replace('|', ' ')
# Sostituisce ogni occorrenza del carattere pipe | con uno spazio.
# Questo è importante perché il pipe viene usato come separatore di campo nel file di log (formato IP|data&ora|testo), quindi se il testo contenesse pipe, romperebbe la struttura del file.
# .replace('\n', ' ')
# Sostituisce ogni carattere di nuova linea (line break, \n) con uno spazio.
# Serve a evitare che il testo contenga interruzioni di riga che spezzerebbero la riga di log in più righe, compromettendo la leggibilità e la parsabilità del file.
# .replace('\r', ' ')
# Sostituisce ogni carattere di ritorno a capo \r (usato in alcuni sistemi operativi come parte della nuova linea) con uno spazio, per lo stesso motivo del punto precedente.
# .strip()  Rimuove eventuali spazi bianchi iniziali e finali residui dopo le sostituzioni, per avere un testo pulito e senza spazi superflui ai bordi.
# ip_str = ip if ip is not None else 'unknown'
# è un costrutto specifico di Python chiamato operatore ternario o conditional expression. Non è un ciclo if, ma un modo compatto per scrivere una condizione if-else in una sola riga.
# with apre il file in modalità append ('a') e assegna l’handle a f.
# Quando il blocco with termina (anche se si verifica un errore), il file viene chiuso automaticamente.
# Questo evita problemi come file lasciati aperti, che possono causare perdite di memoria o blocchi di scrittura.
def salva_testo_utente(testo, ip=None, log_file='log_recensioni.txt'):
    testo_sanitizzato = testo.replace('|', ' ').replace('\n', ' ').replace('\r', ' ').strip()       # sanitization
    timestamp = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')  # data e ora corrente in formato ISO
    ip_str = ip if ip is not None else 'unknown'                                # Se IP non fornito, usa 'unknown'
    riga_log = f"{ip_str}|{timestamp}|{testo_sanitizzato}\n"                    # Costruisci la riga da salvare
    with open(log_file, 'a', encoding='utf-8') as f:                            # Scrivi in append nel file di log
        f.write(riga_log)

