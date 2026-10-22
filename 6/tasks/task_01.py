"""МКР. Завдання 01: Перевірка пароля."""


def solve(password: str) -> str:
    missing = []

    if len(password) < 8:
        missing.append("довжини")

    if not any(char.isdigit() for char in password):
        missing.append("цифри")

    if not any(char.isupper() for char in password):
        missing.append("великої літери")

    if not any(char.islower() for char in password):
        missing.append("малої літери")

    if not missing:
        return "Пароль прийнято"

    return "Не вистачає: " + ", ".join(missing)


if __name__ == "__main__":
    password = input("Введіть пароль: ")
    print(solve(password))