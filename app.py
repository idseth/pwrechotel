import functions
import pandas as pd         # Per gestire i file .csv
import datetime             # Per gestire il timestamp dei file .csv in download.
import re
import io                   # Per gestire operazioni di input/output, in particolare per lavorare con flussi di dati
                            # in memoria (come file virtuali). Usato per creare un buffer in memoria (io.BytesIO())
                            # dove scrivere il CSV dei risultati prima di offrirlo al download tramite Streamlit.
                            # Questo evita di dover salvare un file fisico sul disco e permette di gestire il file
                            # in modo efficiente e temporaneo.

import streamlit as st      # Permette di creare rapidamente interfacce web interattive per applicazioni di data
                            # science e machine learning, senza dover scrivere codice HTML, CSS o JavaScript.
                            # Streamlit applica uno stile predefinito (font, colore, dimensione, allineamento)
                            # che non è direttamente modificabile tramite parametri. Per personalizzazioni
                            # più dettagliate occorre usare st.markdown() con codice HTML e CSS inline.

from preprocessing import preprocessing_text        # Funzione di pre-processing


st.title("Analisi recensioni hotel: reparto e sentiment")

user_input = st.text_area("Inserisci la recensione da analizzare:", height=150, max_chars=1000)
# Crea un input di testo per inserire una recensione, con altezza del box 150 pixel e 1000 caratteri massimi.
# Streamlit gestisce il testo inserito dall'utente come semplice stringa, senza interpretazione o esecuzione.
# La larghezza del box non è modificabile; è gestita da Streamlit in modo reattivo e si adatta automaticamente
# alla larghezza disponibile nella pagina o nella colonna in cui è inserito.



if st.button("Analizza"):
    if user_input.strip() == "":
        st.warning("Per favore, inserisci una recensione.")
    else:
        functions.salva_testo_utente(user_input)
        preprocessed_text = preprocessing_text(user_input)
        st.write(f"**Testo preprocessato:** {preprocessed_text}")
        dept, dept_conf, sent, sent_conf = functions.predict_single(preprocessed_text)

        # Visualizzazione reparto
        if dept == "Indecision":
            conf_text = ", ".join([f"{c[0]}: {c[1]:.2f}" for c in dept_conf])       # list comprehension
            st.markdown(f"**Reparto previsto:** <span style='color:red; font-weight:bold;'>Indecision</span> ({conf_text})", unsafe_allow_html=True)
        else:
            st.write(f"**Reparto previsto:** {dept} (confidenza: {dept_conf[0][1]:.2f})")

        # Visualizzazione sentiment
        if sent == "Indecision":
            conf_text_sent = ", ".join([f"{c[0]}: {c[1]:.2f}" for c in sent_conf])
            st.markdown(f"**Sentiment previsto:** <span style='color:red; font-weight:bold;'>Indecision</span> ({conf_text_sent})", unsafe_allow_html=True)
        else:
            st.write(f"**Sentiment previsto:** {sent} (confidenza: {sent_conf[0][1]:.2f})")


with st.expander("Info / Readme: Analisi singola recensione"):
    st.write("""
    Questa applicazione permette di analizzare recensioni hotel, classificandole per reparto e sentiment usando modelli 
    di machine learning. L'algoritmo utilizzato per l'analisi delle singole recensioni è stato addestrato sul 100% di un 
    dataset di circa 1600 recensioni e fa uso di lemmatizzazione e rimozione delle stopword (modello avanzato).  
    Il sistema è attualmente addestrato a riconoscere recensioni di reparto **Housekeeping**, **F&B** e **Reception**
    e ogni recensione dovrebbe essere monotematica e non ambigua per garantire una classificazione affidabile.  
    Se il modello non è sufficientemente sicuro della classificazione, scatta la clausola di **Indecision** e si richiede 
    l’intervento umano per la decisione finale.  
    """)


#st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)  # aggiunge spazio
st.write("---")

st.header("Analisi batch su dataset di test predefinito")

with st.expander("Info / Readme: Analisi su dataset di test"):
    st.write("""
    E' anche possibile visualizzare e processare un dataset a scopo di test; in questo caso, l'algoritmo utilizzato per 
    l'analisi è stato ottenuto con split 80/20 sul dataset di addestramento e non fa uso di lemmatizzazione e rimozione 
    delle stopword (modello standard). Al termine dell'analisi vengono presentate metriche di controllo per Accuracy, 
    F1 e Confusion Matrix.
    """)

