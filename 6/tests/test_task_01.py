"""Відкриті приклади 01 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(1)

PUBLIC = [(('Abcdef12',), 'Пароль прийнято'), (('abc',), 'Не вистачає: довжини, цифри, великої літери')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('solve',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
