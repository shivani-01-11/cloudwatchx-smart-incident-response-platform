# reusable constants

SERVICES = {
    "payment-service": [
        "PAYMENT_TIMEOUT",
        "PAYMENT_FAILED"
    ],
    "auth-service": [
        "LOGIN_FAILURE",
        "TOKEN_EXPIRED"
    ],
    "inventory-service": [
        "STOCK_SYNC_FAILURE",
        "INVENTORY_MISMATCH"
    ],
    "notification-service": [
        "SMS_DELIVERY_FAILURE",
        "EMAIL_BOUNCE"
    ],
    "checkout-service": [
        "API_LATENCY",
        "CHECKOUT_FAILURE"
    ]
}

SEVERITY_DISTRIBUTION = {
    "LOW": 50,
    "MEDIUM": 30,
    "HIGH": 15,
    "CRITICAL": 5
}