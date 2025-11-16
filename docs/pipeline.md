# 📦 Pipeline End-to-End – Coin Year Regression

Questa pipeline descrive l’intero flusso del progetto, dalla raccolta dei dati fino al deploy del modello su Databricks Model Serving.

---

# 1) Raccolta e Preparazione Dati

- Upload immagini lato front/back
- Validazione file
- Salvataggio in DBFS con timestamp
- Aggiornamento dataset incrementale

---

# 2) Preprocessing

### Trasformazioni applicate:
- Resize 128×128
- Normalizzazione
- RGB o Grayscale (opzionale)
- Data augmentation leggera
- Conversione in tensori

Entrambi i lati subiscono lo stesso preprocessing.

---

# 3) Creazione Dataset

Dataset PyTorch personalizzato:
- Carica immagine front
- Carica immagine back
- Applica preprocessing
- Restituisce tensori + anno di conio

---

# 4) DataLoader

- Batch size configurabile
- Shuffle attivo nel training
- K-Fold cross validation (5-fold)

---

# 5) Training del Modello

Il modello utilizza:
- Backbone: ResNet18 o MobileNetV3
- Dual backbone o shared backbone
- Fusion tramite concatenazione

### Parametri principali:
- Epochs: 20
- Loss: MAE
- Optimizer: Adam
- Learning Rate configurabile

---

# 6) Validazione (K-Fold)

Per ogni fold:
- 4 fold → training
- 1 fold → validation

Metriche calcolate:
- MAE
- MSE
- (opzionale) R²

Il risultato finale è la media delle metriche di tutti i fold.

---

# 7) Logging via MLflow

Per ogni run vengono registrati:
- Parametri
- Metriche
- Artifact (grafici, confusion plots, JSON)
- Modello

---

# 8) Registrazione nel Model Registry

Dopo il training:
- Il modello viene registrato come nuova versione
- Lo stage iniziale è “None”
- Il modello può essere promosso a:
  - Staging
  - Production

---

# 9) Retraining Automatico (Databricks Jobs)

Un job schedulato:
- Legge nuovi dati da DBFS
- Esegue preprocessing
- Ritrena il modello
- Salva nuove versioni su MLflow
- Confronta il nuovo modello con quello attuale

---

# 10) Deploy del Modello

Quando un modello è in “Production”:
- Viene automaticamente utilizzato da Model Serving
- L’endpoint si aggiorna senza downtime

---

# 11) Inferenza

La UI invia una richiesta JSON contenente le due immagini in Base64.  
Il modello produce l’anno previsto e la UI lo visualizza.

---

# 12) Conclusione

La pipeline utilizza un flusso moderno di MLOps che unisce Deep Learning, validazione robusta, monitoraggio continuo e deploy automatizzato su Databricks.
