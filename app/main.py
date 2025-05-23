from fastapi import FastAPI
from routers import payment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["https://votre-site.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app = FastAPI(title="API Maître Paiement – Visa & Mastercard")

app.include_router(payment.router, prefix="/pay", tags=["Paiement"])

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API Paiement intégrée Visa & Mastercard"}
