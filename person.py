from exceptions_person import invalid_dob_error
class Person:
    # constructor
    def __init__(self, firstname, lastname, dob, gender, address, address1):
        # check the dob and if it is out of date then raise exception
        if dob < 18: # have to make more complex for dob
            raise invalid_dob_error ("Ypu are too young for this account")
        self.firstname = firstname
        self.lastname = lastname
        self._dob = dob
        self.gender = gender
        self._address = address

    @property
    def firstname(self):  # acts like getter
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):  # acts like setter
        self._firstname = firstname