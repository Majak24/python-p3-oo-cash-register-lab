class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.discount = discount
        self.last_transaction_amount = 0.0

    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        for _ in range(quantity):
            self.items.append(title)
        self.last_transaction_amount = item_total

    def apply_discount(self):
        if self.discount == 0:
            message = "There is no discount to apply."
            print(message)
            return message
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total = int(self.total - discount_amount)
            message = f"After the discount, the total comes to ${self.total}."
            print(message)
            return message

    def void_last_transaction(self):
        if self.last_transaction_amount > 0:
            self.total -= self.last_transaction_amount
            while self.items and self.last_transaction_amount > 0:
                self.items.pop()
                self.last_transaction_amount -= self.total / len(self.items) if self.items else 0
            self.last_transaction_amount = 0.0

    def items_list(self):
        return self.items