#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0

  def add_item(self, item, price, quantity = 1):
    for i in range(quantity):
      self.items.append(item)
    self.total = self.total + (price * quantity)
    self.last_transaction = price * quantity

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      total_discount = self.total * (self.discount/100)
      self.total -= int(total_discount)
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    self.total -= self.last_transaction
    