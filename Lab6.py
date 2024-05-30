from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        if not value:
            raise ValueError("Name is required")

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate(value):
            raise ValueError("Phone number must be 10 digits")

    @staticmethod
    def validate(value):
        return value.isdigit() and len(value) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone number not found")

    def edit_phone(self, old_number, new_number):
        phone = self.find_phone(old_number)
        if phone:
            if Phone.validate(new_number):
                phone.value = new_number
            else:
                raise ValueError("New phone number must be 10 digits")
        else:
            raise ValueError("Old phone number not found")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Name not found")

# Make adressbook
book = AddressBook()

#Create the John information
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Add John to adressbook
book.add_record(john_record)

# Create Jane informatiom
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Print the adressbook data
for name, record in book.data.items():
    print(record)

# Update John phone number
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Print: Contact name: John, phones: 1112223333; 5555555555

# Find the specific contact in  John adressbook
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Delete Jane
book.delete("Jane")

# Show me athe adressbook after the Jane was deleted
for name, record in book.data.items():
    print(record)
