from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(str(value)) == 10 and str(value).isdigit():
            super().__init__(value)
        else:
            raise ValueError("Phone must be 10 digits")


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

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def add_phone(self, phone):
        if len(str(phone)) == 10:
            self.phones.append(Phone(phone))
        else:
            raise ValueError("Phone must be 10 digits")

    def edit_phone(self, old_phone, new_phone):
        is_edited = False
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                is_edited = True
        if not is_edited:
            raise ValueError("No phone edited as phone does not exist")

    def remove_phone(self, phone):
        is_removed = False
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                is_removed = True
        if is_removed:
            return f"{phone}(s)has been removed"
        else:
            raise ValueError("No such phone in this record")

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


    def find(self, value):
        if self.has_record(value):
            return self.get_record(value)
        for record in self.get_all_record().values():
            for phone in record.phones:
                if phone.value == value:
                    return record

        # raise ValueError("Contact with this value does not exist.")

    def delete(self, name):
        if self.find(name):
            del self.data[name]


def main():
    try:
        book = AddressBook()
        john_record = Record("John")
        john_record.add_phone("1234567890")
        # john_record.add_phone("1234567890111")
        # john_record.add_phone("123456789o")
        john_record.add_phone("5555555555")
        john_record.add_phone('1234567890')
        print(john_record.get_info())
        john_record.edit_phone('5555555555', '4555555555')
        # john_record.delete("123456780")
        john_record.remove_phone("4555555555")
        print(john_record.get_info())
        print(john_record.find_phone("4555555555"))
        book.add_record(john_record)

        # Створення та додавання нового запису для Jane
        jane_record = Record("Jane")
        jane_record.add_phone("9876543210")
        book.add_record(jane_record)
        for name, record in book.data.items():
            print(name, record)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
