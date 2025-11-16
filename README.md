# Coin Year Regression – Deep Learning su immagini di monete antiche

Progetto di **deep learning** per la previsione dell’anno di conio di monete antiche a partire da immagini **fronte/retro**, con pipeline end-to-end su **Databricks**.

---

## 🎯 Obiettivo

Predire l’anno di conio di una moneta antica utilizzando un modello di deep learning basato su **ResNet18**, sfruttando entrambe le immagini (fronte e retro) come input.

---

## 🧠 Architettura del modello

- Base: **ResNet18** pre-addestrata
- Input: 2 immagini (fronte e retro)
- Pipeline:
  - Preprocessing e normalizzazione delle immagini
  - Estrazione di feature per ciascun lato
  - Fusione delle feature e regressione sull’anno di conio
- Task: **regressione** (predizione anno in valore numerico)

---

## 🧪 Pipeline & Training

- Preprocessing immagini (resize, normalization, data augmentation)
- Split del dataset e **K-Fold cross-validation**
- Metriche di valutazione:
  - Mean Absolute Error (MAE)
  - Altre metriche di supporto (es. MSE, R² se utilizzate)

> 📝 Esempio: *MAE finale ≈ 21 anni (valore indicativo, da aggiornare con i tuoi risultati reali)*

---

## 🛠️ Stack Tecnologico

- **Linguaggi & librerie:**
  - Python, PyTorch, torchvision, NumPy, Pandas
- **MLOps & piattaforma:**
  - Databricks, MLflow, Model Registry, Databricks Jobs, Delta Lake, DBFS
- **Visualizzazione & analisi:**
  - Matplotlib, Seaborn


---

## 🚀 Deploy & Serving

- Salvataggio modello e tracciamento esperimenti con **MLflow**
- Registrazione del modello in **Model Registry**
- Deploy tramite **Databricks Model Serving** con endpoint **REST API**
- Creazione di una semplice **interfaccia Streamlit** per consentire il caricamento delle immagini e la predizione dell’anno

---

## 📂 Struttura del progetto (prevista)

```bash
coin-year-regression/
│
├── src/
│   ├── dataset.py
│   ├── model.py
│   ├── train.py
│   ├── inference.py
│   └── utils.py
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   └── 02_training.ipynb
│
├── docs/
│   ├── architecture.png
│   ├── mlflow_screenshots.png
│   └── streamlit_ui.png
│
└── README.md
