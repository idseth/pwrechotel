# Usa un'immagine base Python ufficiale con build tools
FROM python:3.10-slim

# Aggiorna e installa build-essential e altri pacchetti necessari
RUN apt-get update && apt-get install -y build-essential

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file requirements.txt e installa le dipendenze Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m spacy download it_core_news_sm

# Copia tutto il codice nel container
COPY . .

# Comando per avviare l'app Streamlit
CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]
