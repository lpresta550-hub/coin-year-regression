# 🪙 Coin Year Regression – Deep Learning & MLOps Project

Modello di **deep learning** basato su immagini **fronte/retro** per prevedere l’anno di conio di monete antiche.  
Il progetto integra architetture CNN avanzate (ResNet18, MobileNetV3), configurazioni RGB/Grayscale, feature projection, cross-validation e pipeline end-to-end su **Databricks** con tracking tramite **MLflow** e deploy tramite **Model Serving**.

---

# 🎯 Obiettivo

Prevedere l’anno di conio di una moneta antica utilizzando due immagini (fronte e retro), sfruttando un modello neurale dual-input completamente configurabile e ottimizzato per compiti di regressione.

---

# 🔍 Notebook Completo 

Il notebook principale contiene l’intera pipeline di lavoro:

✔ Esplorazione del dataset  
✔ Preprocessing + trasformazioni (RGB/Grayscale)  
✔ Configurazione dei parametri globali  
✔ Selezione backbone: **ResNet18** o **MobileNetV3**  
✔ Opzione **shared backbone** per feature sharing  
✔ Feature projection layer personalizzato  
✔ Training loop completo  
✔ **K-Fold Cross Validation**  
✔ Analisi statistica approfondita  
✔ Inferenza del modello  

📄 Notebook completo:  
➡️ **`notebooks/Coin_Regression_Pipeline.ipynb`**

É la documentazione esatta e completa del workflow end-to-end.

---

# 🧠 Architettura del Modello

Il modello supporta due modalità:

### **1️⃣ Dual Backbone ResNet18/MobileNet (Front + Back separati)**  
- Una CNN per il lato *front*  
- Una CNN per il lato *back*  
- Estrazione feature → concatenazione → regressione finale

### **2️⃣ Shared Backbone (opzionale)**  
- Una sola CNN condivisa  
- Le due immagini passano nello stesso backbone  
- Riduzione dei parametri  
- Maggiore regolarizzazione

### **Feature Projection Layer**  
- Layer opzionale che riduce la dimensionalità delle feature  
- Migliora generalizzazione e stabilità del modello

📌 Implementazione: `src/model.py`

---

# ⚙️ Pipeline di Addestramento

### 🔧 Preprocessing
- Resize 128×128  
- Normalizzazione  
- Conversione RGB o Grayscale  
- Augmentation selezionabile  

### 🧪 Training
- Ottimizzatore: **Adam**  
- Loss: **MAE**  
- Scheduler (se abilitato)  
- Training fully configurable via parametri globali  

### 🔁 Validazione
- **K-Fold Cross Validation (5 fold)**  
- Logging delle metriche per ogni fold  

### 📊 Metriche
- MAE (principale)  
- MSE  
- R² (opzionale)  

Esempio MAE finale: **≈ 20–25 anni**  


---

# 🚀 Deployment & Serving

Pipeline MLOps su Databricks:

1. Tracking esperimenti con **MLflow**  
2. Registrazione del modello su **Model Registry**  
3. Deployment tramite **Model Serving**  
4. Inferenza tramite **REST API**  
5. Interfaccia Streamlit per predizione tramite upload immagini

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
