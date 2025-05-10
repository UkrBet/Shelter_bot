import re


def validate_phone(phone: str):
    # Приклад простої валідації українського номера
    return re.match(r"^\+?3?80\d{9}$", phone) is not None


def validate_email(email: str):
    # Проста валідація формату email
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


def is_yes(text: str):
    return text.lower() in ["так", "yes", "ок", "yep", "ага"]


if __name__ == '__main__':
    print(f"Валідний телефон +380991234567: {validate_phone('+380991234567')}")
    print(f"Невалідний телефон 12345: {validate_phone('12345')}")
    print(f"Валідний email test@example.com: {validate_email('test@example.com')}")
    print(f"Невалідний email test: {validate_email('test')}")
    print(f"'Так' як згода: {is_yes('Так')}")
    print(f"'Ні' як згода: {is_yes('Ні')}")
