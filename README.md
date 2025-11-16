# 🪙 Coin Year Regression – Deep Learning & MLOps Project

Modello di **deep learning** basato su immagini **fronte/retro** per prevedere l’anno di conio delle monete antiche.  
Pipeline completa sviluppata su **Databricks**, con tracking esperimenti tramite **MLflow**, deploy tramite **Model Serving**, e interfaccia di inferenza tramite **Streamlit**.

---

# 🎯 Obiettivo

Sviluppare un sistema automatizzato che analizzi due immagini della stessa moneta (fronte e retro) e predica l’anno di conio attraverso un modello di regressione basato su **ResNet18** con doppio input.

---

# 🔍 Notebook Completo

Il **notebook principale** contenente:

- Esplorazione dataset (EDA)  
- Preprocessing immagini  
- Definizione del modello  
- Training + Validazione  
- MLflow Tracking  
- Inferenza

si trova qui:

➡️ **`notebooks/Coin_Regression_Pipeline.ipynb`**

Questo notebook documenta l’intero workflow end-to-end.

---

# 🧠 Architettura del Modello

- Base: **ResNet18** pre-addestrata su ImageNet  
- Architettura dual-input:
  - ResNet18 per il lato *fronte*
  - ResNet18 per il lato *retro*
- Concatenazione feature → Fully Connected finale  
- Task: Regressione sull’anno di conio  

📌 Implementazione: `src/model.py`

---

# ⚙️ Pipeline di Addestramento

### ✔️ Preprocessing
- Resize 224×224  
- Normalizzazione  
- Data augmentation (opzionale)

### ✔️ Training
- Ottimizzatore: **Adam**  
- Loss: **MAE** (Mean Absolute Error)  
- Valutazione con **K-Fold cross-validation**

### ✔️ Tracking Esperimenti
Tramite **MLflow**:
- Modelli
- Metriche
- Parametri
- Artifact

### ✔️ Metriche principali
- **MAE**
- MSE
- R²

📊 *Esempio:* MAE finale ≈ **21 anni**  


---

# 🚀 Deployment & Serving

Il modello viene:

1. Registrato in **MLflow Model Registry**  
2. Pubblicato tramite **Databricks Model Serving**  
3. Chiamato tramite **REST API**

### Esempio richiesta API:

```json
{
  "inputs": [
    {
      "front_image_base64": "...",
      "back_image_base64": "..."
    }
  ]
}
