import budget
from budget import chart
from unittest import main

food = budget.Category('Food')
food.deposit(1000, 'initial_deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
print(food.get_balance())
clothing = budget.Category('clothing')
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category('Auto')
auto.deposit(1000, 'initial deposit')
auto.withdraw(15)


print(food)
print(clothing)


print(chart([food, clothing, auto]))



main(module='test_module', exit=False)

