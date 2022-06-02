def chart(categories):
    return None



class Category:


    def __init__(self, name):
        self.name = name
        self.ledger = list()
    def deposit(self, amount, description=''):
        """
        A deposit methot that acceps an amount description.
        """
        self.ledger.append({'amount': amount, 'description': description})
    def withdraw(self, amount, description=''):
        """
        A withdraw method.
        """
        if(self.check_funds(amount)):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    def get_balance(self):
        """
        A get_balance methot that returns the current balance of the budget.
        """
        total_cash = 0
        for item in self.ledger:
            total_cash+=item['amount']
        return total_cash
    def transfer(self, amount, category=''):
        """
        A transfer method that accepts an amount and another budget category as arguments.
        """
        if(self.check_funds(amount)):
            self.withdraw(amount, 'Transfer to', category.name)
            return True
        return False
    def check_funds(self, amount):
        if(self.get_balance() >= amount):
            return True
        return False
        











