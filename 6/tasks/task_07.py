"""МКР. Завдання 07: Лічильник із замиканням."""


def make_counter(step: int):
    count = 0

    def counter():
        nonlocal count
        count += step
        return count

    return counter


def apply_n(f, n: int) -> list:
    results = []

    if n <= 0:
        return results

    for _ in range(n):
        results.append(f())

    return results


if __name__ == "__main__":
    f = make_counter(3)
    print(apply_n(f, 4))

    f = make_counter(5)
    print(apply_n(f, 3))

    f = make_counter(10)
    print(apply_n(f, 0))