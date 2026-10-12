class ConsoleView:
    def show_message(self, message) -> None:
        print(message)

    def get_choice(self) -> str:
        choice = input(
            "Выберите действие:\n"
            "1 - Показать справочник\n"
            "2 - Поиск контакта\n"
            "3 - Добавить контакт\n"
            "4 - Изменить контакт\n"
            "5 - Удалить контакт\n"
            "6 - Выход\n"
        ).strip()
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
                contact.comment,
            )

    def show_contact(self, contact) -> None:
        print(
            contact.id,
            contact.first_name,
            contact.second_name,
            contact.phone,
        )
