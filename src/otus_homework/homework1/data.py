import json
from pathlib import Path

PHONEBOOK_PATH = Path(__file__).parent /  "data" / "phonebook.json"

def load_contacts() -> list:
    try:
        with open(PHONEBOOK_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Справочник не найден")
        return []
    except json.JSONDecodeError:
        print("Справочник поврежден")
        return []

def save_contacts(contacts:list) -> None:
    try:
        with open(PHONEBOOK_PATH, 'w', encoding="utf-8") as file:
            json.dump(contacts, file, ensure_ascii=False, indent=4)
            print("Справочник сохранен")
    except OSError:
        print("Ошибка сохранения")
