from person import Person

class Customer(Person):

    def __init__(self, id, firstname, lastname, address, bankaccount, password, contactinfo, dob, gender=None):
        super().__init__(self, firstname, lastname, dob, gender, address)
        self.id = id
        self._bankaccount = bankaccount
        self._password = password
        self._contactinfo = contactinfo