if st.button("Visualizza dataset di test"):
    df_test = functions.carica_dataset_test()
    df_test.index = df_test.index + 1
    st.write("Contenuto del dataset di test (20% del dataset di training):")
    styled_df2 = df_test.drop(columns=['id','preprocessed_body'])
    st.dataframe(styled_df2)


if st.button("Analizza dataset di test"):
    st.write("Risultati dell'analisi batch sul dataset di test:")

    df_test = functions.carica_dataset_test()       # Crea dataframe con i valori di dataset_test20_42.csv

    preds = df_test['preprocessed_body'].apply(lambda x: functions.predict_batch(x))
    # preds è una Serie di Pandas i cui elementi sono tuple (collezione ordinata di valori) che sfrutta il metodo
    # .apply() di Pandas, che internamente itera su ogni elemento della colonna preprocessed_body.
    # Dopo l'invocazione della funzione lambda, la variabile preds conterrà una Serie in cui ogni elemento è una tupla
    # con 4 valori, corrispondenti al risultato della funzione predict_batch applicata a ciascun testo preprocessato
    # della colonna preprocessed_body (department_pred, department_confidences, sentiment_pred, sentiment_confidences)

    df_test['department_pred'] = preds.apply(lambda x: x[0])                            # Funzioni lambda che prendono i 4 valori delle tuple
    df_test['department_conf'] = preds.apply(lambda x: functions.format_confidence_values_only(x[1]))   # nella serie preds e aggiungono i rispettivi campi al
    df_test['sentiment_pred'] = preds.apply(lambda x: x[2])                                             # dataframe df_test
    df_test['sentiment_conf'] = preds.apply(lambda x: functions.format_confidence_values_only(x[3]))

    # 'department_conf' e 'sentiment_conf' contengono dati complessi poiché sono liste di tuple, dove ogni tupla
    # rappresenta una classe e la sua probabilità associata, ad esempio [("F&B", np.float64(0.80))]
    # Questo tipo di struttura dati (lista di tuple con tipi numpy) non è un tipo semplice come numeri o stringhe,
    # ma un oggetto complesso che Pandas e Streamlit non riescono a convertire direttamente in formato tabellare per la
    # visualizzazione, causando l’errore ArrowTypeError. Per essere visualizzati correttamente è necessario estrarre
    # la parte numerica come fatto con format_conf_no_label

    df_test.index = df_test.index + 1   # fa partire il campo id da 1 invece che da 0

    cols_order = ['title', 'body', 'department', 'sentiment', 'preprocessed_body',
        'department_pred', 'department_conf', 'sentiment_pred', 'sentiment_conf']

    styled_df = df_test[cols_order].style.apply(functions.highlight_errors, axis=1)
    # Il metodo .style in Pandas serve a creare un oggetto "Styler" che permette di applicare formattazioni visive e
    # stili personalizzati alle celle di un DataFrame quando viene mostrato, ad esempio, in un ambiente interattivo
    # come Jupyter Notebook o Streamlit. Consente di:
    # evidenziare celle con colori di sfondo o testo in base a condizioni (es. errori, valori fuori soglia);
    # applicare formattazioni condizionali (colori, font, grassetto) ecc;
    # Il parametro axis=1 nel metodo .apply() di un DataFrame Pandas indica che la funzione passata a .apply() deve
    # essere applicata riga per riga. Con axis=0, la funzione viene applicata colonna per colonna:

    st.dataframe(styled_df)

    functions.mostra_metriche(df_test['department'], df_test['department_pred'], df_test['sentiment'], df_test['sentiment_pred'])

    st.session_state['df_test'] = df_test       # salva in session_state; fondamentale per poter visualizzare il button
                                                # per il download del report analizzato



if 'df_test' in st.session_state:               # Mostra il bottone di download solo se il dataframe è in session_state
    df_test = st.session_state['df_test']
    now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'predizioni_test_{now}.csv'

    csv_buffer = io.StringIO()      # Crea un contenitore temporaneo in memoria per il contenuto CSV, che poi viene
                                    # passato a Streamlit per il download, senza scrivere file fisici. Evita operazioni
                                    # di I/O su disco, più lente e soggette a permessi.

    df_test.to_csv(csv_buffer, index=False, sep='|', encoding='utf-8')    # Usa to_csv direttamente con StringIO
    csv_data = csv_buffer.getvalue()    # Il contenuto del buffer viene recuperato come stringa con csv_buffer.getvalue()

    st.download_button(
        label='Scarica file CSV del test',
        data=csv_data,
        file_name=filename,
        mime='text/csv'
    )

