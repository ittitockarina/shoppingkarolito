from store.models import StoreProduct

CART_SESSION_KEY = 'f0d6bfcefe8b4885a698ce3f7aa6fc56'

PAYMENT_CARD_SESSION_KEY = '2e68e19ec6684d12837e6da3885f319f'

SHIPPING_INFORMATION_SESSION_KEY = '552414bfc3454ba09bc00b4bed4975ad'

class Cart:
    def __init__(self, request):
        self.session = request.session
        if CART_SESSION_KEY in request.session:
            self.carta = self.session.get(CART_SESSION_KEY)
        else:
            self.carta = self.session[CART_SESSION_KEY] = {}

        if PAYMENT_CARD_SESSION_KEY in request.session:
            self.payment_card = self.session.get(PAYMENT_CARD_SESSION_KEY)
        else:
            self.payment_card = self.session[PAYMENT_CARD_SESSION_KEY] = {}

        if SHIPPING_INFORMATION_SESSION_KEY in request.session:
            self.shipping_information = self.session.get(SHIPPING_INFORMATION_SESSION_KEY)
        else:
            self.shipping_information = self.session[SHIPPING_INFORMATION_SESSION_KEY] = {}

    def __len__(self):
        return len(self.carta)

    def get_payment_card(self):
        return self.payment_card

    def get_shipping_information(self):
        return self.shipping_information

    def get_store_products(self):
        store_products = StoreProduct.objects.filter(id__in=self.carta.keys())
        return store_products

    def get_quantities(self):
        return self.carta

    def add(self, store_product, quantity):
        self.carta[str(store_product.id)] = quantity
        self.session.modified = True

    def set_payment_card(self, cvc, date, number):
        self.payment_card['cvc'] = cvc
        self.payment_card['date'] = date
        self.payment_card['number'] = number
        self.session.modified = True

    def set_shipping_information(self, address, phone_number):
        self.shipping_information['address'] = address
        self.shipping_information['phone_number'] = phone_number
        self.session.modified = True

    def delete(self, store_product_id):
        del self.carta[str(store_product_id)]
        self.session.modified = True

    def total(self):
        total = 0
        quantities = self.get_quantities()
        store_products = StoreProduct.objects.filter(id__in=self.carta.keys())

        for key, value in quantities.items():
            key = int(key)
            for store_product in store_products:
                if store_product.id == key:
                    total += store_product.price * value

        return total
