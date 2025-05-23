from fastapi import APIRouter, HTTPException
from schemas.transaction import Transaction
from modules import visa, mastercard

router = APIRouter()

@router.post("/")
def process_payment(transaction: Transaction):
    provider = transaction.provider.lower()
    if provider == "visa":
        return visa.send_funds(transaction.dict())
    elif provider == "mastercard":
        return mastercard.send_funds(transaction.dict())
    else:
        raise HTTPException(status_code=400, detail="Fournisseur non supporté")