from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def check_if_10(self):
        length=self
        if len(length)!=10:
            raise Exception("Wrong phone number format. Should be 10 digits.")
        else:
            return self
              
class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,item):
        try:
            self.phones.append(str(Phone.check_if_10(item)))
        except Exception as e:
            print(e)
        
    def remove_phone(self,item):
        if item in self.phones:
            self.phones.remove(item)
    
    def edit_phone(self,old,new):
        if old in self.phones:
            self.phones.remove(old)
            try:
                self.phones.append(str(Phone.check_if_10(new)))
            except Exception as e:
                print(e)
            # return f"{self.name.value}:{'; '.join(p for p in self.phones)}"
        
    def find_phone(self,phone:str):
        '''
        Looking for pphone in phone list
        '''
        if phone in self.phones:
            return f"{self.name}: {phone}"
        else:
            return "Not found"
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):
    def add_record (self,item:Record):
        self.data[item.name.value]=item
    
    def find(self,item:Record)->Record:
        return self.data.get(item)
            
    def delete(self,item:Record):
        if item in self.data:
            del self.data[item]


# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
book.delete("Jane")