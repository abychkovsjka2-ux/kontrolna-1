"""Відкриті приклади 05 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(5)

PUBLIC = [(('Banana',), 'a: 3\nn: 2\nb: 1\nРізних символів: 3'), (('   ',), 'Порожній текст')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('solve',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
