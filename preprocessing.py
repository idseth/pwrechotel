import re  # Per le regular expressions
import spacy  # Per il Natural Language Processing
from spacy.cli import download

try:
    nlp = spacy.load("it_core_news_sm")
except OSError:
    download("it_core_news_sm")
    nlp = spacy.load("it_core_news_sm")


def preprocessing_text(text):
    # La funzione effettua il preprocessing del testo: eliminazione simboli e punteggiatura non consentita,
    # rendendo il testo in minuscolo ed effettuando la tokenizzazione. In più, la funzione elimina spazi multipli, a capo, tabulazioni
    # ed effettua l'escape dei caratteri ammessi (& e spazio singolo) ed equipara "è" a "é" in un unico carattere

    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789èéòàìù& "  # Caratteri ammessi: lettere minuscole a-z, cifre 0-9,
                                                                    # vocali accentate italiane, spazio, &

    text = text.replace('è', 'é').replace('È','É')  # Normalizza le vocali accentate: sostituisce 'è' con 'é', sia per non avere 2 token
                                                    # con lo stesso significato, sia perchè SpaCy include le "è" nell'elenco delle stopword
                                                    # In questo modo, se un utente utilizzasse "è" ci sarebbe perdita di informazione.

    pattern = f"[^{re.escape(allowed_chars)}]"  # Costruisce pattern dei caratteri ammessi ed effettua l'escape dei caratteri speciali
    filtered_text = re.sub(pattern, " ", text.lower())  # Sostituisce i caratteri non ammessi con spazio, applicando lowercasing

    filtered_text = re.sub(r"\s+", " ", filtered_text).strip()
    # Sostituisce tutte le sequenze di spazi bianchi (spazi, tab, newline)
    # con un singolo spazio, normalizzando gli spazi nel testo.
    # .strip() rimuove eventuali spazi bianchi all’inizio o alla fine della stringa

    doc = nlp(filtered_text)
    # Processa il testo con spaCy. nlp è un oggetto modello spaCy che contiene regole, dizionari e algoritmi
    # per analizzare il testo. Esegue il pipeline di elaborazione linguistica sul testo.
    # Il risultato è un oggetto Doc (qui assegnato a doc) che rappresenta il testo analizzato come
    # una sequenza di token con attributi linguistici (es. token.text, token.is_stop, token.lemma_, ecc.)
    # In questo modo è possibile operare facilmente sui vari token per lemmatizzare o eliminare le stopword

    tokens = [token.lemma_ for token in doc if not token.is_stop]  # Effettua il preprocessing lemmatizzando il testo e rimuovendo le stopword

    return " ".join(tokens)