import json

from otus_homework.homework2.exceptions import (
    ContactNotFoundError,
    CorruptedPhonebookError,
    EmptySearchQueryError,
    PhonebookNotFoundError,
    PhonebookSaveError,
)


class Contact:
    def __init__(self, contact_id, first_name, second_name, phone, comment):
        self.id = contact_id
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.comment = comment

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "second_name": self.second_name,
            "phone": self.phone,
            "comment": self.comment,
        }


def is_phone(phone: str) -> bool:
    text = phone.strip().replace(" ", "").replace("-", "")
    if text.startswith("+"):
        text = text[1:]
    return text.isdigit() and 10 <= len(text) <= 15


class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise PhonebookNotFoundError("Справочник не найден")
        except json.JSONDecodeError:
            raise CorruptedPhonebookError("Справочник поврежден")


class FileWriter:
    def __init__(self, path):
        self.path = path

    def write(self, contacts: list) -> None:
        try:
            with open(self.path, "w", encoding="utf-8") as file:
                json.dump(contacts, file, ensure_ascii=False, indent=4)
        except OSError:
            raise PhonebookSaveError("Ошибка сохранения")


class PhoneBook:
    def __init__(self, path):
        self.reader = FileReader(path)
        self.writer = FileWriter(path)
        self.contacts = []

    def load(self) -> None:
        try:
            data = self.reader.read()
        except PhonebookNotFoundError:
            self.contacts = []
            raise
        except CorruptedPhonebookError:
            self.contacts = []
            raise

        self.contacts = []
        for item in data:
            contact = Contact(
                item["id"],
                item["first_name"],
                item["second_name"],
                item["phone"],
                item["comment"],
            )
            self.contacts.append(contact)

    def save(self) -> None:
        data = []
        for contact in self.contacts:
            data.append(contact.to_dict())
        self.writer.write(data)

    def find_by_id(self, contact_id: int):
        for contact in self.contacts:
            if contact.id == contact_id:
                return contact
        raise ContactNotFoundError("Контакт не найден")

    def find(self, query: str) -> list:
        query = query.strip().lower()
        if query == "":
            raise EmptySearchQueryError("Введите слово")

        found = []
        for contact in self.contacts:
            text = " ".join(
                [
                    contact.first_name,
                    contact.second_name,
                    contact.phone,
                    contact.comment,
                ]
            ).lower()
            if query in text:
                found.append(contact)
        return found

    def next_id(self) -> int:
        if len(self.contacts) == 0:
            return 1

        return max(contact.id for contact in self.contacts) + 1

    def reindex(self) -> None:
        for index, contact in enumerate(self.contacts, start=1):
            contact.id = index

    def add(self, first_name, second_name, phone, comment) -> None:
        contact = Contact(
            self.next_id(), first_name, second_name, phone, comment
        )
        self.contacts.append(contact)
        self.save()

    def update(self, contact, first_name, second_name, phone, comment) -> None:
        if first_name != "":
            contact.first_name = first_name
        if second_name != "":
            contact.second_name = second_name
        if phone != "":
            contact.phone = phone
        if comment != "":
            contact.comment = comment
        self.save()

    def delete(self, contact) -> None:
        self.contacts.remove(contact)
        self.reindex()
        self.save()
