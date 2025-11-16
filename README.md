# 🪙 Coin Year Regression – End-to-End MLOps System on Databricks

Questo progetto implementa un sistema completo di Computer Vision e MLOps per prevedere l’anno di conio di una moneta antica partendo da due immagini (fronte e retro).  
Il sistema utilizza l’intera piattaforma Databricks: Model Serving, MLflow, Model Registry, Jobs per il retraining, DBFS per il logging, e un frontend Streamlit.

---

# 🎯 Obiettivo

Costruire un sistema scalabile, automatico e affidabile per:

- ricevere due immagini (front/back)  
- eseguire inferenza in tempo reale tramite Model Serving  
- registrare dati per monitoraggio e retraining  
- aggiornare automaticamente il modello tramite pipeline schedulate  

---

# 🧩 Architettura End-to-End

Il flusso completo del sistema è il seguente:

### 1. Front-End (Streamlit)
- L’utente carica due immagini (fronte e retro).
- Le immagini vengono convertite in Base64.
- Viene inviata una richiesta JSON all’API REST.

### 2. Databricks Gateway (Endpoint REST)
- Riceve la richiesta HTTP POST.
- Inoltra le immagini al modello in produzione.
- Gestisce risposta ed eventuali errori.

### 3. Model Serving
- Esegue inferenza in tempo reale.
- Utilizza la versione più recente del modello in “Production”.
- Restituisce l’anno di conio previsto.

### 4. DBFS Logging (opzionale ma consigliato)
Il sistema salva:
- immagini in Base64  
- predizione  
- timestamp  
- versione modello  
- eventuali metadati  

Questi dati alimentano:  
- monitoraggio  
- analisi qualità  
- dataset per retraining  

### 5. Retraining Pipeline (Databricks Jobs)
Un job schedulato:
- legge i nuovi dati da DBFS  
- prepara il dataset aggiornato  
- esegue preprocessing e cleaning  
- allena un nuovo modello  
- registra il tutto su MLflow  

### 6. Validazione Automatica
Il nuovo modello viene confrontato con quello in produzione:
- se le metriche sono **migliori** → viene promosso  
- se sono **peggiori** → viene scartato  

### 7. MLflow Model Registry
- Versionamento automatico dei modelli.
- Gestione degli stage:
  - None  
  - Staging  
  - Production  
- Rollback immediato in caso di errori.

### 8. Aggiornamento del Model Serving
- Quando un modello viene promosso a “Production”, il serve endpoint utilizza automaticamente la nuova versione.
- Nessun downtime.

### 9. Inferenza tramite API
L’interfaccia utente riceve il risultato in tempo reale e lo visualizza.

---

# 🧠 Modello di Deep Learning

Il sistema utilizza un modello dual-input basato su PyTorch.

### Backbone disponibili:
- ResNet18  
- MobileNetV3 Small  

### Due modalità architetturali:
- **Dual Backbone**  
  - una CNN per fronte  
  - una CNN per retro  

- **Shared Backbone**  
  - una sola CNN condivisa per entrambi i lati  

### Feature Fusion:
- concatenazione  
- projection layer opzionale  

### Output:
- regressione (anno di conio)

---

# 📓 Notebook

Notebook completo della pipeline tecnica:

`notebooks/Coin_Regression_Pipeline.ipynb`

Include:
- EDA  
- preprocessing  
- configurazione modello  
- training  
- K-Fold  
- analisi risultati  
- inferenza  

---

# 📚 Documentazione Tecnica (cartella /docs)

- **architecture.md** → architettura completa Databricks  
- **pipeline.md** → pipeline end-to-end (data → model → deploy)  
- **api_schema.md** → specifica tecnica dell’API REST  
- architecture.png → schema visivo (in arrivo)

---

# 📡 Schema API 

### Input:

{
  "inputs": [
    {
      "front_image_base64": "stringa_base64",
      "back_image_base64": "stringa_base64"
    }
  ]
}

### Output:
{
  "predictions": [ anno_predetto ]
}

### 🛠️ Stack Tecnologico
- Machine Learning
- PyTorch
- torchvision
- numpy
- pandas
- MLOps (Databricks)
- MLflow
- Model Registry
- Databricks Workflows (Jobs)
- Model Serving
- DBFS
### Front-end & API
- Streamlit
- REST API (JSON Base64)
### 🚀 Flusso di Inferenza
L’utente carica le due immagini
Streamlit invia la richiesta JSON al Model Serving
Il modello restituisce l’anno previsto
La UI mostra la predizione

