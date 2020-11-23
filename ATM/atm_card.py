class AtmCard:
    def __init__(self, default_pin, default_balance):
        self.default_pin = default_pin
        self.default_balance = default_balance

    def cek_pin(self):
        return self.default_pin

    def cek_saldo(self):
        return self.default_balance
