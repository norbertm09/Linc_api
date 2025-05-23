import requests
from typing import Dict

def send_funds(transaction: Dict):
    payload = {
        "amount": transaction["amount"],
        "transactionCurrencyCode": transaction["currency"],
        "recipientPrimaryAccountNumber": transaction["recipient"]["card"],
        "senderName": transaction["sender"]["name"],
        "senderAddress": transaction["sender"].get("address", "N/A"),
        "acquirerCountryCode": "840",
        "retrievalReferenceNumber": "330000550000",
        "systemsTraceAuditNumber": "451001",
        "localTransactionDateTime": "2025-05-23T14:30:00",
        "acquiringBin": "408999",
        "senderAccountNumber": "4111111111111111"
    }

    # Simulation
    return {
        "provider": "visa",
        "status": "success",
        "message": "Transaction simulée vers Visa Direct",
        "payload": payload
    }
