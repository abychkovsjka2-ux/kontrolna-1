"""МКР. Завдання 08: Порівняння наборів тегів."""


def compare_tags(first: list[str], second: list[str]) -> dict:
    first_set = set()
    second_set = set()

    for tag in first:
        tag = tag.strip().lower()
        if tag:
            first_set.add(tag)

    for tag in second:
        tag = tag.strip().lower()
        if tag:
            second_set.add(tag)

    only_first = sorted(first_set - second_set)
    only_second = sorted(second_set - first_set)
    both = sorted(first_set & second_set)

    all_tags = first_set | second_set

    if not all_tags:
        similarity = 0.0
    else:
        similarity = round(len(both) / len(all_tags), 2)

    return {
        "only_first": only_first,
        "only_second": only_second,
        "both": both,
        "similarity": similarity
    }


if __name__ == "__main__":
    print(compare_tags(
        ["Python", "Code", "Python", "Web"],
        ["python", "Web", "HTML"]
    ))

    print()

    print(compare_tags(
        ["Python", "Code"],
        ["Python", "Code"]
    ))

    print()

    print(compare_tags([], []))
