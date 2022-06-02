
def chart(categories):
    """
    chart that takes a list of categories as an argument, it should return a string that is a bar chart
    """

    res = 'Percentage spent by category\n'
    i = 100
    totals = getTotals(categories)
    while i >= 0:
        cat_spaces = '  '
        for total in totals:
            if total * 100 >= i:
                cat_spaces += 'o  '
            else:
                cat_spaces += '  '
        res += str(i).rjust(3) + '|' + cat_spaces + ('\n')
        i-=10

    dashes = '-' + '---'*len(categories)
    names = []
    x_axis = ''
    for category in categories:
        names.append(category.name)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        nameStr = '    '
        for name in names:
            if x >= len(name):
                nameStr += '   '
            else:
               nameStr += name[x] + '  ' 
        if(x != len(maxi) - 1):
            nameStr += '\n'
        
        x_axis += nameStr
    res += dashes.rjust(len(dashes)+4) + '\n' + x_axis
    return res

def truncate(n):
    multipier = 10
    return int(n * multipier) / multipier


def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded






class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
    
    def __str__(self):
        title = f'{self.name:*^30}\n'
        items=''
        total = 0
        for item in self.ledger:
            a = item['description']
            b = item['amount']
            items += f'{a[0:23]:23}' + f'{b:7.2f}' + '\n'
            #items += f'{item['description'][0:23]:23}' + f'{item['amount']:>7.2f}' + '\n'
            total += item['amount']
        
        output = title + items + 'Total: ' + str(total)
        return output

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
    def transfer(self, amount, category):
        """
        A transfer method that accepts an amount and another budget category as arguments.
        """
        if(self.check_funds(amount)):
            self.withdraw(amount, 'Transfer to' + category.name)
            category.deposit(amount, 'Transfer from' + self.name)
            return True
        return False
    def check_funds(self, amount):
        if(self.get_balance() >= amount):
            return True
        return False
    #category method
    def get_withdrawls(self):
        total = 0
        for item in self.ledger:
            if item['amount'] < 0:
                total+= item['amount']
        return total

        











