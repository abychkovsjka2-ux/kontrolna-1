"""МКР. Завдання 09: Інвертований індекс слів."""


def normalize_word(word: str) -> str:
    word = word.strip('.,!?;:"\'()')
    return word.lower()


def build_index(docs: list[tuple[int, str]]) -> dict[str, list[int]]:
    temp_index = {}

    for doc_id, text in docs:
        words = text.split()

        for word in words:
            word = normalize_word(word)

            if not word:
                continue

            if word not in temp_index:
                temp_index[word] = set()

            temp_index[word].add(doc_id)

    index = {}

    for word in sorted(temp_index):
        index[word] = sorted(temp_index[word])

    return index


def search(index: dict, query: str) -> list[int]:
    required = []
    excluded = []

    for word in query.split():
        if word.startswith("-"):
            word = normalize_word(word[1:])

            if word:
                excluded.append(word)
        else:
            word = normalize_word(word)

            if word:
                required.append(word)

    if not required:
        return []

    first_word = required[0]

    if first_word not in index:
        return []

    result = set(index[first_word])

    for word in required[1:]:
        if word not in index:
            return []

        result &= set(index[word])

    for word in excluded:
        if word in index:
            result -= set(index[word])

    return sorted(result)


if __name__ == "__main__":
    docs = [
        (1, "Python це мова програмування."),
        (2, "Мова Python проста!"),
        (3, "Мова C складна")
    ]

    index = build_index(docs)

    print(index)
    print(search(index, "мова python"))
    print(search(index, "мова -python"))
    print(search(index, "python"))