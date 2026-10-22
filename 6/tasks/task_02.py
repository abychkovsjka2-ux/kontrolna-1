"""МКР. Завдання 02: Таблиця множення."""


def solve(n: str) -> str:
    n = n.strip()

    if not n.isdigit():
        return "Помилка: n має бути цілим від 1 до 12"

    number = int(n)

    if number < 1 or number > 12:
        return "Помилка: n має бути цілим від 1 до 12"

    result = []
    total = 0

    for k in range(1, 11):
        product = number * k
        result.append(f"{number} x {k} = {product}")
        total += product

    result.append(f"Сума: {total}")

    return "\n".join(result)


if __name__ == "__main__":
    print(solve(input("Введіть n: ")))
