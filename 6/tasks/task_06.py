"""МКР. Завдання 06: Фільтр і статистика чисел."""


def solve(text: str) -> str:
    items = text.split()

    if not items:
        return "Помилка: немає чисел."

    numbers = []

    for item in items:
        if item.startswith("-"):
            digits = item[1:]
        else:
            digits = item

        if not digits.isdigit() or digits == "":
            return f"Помилка: некоректний елемент: {item}"

        numbers.append(int(item))

    positive = []
    negative = []
    zeros = 0

    for number in numbers:
        if number > 0:
            positive.append(number)
        elif number < 0:
            negative.append(number)
        else:
            zeros += 1

    if positive:
        positive_average = sum(positive) / len(positive)
        positive_result = (
            f"Додатні: {len(positive)} шт., "
            f"мін {min(positive)}, макс {max(positive)}, "
            f"середнє {positive_average:.2f}"
        )
    else:
        positive_result = "Додатні: немає"

    if negative:
        negative_average = sum(negative) / len(negative)
        negative_result = (
            f"Від'ємні: {len(negative)} шт., "
            f"мін {min(negative)}, макс {max(negative)}, "
            f"середнє {negative_average:.2f}"
        )
    else:
        negative_result = "Від'ємні: немає"

    return (
        f"{positive_result}\n"
        f"{negative_result}\n"
        f"Нулі: {zeros}"
    )


if __name__ == "__main__":
    print(solve(input("Введіть числа: ")))
