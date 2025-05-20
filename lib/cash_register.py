#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0  # To track the last transaction amount

    def add_item(self, title, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        self.last_transaction = item_cost
        self.items.extend([title] * quantity)  # Add item title for each quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
        return self.total

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0  # Reset after voiding
