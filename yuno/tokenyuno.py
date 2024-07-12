import requests
import json
import random
from urllib.parse import urljoin

class ApiClient:
    def __init__(self, base_url, public_api_key, private_secret_key, media_type="application/json"):
        self.base_url = base_url
        self.public_api_key = public_api_key
        self.private_secret_key = private_secret_key
        self.media_type = media_type

    def send_post_method(self, entity, metodo):
        url_metodo = urljoin(self.base_url, metodo)
        json_text = json.dumps(entity)
        
        headers = {
            "accept": self.media_type,
            "charset": "utf-8",
            "content-type": self.media_type,
            self.public_api_key: self.public_api_key,
            self.private_secret_key: self.private_secret_key,
            "X-idempotency-key": str(random.randint(0, 1000000))
        }

        response = requests.post(url_metodo, data=json_text, headers=headers)
        
        return response.text

# Ejemplo de uso:
base_url = "https://api-sandbox.y.uno/"
public_api_key = "sandbox_gAAAAABmULQZqNYRmMEyeutiZ7MLxBKbCHzWcUKdq8F53eVHXX_D6vsZvpItVyUxVYXQODe3wRIJqJVEdUS-WnXEOmHxO9saxwwIjdbBhJC0SWKzP7hkT5sz4w5suhM9BRDkZg-d6uqQWuigUklLZxTsFPyFdzeD5jaZ4kKrfIASNkJ4i3CNupR6m5-9p7T4WzW_24wxrgLwCBymZIFK7_N7Be92icuGiUwyvxpej1zGKyRc81fhQiY-sY9ncu2E0CgcVM3O6-ni"
private_secret_key = "gAAAAABmULQZJCFTJnM-rHEY11P-Mz3aihCmwcwoMRYGeO1JBT7hwZAuo4D5CT_RuuM6obEUJXW1leGVRWiu9BokV4WBRUqQSF78es0CFwhQVVXaS_ezW0h7Pl1P7J4CR7oKGtvp9mZ-1RNXgxyZC2MG0GKdIEeXq7rruJokpaLwCeSYU7hwzrPwxJJ7Z4Ftupy3dS7i8RkNAwqwoTFfzHIVX6fqJKw6wtcrhxlrFK01JaZ71Twp_McjTLCQ-zldKPy63-fW7dWj"

client = ApiClient(base_url, public_api_key, private_secret_key)

# Datos de ejemplo para enviar
entity = {
    "document": {
        "document_number": "1093333333",
        "document_type": "CC"
    },
    "phone": {
        "country_code": "57",
        "number": "3132450765"
    },
    # ... otros datos ...
}

metodo = "v1/customers"
response = client.send_post_method(entity, metodo)
print(response)
