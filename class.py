from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10):
            raise ValueError("Phone number must be 10 digits") 


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

    def add_phone(self, phone):
        self.phones.append(Phone(phone))   
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break
    def edit_phone(self, old_phone: str, new_phone: str):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
            break

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    def find(self, name):
        return self.data.get(name)
    def delete (self, name):
        if name in self.data:
            del self.data[name]
                

        
        
        
    