from atm_card import AtmCard

class Customer:

    def __init__(self, id, cust_pin = 1234, cust_balance = 10000):
        self.id = id
        self.cust_pin = cust_pin
        self.cust_balance = cust_balance

    def cek_id(self):
        return self.id

    def cek_pin(self):
        return self.cust_pin

    def cek_saldo(self):
        return self.cust_balance

    def update_pin(self, pin_baru):
        self.cust_pin = pin_baru

    def tarik_tunai(self,nominal):
        self.cust_balance -= nominal

    def setor_tunai(self, nominal):
        self.cust_balance += nominal