#with st.expander("Info / Readme"):
#    st.write("""
#    Questa applicazione permette di analizzare recensioni hotel,
#    classificandole per reparto e sentiment usando modelli ML.
#    Puoi incollare una recensione e vedere subito il risultato.
#    """)

st.markdown("<div style='margin-top:40px'></div>", unsafe_allow_html=True)  # aggiunge spazio
st.write("---")

uploaded_file = st.file_uploader('Carica un file CSV con recensioni', type=['csv'])
if uploaded_file is not None:
    max_file_size = 5 * 1024 * 1024 # 5 MB
    if uploaded_file.size > max_file_size:
        st.error("Il file è troppo grande. Limite massimo: 5 MB.")
    else:
        try:
            df = pd.read_csv(uploaded_file, sep='|')
        except Exception as e:
            st.error(f"Errore nel caricamento del file CSV: {e}")
        else:
            required_cols = ['body', 'department', 'sentiment']
            if not all(col in df.columns for col in required_cols):
                st.error(f"Il file CSV deve contenere le colonne obbligatorie: {', '.join(required_cols)}.")
            else:
                max_rows = 10000
                if len(df) > max_rows:
                    st.error(f"Il file contiene troppe righe (max {max_rows}).")
                else:
                    def remove_html_tags(text):
                        clean = re.compile('<.*?>')
                        return re.sub(clean, '', text)

                    df['body'] = df['body'].astype(str).apply(remove_html_tags).str.slice(0, 1000)


                    df['preprocessed_body'] = df['body'].apply(lambda x: preprocessing_text(x))
                    preds = df['preprocessed_body'].apply(lambda x: functions.predict_batch(x))
                    df['department_pred'] = preds.apply(lambda x: x[0])
                    df['department_conf'] = preds.apply(lambda x: functions.format_confidence_values_only(x[1]))
                    df['sentiment_pred'] = preds.apply(lambda x: x[2])
                    df['sentiment_conf'] = preds.apply(lambda x: functions.format_confidence_values_only(x[3]))
                    # Richiama la funzione format_confidence_values_only per estrapolare solo i valori numerici ed evitare la
                    # ripetizione dell'etichetta nel dataframe che è già richiamata in department_pred e sentiment_pred

                    st.write("Risultati dell'analisi batch:")
                    df.index = df.index + 1

                    cols_to_keep = ['body', 'department', 'sentiment', 'department_pred', 'department_conf', 'sentiment_pred',
                                    'sentiment_conf']
                    df = df[[col for col in cols_to_keep if col in df.columns]]     # Elimino eventuali campi non necessari

                    styled_df = df[cols_to_keep].style.apply(functions.highlight_errors, axis=1)
                    st.dataframe(styled_df)

                    functions.mostra_metriche(df['department'], df['department_pred'], df['sentiment'], df['sentiment_pred'])

                    st.session_state['df_uploaded'] = df


with st.expander("Info / Readme: Caricamento e analisi dataset personalizzato"):
    st.write("""
    Infine, è possibile caricare un proprio dataset per sottoporlo ad analisi e visualizzare/scaricare i risultati.
    Il file da processare deve essere un file CSV con separatore | (pipe) e contenere almeno le colonne body, department e sentiment
    """)


if 'df_uploaded' in st.session_state:                           # l’export è diretto perché i campi di confidenza sono
    df_uploaded = st.session_state['df_uploaded']               # già formattati come stringhe, mentre nel blocco test
    now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')     # la formattazione in export perché i dati sono ancora
    filename = f'predizioni_upload_{now}.csv'                   # in forma di liste di tuple.

    csv_buffer = io.StringIO()
    df_uploaded.to_csv(csv_buffer, index=False, sep='|', encoding='utf-8')
    csv_data = csv_buffer.getvalue()

    st.download_button(
        label='Scarica file CSV analizzato',
        data=csv_data,
        file_name=filename,
        mime='text/csv'
    )

