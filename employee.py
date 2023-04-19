from person import Person

class Employee(Person):

    def __init__(self, id, firstname, lastname, dob, gender, address,  nationalinsurno, salary, bankaccount, contactinfo):
        super().__init__(self, firstname, lastname, dob, gender, address)
        self.id = id
        self._nationalinsurno = nationalinsurno
        self._salary = salary
        self._bankaccount = bankaccount
        self._contactinfo = contactinfo
