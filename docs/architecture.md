# 🧩 Architettura del Sistema – Coin Year Regression (MLOps su Databricks)

Questa architettura descrive il funzionamento completo del sistema Coin Year Regression, un progetto di deep learning e MLOps completamente integrato in Databricks.  
Il sistema gestisce inferenza real-time, logging, retraining automatico, versionamento del modello e un’interfaccia utente per la predizione.

---

# 1) Panoramica Generale

Il sistema è composto da:

- Interfaccia utente (Streamlit)
- API REST tramite Databricks Model Serving
- Salvataggio dati e logging in DBFS
- Pipeline di retraining automatizzata
- MLflow per tracking e versionamento
- Model Registry per gestione modelli
- Endpoint in produzione senza downtime

---

# 2) Flusso End-to-End

## a) UI → API
- L’utente carica due immagini (fronte e retro).
- L’app Streamlit converte le immagini in Base64.
- Viene inviata una richiesta POST all’endpoint REST.

## b) Databricks Gateway
- Riceve la richiesta HTTP.
- Valida il payload.
- La inoltra al modello in produzione via Model Serving.

## c) Model Serving (Produzione)
- Carica automaticamente la versione del modello in “Production”.
- Esegue inferenza real-time.
- Restituisce l’anno di conio stimato.

## d) Logging in DBFS
Il sistema può salvare:
- immagini in Base64
- predizione
- timestamp
- versione del modello
- eventuali metadati

## e) Retraining Pipeline (Databricks Jobs)
Un job schedulato:
- legge i nuovi dati salvati
- aggiorna il dataset
- esegue preprocessing
- addestra un nuovo modello
- registra parametri, metriche e pesi in MLflow

## f) Validazione Automatica
Il nuovo modello viene confrontato con quello attuale:
- se migliore → promosso
- se peggiore → scartato

## g) Model Registry
- Il modello viene versionato automaticamente.
- Gli stage possibili: None → Staging → Production
- Permette rollback immediati.

## h) Deploy Automatico
- Quando lo stage diventa “Production”, l’endpoint serve automaticamente la nuova versione del modello.
- Nessun downtime.

---

# 3) Componenti Principali

### • Streamlit UI
Gestisce il caricamento delle immagini e visualizza i risultati.

### • Databricks Model Serving
Esegue inferenza immediata.

### • MLflow Tracking
Registra:
- metriche
- parametri
- artifact del modello

### • Model Registry
Gestisce versioni e promozioni.

### • Databricks Jobs
Esegue retraining programmato.

### • DBFS
Memorizza dati per audit e retraining.

---

# 4) Benefici dell'Architettura

- Scalabilità
- Zero downtime
- Automazione completa del retraining
- Versionamento robusto
- Pipeline affidabile e riproducibile
- Integrazione end-to-end in un unico ambiente

---

# 5) Componenti del Modello (breve overview)

- Backbone: ResNet18 o MobileNetV3
- Modalità: Dual backbone o Shared backbone
- Fusion: concatenazione + projection layer (opzionale)
- Output: regressione dell’anno di conio

---

# 6) Conclusione

Questa architettura permette di mantenere un sistema di Computer Vision in produzione in modo professionale, scalabile e completamente automatizzato attraverso Databricks.
