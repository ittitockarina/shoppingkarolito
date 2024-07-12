import requests

def create_customer():
    url = "https://api-sandbox.y.uno/v1/customers"

    payload = {
        "document": {
            "document_number": "1093333333",
            "document_type": "CC"
        },
        "phone": {
            "country_code": "57",
            "number": "3132450765"
        },
        "billing_address": {
            "country": "PE",
            "address_line_1": "Calle 34 # 56 - 78",
            "address_line_2": "Apartamento 502, Torre I",
            "city": "Bogotá",
            "state": "Cundinamarca",
            "zip_code": "111111",
            "neighborhood": "Comuna 2"
        },
        "shipping_address": {
            "country": "EC",
            "address_line_1": "Calle 34 # 56 - 78",
            "address_line_2": "Apartamento 502, Torre I",
            "city": "Bogotá",
            "state": "Cundinamarca",
            "zip_code": "111111",
            "neighborhood": "Comuna 2"
        },
        "merchant_customer_id": "155521",
        "merchant_customer_created_at": "2022-05-09T20:46:54.786342Z",
        "first_name": "John",
        "last_name": "Doe",
        "gender": "M",
        "date_of_birth": "1990-02-28",
        "email": "john.doe@email.com",
        "nationality": "CO",
        "country": "CO",
        "metadata": [
            {
                "key": "ID",
                "value": "123456"
            },
            {
                "value": "123456",
                "key": "ID"
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
#response = create_customer()
#print(response.text)


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
#response = create_checkout_session()
#print(response.text)



import requests

def create_payment():
    url = "https://api-sandbox.y.uno/v1/payments"

    payload = {
        "country": "CO",
        "amount": {
            "currency": "ARS",
            "value": 5000
        },
        "customer_payer": {
            "document": { "document_number": "351.040.753-97" },
            "billing_address": {
                "address_line_1": "Calle 34 # 56 - 78",
                "city": "Bogota",
                "country": "BR",
                "state": "Cundinamarca",
                "zip_code": "111111",
                "neighborhood": "Barrio 11"
            },
            "shipping_address": {
                "address_line_1": "Calle 34 # 56 - 78",
                "city": "Bogota",
                "country": "CO"
            },
            "id": "0c7257ea-3732-4cb3-a38c-7411dc6979e2",
            "merchant_customer_id": "example00234",
            "first_name": "John",
            "last_name": "Doe",
            "gender": "M",
            "date_of_birth": "1990-02-28",
            "email": "johndoe@y.uno",
            "nationality": "CO",
            "ip_address": "192.168.123.167",
            "device_fingerprint": "hi88287gbd8d7d782ge"
        },
        "checkout": { "session": "{{checkout_session}}" },
        "workflow": "DIRECT",
        "payment_method": {
            "detail": { "card": { "verify": False } },
            "type": "EFECTY"
        },
        "account_id": "d06a2605-85d3-4a3f-a86b-b5750feb1b09",
        "description": "Test Payment",
        "merchant_order_id": "AA01",
        "merchant_reference": "Test_AAB",
        "callback_url": "www.y.uno",
        "metadata": [
            {
                "key": "ID",
                "value": "SD00"
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "charset": "utf-8",
        "content-type": "application/json",
        "public-api-key": "sandbox_gAAAAABmULQZqNYRmMEyeutiZ7MLxBKbCHzWcUKdq8F53eVHXX_D6vsZvpItVyUxVYXQODe3wRIJqJVEdUS-WnXEOmHxO9saxwwIjdbBhJC0SWKzP7hkT5sz4w5suhM9BRDkZg-d6uqQWuigUklLZxTsFPyFdzeD5jaZ4kKrfIASNkJ4i3CNupR6m5-9p7T4WzW_24wxrgLwCBymZIFK7_N7Be92icuGiUwyvxpej1zGKyRc81fhQiY-sY9ncu2E0CgcVM3O6-ni",
        "private-secret-key": "gAAAAABmULQZJCFTJnM-rHEY11P-Mz3aihCmwcwoMRYGeO1JBT7hwZAuo4D5CT_RuuM6obEUJXW1leGVRWiu9BokV4WBRUqQSF78es0CFwhQVVXaS_ezW0h7Pl1P7J4CR7oKGtvp9mZ-1RNXgxyZC2MG0GKdIEeXq7rruJokpaLwCeSYU7hwzrPwxJJ7Z4Ftupy3dS7i8RkNAwqwoTFfzHIVX6fqJKw6wtcrhxlrFK01JaZ71Twp_McjTLCQ-zldKPy63-fW7dWj",
        "X-Idempotency-Key": "d06a2605-85d3-4a3f-a86b-b5750feb1b09"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response

# Llamada a la función y manejo de la respuesta
#response = create_payment()
#print(response.text)



def create_customer2(merchant_customer_id, first_name, last_name):
    url = "https://api-sandbox.y.uno/v1/customers"

    payload = {
        "document": {
            "document_number": "1093333333",
            "document_type": "CC"
        },
        "phone": {
            "country_code": "57",
            "number": "3132450765"
        },
        "billing_address": {
            "country": "PE",
            "address_line_1": "Calle 34 # 56 - 78",
            "address_line_2": "Apartamento 502, Torre I",
            "city": "Bogotá",
            "state": "Cundinamarca",
            "zip_code": "111111",
            "neighborhood": "Comuna 2"
        },
        "shipping_address": {
            "country": "EC",
            "address_line_1": "Calle 34 # 56 - 78",
            "address_line_2": "Apartamento 502, Torre I",
            "city": "Bogotá",
            "state": "Cundinamarca",
            "zip_code": "111111",
            "neighborhood": "Comuna 2"
        },
        "merchant_customer_id": merchant_customer_id,
        "merchant_customer_created_at": "2022-05-09T20:46:54.786342Z",
        "first_name": first_name,
        "last_name": last_name,
        "gender": "M",
        "date_of_birth": "1990-02-28",
        "email": "john.doe@email.com",
        "nationality": "CO",
        "country": "CO",
        "metadata": [
            {
                "key": "ID",
                "value": "123456"
            },
            {
                "value": "123456",
                "key": "ID"
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