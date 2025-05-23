from fastapi import FastAPI
from routers import payment

app = FastAPI(title="API Maître Paiement – Visa & Mastercard")

app.include_router(payment.router, prefix="/pay", tags=["Paiement"])

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API Paiement intégrée Visa & Mastercard"}