"""Відкриті приклади 04 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(4)

PUBLIC = [(('100', 'C'), 'C: 100.0\nF: 212.0\nK: 373.1'), (('-300', 'C'), 'Помилка: нижче абсолютного нуля')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('solve',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
