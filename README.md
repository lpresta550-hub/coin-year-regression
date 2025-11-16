# 🪙 Coin Year Regression – Deep Learning & MLOps Project

Modello di **deep learning** basato su immagini **fronte/retro** per prevedere l’anno di conio delle monete antiche.  
Pipeline completa progettata e sviluppata su **Databricks**, con tracking esperimenti tramite **MLflow**, deploy tramite **Model Serving** e interfaccia di inferenza con **Streamlit**.

---

# 🎯 Obiettivo

Sviluppare un sistema automatizzato che analizzi due immagini della stessa moneta (fronte e retro) e predica l’anno di conio tramite un modello di regressione basato su architettura **ResNet18**.

---

# 🧠 Architettura del Modello

- Modello base: **ResNet18** pre-addestrata su ImageNet  
- Approccio multi-input:
  - Una ResNet per il lato *fronte*
  - Una ResNet per il lato *retro*
- Estrazione feature → concatenazione → regressione finale
- Output: anno stimato (valore numerico)

📌 *Architettura implementata in `model.py`.*

---

# ⚙️ Pipeline di Addestramento

### ✔️ Preprocessing
- Resize → 224x224
- Normalizzazione
- Data augmentation 

### ✔️ Training
- Ottimizzatore: **Adam**
- Loss function: **MAE**
- Validazione: **K-Fold cross-validation**
- Tracciamento esperimenti: **MLflow**

### ✔️ Metriche
- **MAE** (Mean Absolute Error)
- **MSE**
- **R²** (se calcolato)

📊 *Esempio: MAE finale ≈ 21 anni*  


---

# 🛠️ Stack Tecnologico

### 🔹 Deep Learning
- PyTorch  
- torchvision  

### 🔹 MLOps
- Databricks  
- MLflow  
- Model Registry  
- Databricks Jobs  
- Model Serving API  

### 🔹 Data & Tools
- Pandas  
- NumPy  
- Pillow  
- Matp
