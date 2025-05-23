from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import payment, send_visa_router  # ⬅️ Import ici

app = FastAPI(title="API Paiement Visa & Mastercard")

# ✅ Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Route de test HEAD/GET
@app.get("/", include_in_schema=False)
async def root():
    return {"status": "ok"}

# ✅ Inclusion des routers APRES déclaration de `app`
app.include_router(payment.router, prefix="/pay", tags=["Paiement"])
app.include_router(send_visa_router.router)  # ⬅️ C’est ici que l’erreur venait

