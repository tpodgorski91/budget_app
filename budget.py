class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, desc=''):
        return self.ledger.append({
          "amount": amount,
          "description": desc
        })

    def withdraw(self, amount, desc=''):
        if self.get_balance() > amount:
            self.ledger.append({
              "amount": - amount,
              "description": desc
            })
            return True
        else:
            return False

    def get_balance(self):
        budget = 0
        for ele in self.ledger:
            budget += ele['amount']
        return budget

    def transfer(self):
        pass

    def check_funds(self):
        pass

def create_spend_chart(categories):
  pass

a = Category("Food")