"""МКР. Завдання 03: Статистика слів."""


def solve(text: str) -> str:
    words = text.split()

    if not words:
        return "Слів: 0\nНайдовше: -\nЗ великої літери: 0"

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    capital_count = 0

    for word in words:
        if word[0].isupper():
            capital_count += 1

    return (
        f"Слів: {len(words)}\n"
        f"Найдовше: {longest}\n"
        f"З великої літери: {capital_count}"
    )


if __name__ == "__main__":
    print(solve(input("Введіть текст: ")))
