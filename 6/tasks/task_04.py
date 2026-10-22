"""МКР. Завдання 04: Конвертер температур."""


def solve(value: str, scale: str) -> str:
    value = value.strip()
    scale = scale.strip().upper()

    if not value:
        return "Помилка: некоректні дані"

    if value.startswith("-"):
        number = value[1:]
    else:
        number = value

    if number.count(".") > 1 or not number.replace(".", "").isdigit():
        return "Помилка: некоректні дані"

    if "." in number:
        parts = number.split(".")

        if parts[0] == "" or parts[1] == "":
            return "Помилка: некоректні дані"

    if scale not in ("C", "F", "K"):
        return "Помилка: некоректні дані"

    temperature = float(value)

    # Переведення у градуси Цельсія
    if scale == "C":
        celsius = temperature
    elif scale == "F":
        celsius = (temperature - 32) * 5 / 9
    else:
        celsius = temperature - 273.15

    # Перевірка абсолютного нуля
    if celsius < -273.15:
        return "Помилка: нижче абсолютного нуля"

    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15

    return (
        f"C: {celsius:.1f}\n"
        f"F: {fahrenheit:.1f}\n"
        f"K: {kelvin:.1f}"
    )


if __name__ == "__main__":
    print(solve(input("Введіть температуру: "), input("Введіть шкалу: ")))
