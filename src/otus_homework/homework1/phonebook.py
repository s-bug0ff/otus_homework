
from otus_homework.homework1.data import *
from otus_homework.homework1.util import *


def main_menu()->None:
    contacts = load_contacts()
    while True:
        choice = input("Выберите действие:\n1 - Показать справочник\n2 - Поиск контакта\n3 - Добавить контакт\n4 - Изменить контакт\n5 - Удалить контакт\n6 - Выход\n").strip()
        if not choice.isdigit():
            print("Введено неправильное действие, выберите другое")
            continue
        if int(choice) == 1:
            print("Справочник")
            list_contact(contacts)
        elif int(choice) == 2:
            print("Поиск")
            find_contact(contacts)
        elif int(choice) == 3:
            print("Добавить контакт")
            add_contact(contacts)
        elif int(choice) == 4:
            print("Изменить контакт")
            edit_contact(contacts)
        elif int(choice) == 5:
            print("Удалить контакт")
            delete_contact(contacts)
        elif int(choice) == 6:
            print("Выход")
            break
        else:
            print("Введено неправильное действие, выберите другое")
            continue

    return


def list_contact(contacts:list) -> None:
    if len(contacts) == 0:
        print("Контактов нет")
        return

    for contact in contacts:
        print(
            contact["id"],
            contact["first_name"],
            contact["second_name"],
            contact["phone"],
            contact["comment"]
        )

def add_contact(contracts:list  ) -> None:
    first_name = input("Введите имя: ").strip()
    if len(first_name) == 0 or first_name == "":
        print("Имя не может быть пустым")
        return
    second_name = input("Введите фамилию: ").strip()
    phone = input("Введите номер телефона: ").strip()
    if len(phone) == 0 or phone == "":
        print("Телефон не может быть пустым")
        return
    if not is_phone(phone):
        print("Некорректный телефон")
        return
    comment = input("Введите коментарий: ").strip()

    contracts.append(
        {
            "id": next_id(contracts),
            "first_name": first_name,
            "second_name": second_name,
            "phone": phone,
            "comment": comment,
        }
    )
    save_contacts(contracts);
    print("Контакт добавлен")

def delete_contact(contacts:list) -> None:
    id = input("Введите id контакта: ").strip()
    if not id.isdigit():
        print("Введен неправильный id")
        return

    contact = find_by_id(contacts, int(id))
    if contact is None:
        print("Контакт не найден")
        return

    print(contact["id"], contact["first_name"], contact["second_name"], contact["phone"])
    answer = input("Удалить? y/n: ").strip().lower()
    if answer != "y":
        print("Удаление отменено")
        return
    contacts.remove(contact)
    reindex(contacts)
    save_contacts(contacts)
    print("Контакт удалён")

def find_contact(contacts: list) -> None:
    query = input("Введите текст для поиска: ").strip().lower()
    if query == "":
        print("Введите слово")
        return

    found = []
    for contact in contacts:
        text = " ".join(
            [
                contact["first_name"],
                contact["second_name"],
                contact["phone"],
                contact["comment"],
            ]
        ).lower()
        if query in text:
            found.append(contact)

    if len(found) == 0:
        print("Ничего не найдено")
        return

    list_contact(found)

def edit_contact(contacts: list) -> None:
    text = input("Введите id контакта: ").strip()
    if not text.isdigit():
        print("Введен неправильный id")
        return

    contact = find_by_id(contacts, int(text))
    if contact is None:
        print("Контакт не найден")
        return

    print("Пустой ввод оставляет старое значение")

    first_name = input(f"Имя [{contact['first_name']}]: ").strip()
    second_name = input(f"Фамилия [{contact['second_name']}]: ").strip()
    phone = input(f"Телефон [{contact['phone']}]: ").strip()
    comment = input(f"Комментарий [{contact['comment']}]: ").strip()

    if phone != "" and not is_phone(phone):
        print("Некорректный телефон")
        return

    if first_name != "":
        contact["first_name"] = first_name
    if second_name != "":
        contact["second_name"] = second_name
    if phone != "":
        contact["phone"] = phone
    if comment != "":
        contact["comment"] = comment

    save_contacts(contacts)
    print("Контакт изменён")
