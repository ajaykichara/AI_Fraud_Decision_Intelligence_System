from services.transaction_service import TransactionService

service = TransactionService()

print("Transaction Service Loaded Successfully.")


from services.transaction_service import TransactionService

service = TransactionService()

transaction = {

    "merchant": "fraud_Rippin, Kub and Mann",
    "merchant_category": "grocery_pos",
    "transaction_amount": 250.50,
    "gender": "F",
    "city": "Lytton",
    "state": "IA",
    "customer_zip": 50561,
    "city_population": 1583,
    "job": "Scientist",
    "merchant_zip": 50561,
    "customer_age": 42,
    "transaction_hour": 22,
    "transaction_day": 15,
    "transaction_month": 6,
    "transaction_weekday": 4,
    "is_weekend": 0,
    "is_night_transaction": 1,
    "high_amount_transaction": 1

}

result = service.process_transaction(transaction)

print(result)