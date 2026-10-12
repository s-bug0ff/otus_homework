class PhonebookError(Exception):
    pass


class PhonebookNotFoundError(PhonebookError):
    pass


class CorruptedPhonebookError(PhonebookError):
    pass


class PhonebookSaveError(PhonebookError):
    pass


class EmptyNameError(PhonebookError):
    pass


class EmptyPhoneError(PhonebookError):
    pass


class InvalidPhoneError(PhonebookError):
    pass


class InvalidContactIdError(PhonebookError):
    pass


class ContactNotFoundError(PhonebookError):
    pass


class EmptySearchQueryError(PhonebookError):
    pass


class InvalidMenuChoiceError(PhonebookError):
    pass
