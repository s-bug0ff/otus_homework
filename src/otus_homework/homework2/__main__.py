from pathlib import Path

from otus_homework.homework2.controller import PhoneBookController
from otus_homework.homework2.exceptions import PhonebookError
from otus_homework.homework2.model import PhoneBook
from otus_homework.homework2.view import ConsoleView


def main()->None:
    path = Path(__file__).parent /  "data" / "phonebook.json"
    view = ConsoleView()
    phonebook = PhoneBook(path)
    try:
        phonebook.load()
    except PhonebookError as error:
        view.show_message(str(error))
    controller = PhoneBookController(phonebook, view)
    controller.run()


if __name__ == "__main__":
    main()
