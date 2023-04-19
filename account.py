# create a blue-print (a class) for a bank account
# class is a method
class Account:
    number_of_accounts = 0
    # pass - makes sure error does not occur (placeholder)
    # lets function know something will be put in after

    # constructor
    def __init__(self, opening_amount):
        self._balance = opening_amount
        Account.number_of_accounts += 1

    ###################### Data #######################
    # getter - to read potentially data (hidden files) in a method
    def get_balance(self):
        # ._ means semi private
        #.__ means private
        # means don't mess with it/stay out
        return self._balance

    # getter
    def get_firstname(self):
        return self._firstname

    # setter
    def set_firstname(self, firstname):
        self._firstname = firstname

    # properties
    # @ is a decorator - adds extra layer of functionality to something
    @property
    def lastname(self): # acts like getter
        return self._lastname

    @lastname.setter
    def lastname(self, lastname): # acts like setter
        self._lastname = lastname

     ################### Functionality #####################
     # behaviour/functionality
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and self._balance - amount >=0:
            self._balance -= amount
        # return

    # overloading of __str__ special method
    def __str__(self):
        return "Bank account gas a balance of £" + str(self._balance)