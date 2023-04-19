from account import Account
from saving_account import SavingAccount

# from module import class
# create an object instance form class
# this is called instantiation

lisa_account = Account(250) # calling a constructor to ensure object is ready to be used
bart_account = Account(20)

# object dot attributes(data) & object dot methods(behaviour, aka functions)
def GetAndDisplayBalance():
    global lisa_balance, bart_balance
    lisa_balance = lisa_account.get_balance()
    bart_balance = bart_account.get_balance()
    print(f'Lisa has £{lisa_balance} and Bart has £{bart_balance}')


# lisa_account.__init__()
GetAndDisplayBalance()

# lisa_account.__balance = 1000
# print(lisa_account.__balance)

lisa_balance = lisa_account.get_balance()
# underscore at the start of name is significantly important


print(f'Lisa has £{lisa_balance} and Bart has £{bart_balance}')

lisa_account.deposit(30)

lisa_balance = lisa_account.get_balance()
print(f'Lisa has £{lisa_balance} and Bart has £{bart_balance}')

print('=' * 50)
bart_account.withdraw(10)
lisa_balance = lisa_account.get_balance()
bart_balance = bart_account.get_balance()
print(f'Lisa has £{lisa_balance} and Bart has £{bart_balance}')

lisa_account.withdraw(20)
bart_account.withdraw(10)
lisa_balance = lisa_account.get_balance()
bart_balance = bart_account.get_balance()
print(f'Lisa has £{lisa_balance} and Bart has £{bart_balance}')

if hasattr(lisa_account, '__str__'):
    print('Lisa has an __str__')
    print(lisa_account)
    print(type(lisa_account))

x = 10
y = 3

if x > y:
    print('x is larger')

# if lisa_account > bart_account:
#     print('?')

# operator overloading
word = ' Wednesday '
print(word * 4)
print(x + y)
print(3.5 * 2)

nums = [1, 2, 3, 4]
if nums:
    print("The list is NOT empty")

if bart_account:
    print("Bart's account is TRUE")

print(lisa_account)
print(bart_account)

# using java type getters and setters for data
lisa_account.set_firstname('Lisa')
print(lisa_account.get_firstname())
account_firstname = lisa_account.get_firstname()

# using .Net type properties for data
lisa_account.lastname = 'Simpson'
print(lisa_account.lastname)

# instantiate  some saving account objects
lisa_saving_account = SavingAccount(150, 2.5)
marge_saving_account = SavingAccount(500, 3.0)


marge_saving_account.set_firstname('Marge')
marge_saving_account.lastname = 'Simpson'
print(marge_saving_account.get_interest_rate())


