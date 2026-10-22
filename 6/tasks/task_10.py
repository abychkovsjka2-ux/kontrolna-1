"""МКР. Завдання 10: Ледачі вікна й серії."""


from collections import deque


def windows(items, k: int):
    if k <= 0:
        raise ValueError("k має бути додатним")

    window = deque()

    for item in items:
        window.append(item)

        if len(window) == k:
            yield tuple(window)
            window.popleft()


def run_lengths(items):
    iterator = iter(items)

    try:
        current = next(iterator)
    except StopIteration:
        return

    length = 1

    for item in iterator:
        if item == current:
            length += 1
        else:
            yield (current, length)
            current = item
            length = 1

    yield (current, length)


def best_window(values: list[int], k: int) -> tuple | None:
    if k <= 0:
        raise ValueError("k має бути додатним")

    best = None
    best_sum = None
    start = 0

    for window in windows(values, k):
        current_sum = sum(window)

        if best_sum is None or current_sum > best_sum:
            best_sum = current_sum
            best = (start, current_sum)

        start += 1

    return best


if __name__ == "__main__":
    print(windows([1, 2, 3, 4], 2))
    print(list(windows([1, 2, 3, 4], 2)))

    print(list(run_lengths("aabccc")))

    print(best_window([1, 5, 2, 8, 1], 2))

    print(best_window([1], 3))