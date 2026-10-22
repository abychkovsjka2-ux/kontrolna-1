"""МКР. Завдання 05: Частоти символів."""


def solve(text: str) -> str:
    text = text.lower()

    counts = {}

    for char in text:
        if not char.isspace():
            counts[char] = counts.get(char, 0) + 1

    if not counts:
        return "Порожній текст"

    sorted_items = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    top_items = sorted_items[:5]

    result = []

    for char, count in top_items:
        result.append(f"{char}: {count}")

    result.append(f"Різних символів: {len(counts)}")

    return "\n".join(result)


if __name__ == "__main__":
    print(solve(input("Введіть текст: ")))
