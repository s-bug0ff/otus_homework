from otus_homework.homework2.exceptions import (
    EmptyNameError,
    EmptyPhoneError,
    InvalidContactIdError,
    InvalidMenuChoiceError,
    InvalidPhoneError,
    PhonebookError,
)
from otus_homework.homework2.model import is_phone
from otus_homework.homework2.view import ConsoleView


class PhoneBookController:
    def __init__(self, phonebook, view: ConsoleView):
        self.phonebook = phonebook
        self.view = view

    def run(self) -> None:
        while True:
            choice = self.view.get_choice()
            try:
                if not choice.isdigit():
                    raise InvalidMenuChoiceError(
                        "Введено неправильное действие, выберите другое"
                    )
                if int(choice) == 1:
                    self.list_contact()
                elif int(choice) == 2:
                    self.find_contact()
                elif int(choice) == 3:
                    self.add_contact()
                elif int(choice) == 4:
                    self.edit_contact()
                elif int(choice) == 5:
                    self.delete_contact()
                elif int(choice) == 6:
                    self.view.show_message("Выход")
                    break
                else:
                    raise InvalidMenuChoiceError(
                        "Введено неправильное действие, выберите другое"
                    )
            except PhonebookError as error:
                self.view.show_message(str(error))

    def list_contact(self) -> None:
        self.view.show_message("Справочник")
        self.view.show_contacts(self.phonebook.contacts)

    def find_contact(self) -> None:
        self.view.show_message("Поиск")
        query = self.view.ask("Введите текст для поиска: ")
        found = self.phonebook.find(query)
        if len(found) == 0:
            self.view.show_message("Ничего не найдено")
            return
        self.view.show_contacts(found)

    def add_contact(self) -> None:
        self.view.show_message("Добавить контакт")
        first_name = self.view.ask("Введите имя: ")
        if len(first_name) == 0 or first_name == "":
            raise EmptyNameError("Имя не может быть пустым")
        second_name = self.view.ask("Введите фамилию: ")
        phone = self.view.ask("Введите номер телефона: ")
        if len(phone) == 0 or phone == "":
            raise EmptyPhoneError("Телефон не может быть пустым")
        if not is_phone(phone):
            raise InvalidPhoneError("Некорректный телефон")
        comment = self.view.ask("Введите коментарий: ")

        self.phonebook.add(first_name, second_name, phone, comment)
        self.view.show_message("Справочник сохранен")
        self.view.show_message("Контакт добавлен")

    def edit_contact(self) -> None:
        self.view.show_message("Изменить контакт")
        text = self.view.ask("Введите id контакта: ")
        if not text.isdigit():
            raise InvalidContactIdError("Введен неправильный id")

        contact = self.phonebook.find_by_id(int(text))
        self.view.show_message("Пустой ввод оставляет старое значение")

        first_name = self.view.ask(f"Имя [{contact.first_name}]: ")
        second_name = self.view.ask(f"Фамилия [{contact.second_name}]: ")
        phone = self.view.ask(f"Телефон [{contact.phone}]: ")
        comment = self.view.ask(f"Комментарий [{contact.comment}]: ")

        if phone != "" and not is_phone(phone):
            raise InvalidPhoneError("Некорректный телефон")

        self.phonebook.update(contact, first_name, second_name, phone, comment)
        self.view.show_message("Справочник сохранен")
        self.view.show_message("Контакт изменён")

    def delete_contact(self) -> None:
        self.view.show_message("Удалить контакт")
        contact_id = self.view.ask("Введите id контакта: ")
        if not contact_id.isdigit():
            raise InvalidContactIdError("Введен неправильный id")

        contact = self.phonebook.find_by_id(int(contact_id))
        self.view.show_contact(contact)
        answer = self.view.ask("Удалить? y/n: ").lower()
        if answer != "y":
            self.view.show_message("Удаление отменено")
            return
        self.phonebook.delete(contact)
        self.view.show_message("Справочник сохранен")
        self.view.show_message("Контакт удалён")
