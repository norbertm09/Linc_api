# API Maître Paiement – Visa Direct & Mastercard Cross-Border

Cette API permet de router les paiements vers Visa ou Mastercard selon le fournisseur choisi.

## Endpoints

- `POST /pay` – Envoie un paiement simulé vers Visa ou Mastercard.

## Exemple de payload

```json
{
  "provider": "visa",
  "amount": 100.0,
  "currency": "USD",
  "sender": {"name": "John Smith", "country": "US"},
  "recipient": {"name": "Jane Doe", "card": "4111111111111111", "country": "KE"}
}
```

## Déploiement Render

```bash
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
```

## Accès Swagger

- [http://localhost:8000/docs](http://localhost:8000/docs)
