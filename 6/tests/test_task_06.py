"""Відкриті приклади 06 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(6)

PUBLIC = [(('1 -2 0 9 -4 3',),
  'Додатні: 3 шт., мін 1, макс 9, середнє 4.33\n'
  "Від'ємні: 2 шт., мін -4, макс -2, середнє -3.00\n"
  'Нулі: 1'),
 (('1 x 3',), 'Помилка: некоректний елемент: x')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('solve',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
