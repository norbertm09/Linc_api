
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import payment
from routers import send_visa_router
app.include_router(send_visa_router.router)

app = FastAPI(title="API Paiement Visa & Mastercard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
async def root():
    return {"status": "ok"}

app.include_router(payment.router, prefix="/pay", tags=["Paiement"])
