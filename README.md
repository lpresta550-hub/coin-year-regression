### 🪙 Coin Year Regression – End-to-End MLOps System on Databricks
Questo progetto implementa un sistema completo di Computer Vision e MLOps per prevedere l’anno di conio di una moneta antica a partire da due immagini (fronte e retro).
L’intero flusso – dal preprocessing alla predizione in tempo reale – è gestito tramite l’ecosistema Databricks, con pipeline automatizzate, versionamento dei modelli e deploy tramite Model Serving.
### 🎯 Obiettivo
Creare un sistema affidabile, scalabile e automatizzato che:
riceve due immagini della moneta
esegue inferenza in tempo reale tramite API
salva i dati per il monitoraggio e il retraining
aggiorna automaticamente il modello tramite pipeline schedulate
### 📡 Flusso End-to-End
L’architettura Databricks utilizzata comprende:
UI (Streamlit)
L’utente carica le due immagini.
API REST (Databricks Gateway)
La UI invia una richiesta HTTP al Databricks Model Serving.
Model Serving
Il modello di produzione esegue la predizione.
DBFS Logging
Le richieste possono essere salvate in DBFS:
immagini
risultati
timestamp
versione modello
Retraining Pipeline (Databricks Jobs)
Un job schedulato:
legge i nuovi dati
aggiorna il dataset
esegue preprocessing
allena un nuovo modello
registra tutto su MLflow
Model Registry
Il nuovo modello viene confrontato con quello in produzione:
se migliore → Promozione automatica
se peggiore → rifiutato
Aggiornamento automatico del serve endpoint
Il modello nuovo passa automaticamente in Production.
### 🧠 Modello di Deep Learning
Il sistema usa un’architettura dual-input con backbone selezionabile:
Backbone disponibili:
ResNet18
MobileNetV3 Small
Due modalità:
Dual Backbone – una CNN per fronte e una per retro
Shared Backbone – una sola CNN condivisa
Feature Fusion:
concatenazione
projection layer opzionale
Output:
regressione → anno di conio stimato
### 📓 Notebook Principale
L’intera pipeline tecnica è documentata qui:
➡️ notebooks/Coin_Regression_Pipeline.ipynb
Contiene:
EDA
preprocessing
training
K-Fold
analisi statistica
configurazione backbone
inference
### 🛠️ Documentazione Tecnica
La documentazione è nella directory:
docs/
Contiene:
architecture.md – architettura MLOps completa
pipeline.md – pipeline dettagliata end-to-end
api_schema.md – schema completo dell’API REST

### ⚙️ Tecnologie Utilizzate
Machine Learning
PyTorch
torchvision
numpy
pandas
MLOps & Infrastruttura
Databricks
MLflow
Model Registry
Model Serving
Databricks Jobs
DBFS
Front-end & API
Streamlit
REST API (JSON Base64)
###  Come funziona l’inferenza
L’utente carica le due immagini
Il front-end le converte in Base64
Invio richiesta JSON al Model Serving
Il modello produce l’anno stimato
La UI mostra il risultato
### Esempio Chiamata API
{
  "inputs": [
    {
      "front_image_base64": "stringa_base64",
      "back_image_base64": "stringa_base64"
    }
  ]
}
Output:
{
  "predictions": [ anno_predetto ]
}

