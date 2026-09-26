def next_id(contracts:list)->int:
    if len(contracts) == 0:
        return 1

    return max(contract["id"] for contract in contracts) + 1;

def is_phone(phone: str) -> bool:
    text = phone.strip().replace(" ", "").replace("-", "")
    if text.startswith("+"):
        text = text[1:]
    return text.isdigit() and 10 <= len(text) <= 15

def find_by_id(contacts: list, contact_id: int) -> dict | None:
    for contact in contacts:
        if contact["id"] == contact_id:
            return contact
    return None

def reindex(contacts: list) -> None:
    for index, contact in enumerate(contacts, start=1):
        contact["id"] = index
