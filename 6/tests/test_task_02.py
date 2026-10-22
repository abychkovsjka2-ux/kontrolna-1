"""Відкриті приклади 02 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(2)

PUBLIC = [(('3',),
  '3 x 1 = 3\n'
  '3 x 2 = 6\n'
  '3 x 3 = 9\n'
  '3 x 4 = 12\n'
  '3 x 5 = 15\n'
  '3 x 6 = 18\n'
  '3 x 7 = 21\n'
  '3 x 8 = 24\n'
  '3 x 9 = 27\n'
  '3 x 10 = 30\n'
  'Сума: 165'),
 (('13',), 'Помилка: n має бути цілим від 1 до 12')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('solve',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
