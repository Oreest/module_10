from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # super.__init__()
    # реалізація класу
    pass


class Phone(Field):
    # реалізація класу
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def get_info(self):
        phones_info = ''
        for phone in self.phones:
            phones_info += f'{phone.value}, '
        return f'{self.name.value} : {phones_info[:-2]}'

    def add_phone(self, phone):
        if len(str(phone)) == 10:
            self.phones.append(Phone(phone))
        else:
            raise ValueError("Phone must be 10 digits")

    def change_phones(self, phones):
        for phone in phones:
            self.add_phone(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = dict()

    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_all_record(self):
        return self.data

    def has_record(self, name):
        return bool(self.data.get(name))

    def get_record(self, name) -> Record:
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)
        for record in self.get_all_record().values():
            for phone in record.phones:
                if phone.value == value:
                    return record

        raise ValueError("Contact with this value does not exist.")


def main():
    book = AddressBook()
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    for name, record in book.data.items():
        print(name, record)


if __name__ == "__main__":
    main()
