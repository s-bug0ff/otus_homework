class ConsoleView:
    def show_message(self, message) -> None:
        print(message)

    def get_choice(self) -> str:
        choice = input("Выберите действие:\n1 - Показать справочник\n2 - Поиск контакта\n3 - Добавить контакт\n4 - Изменить контакт\n5 - Удалить контакт\n6 - Выход\n").strip()
        return choice

    def ask(self, text) -> str:
        return input(text).strip()

    def show_contacts(self, contacts: list) -> None:
        if len(contacts) == 0:
            print("Контактов нет")
            return

        for contact in contacts:
            print(
                contact.id,
                contact.first_name,
                contact.second_name,
                contact.phone,
                contact.comment
            )

    def show_contact(self, contact) -> None:
        print(contact.id, contact.first_name, contact.second_name, contact.phone)
