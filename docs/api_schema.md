# 📡 API Schema – Coin Year Regression

Questo documento definisce la struttura dell’API REST che permette di inviare due immagini (fronte/retro) e ottenere l’anno di conio stimato dal modello.

---

# 1) Endpoint

Metodo: POST  
Content-Type: application/json  
Auth: Bearer Token (Databricks)  
URL: endpoint del Model Serving

---

# 2) Payload di Input

Struttura della richiesta:

Input:
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
