import requests

def create_checkout_session():
    url = "https://api-sandbox.y.uno/v1/checkout/sessions"

    payload = {
        "country": "AR",
        "amount": {
            "currency": "ARS",
            "value": 20000
        },
        "installments": { "plan_id": "7b70350a-0d08-4f2f-be84-6423273aec7c" },
        "customer_id": "6eee253e-fcb1-44d9-bd7a-fd232d7278cf",
        "merchant_order_id": "Example Order ID",
        "payment_description": "Example Payment Description",
        "callback_url": "www.y.uno",
        "account_id": "d06a2605-85d3-4a3f-a86b-b5750feb1b09",
        "metadata": [
            {
                "key": "ID",
                "value": "123456"
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "charset": "utf-8",
        "content-type": "application/json",
        "public-api-key": "sandbox_gAAAAABmULQZqNYRmMEyeutiZ7MLxBKbCHzWcUKdq8F53eVHXX_D6vsZvpItVyUxVYXQODe3wRIJqJVEdUS-WnXEOmHxO9saxwwIjdbBhJC0SWKzP7hkT5sz4w5suhM9BRDkZg-d6uqQWuigUklLZxTsFPyFdzeD5jaZ4kKrfIASNkJ4i3CNupR6m5-9p7T4WzW_24wxrgLwCBymZIFK7_N7Be92icuGiUwyvxpej1zGKyRc81fhQiY-sY9ncu2E0CgcVM3O6-ni",
        "private-secret-key": "gAAAAABmULQZJCFTJnM-rHEY11P-Mz3aihCmwcwoMRYGeO1JBT7hwZAuo4D5CT_RuuM6obEUJXW1leGVRWiu9BokV4WBRUqQSF78es0CFwhQVVXaS_ezW0h7Pl1P7J4CR7oKGtvp9mZ-1RNXgxyZC2MG0GKdIEeXq7rruJokpaLwCeSYU7hwzrPwxJJ7Z4Ftupy3dS7i8RkNAwqwoTFfzHIVX6fqJKw6wtcrhxlrFK01JaZ71Twp_McjTLCQ-zldKPy63-fW7dWj"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response

# Llamada a la función y manejo de la respuesta
response = create_checkout_session()
print(response.text)
