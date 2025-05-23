import requests
from typing import Dict

def send_funds(transaction: Dict):
    payload = {
        "transferAmount": {
            "amount": transaction["amount"],
            "currency": transaction["currency"]
        },
        "sender": {
            "name": transaction["sender"]["name"],
            "country": transaction["sender"].get("country", "US")
        },
        "recipient": {
            "name": transaction["recipient"]["name"],
            "accountUri": "pan:" + transaction["recipient"]["card"],
            "country": transaction["recipient"].get("country", "KE")
        },
        "channel": "card",
        "quoteId": "123456789"
    }

    # Simulation
    return {
        "provider": "mastercard",
        "status": "success",
        "message": "Transaction simulée vers Mastercard Cross-Border",
        "payload": payload
    }
