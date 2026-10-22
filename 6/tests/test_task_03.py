"""Відкриті приклади 03 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(3)

PUBLIC = [(('Київ є столицею України',), 'Слів: 4\nНайдовше: столицею\nЗ великої літери: 2'),
 (('',), 'Слів: 0\nНайдовше: -\nЗ великої літери: 0')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('solve',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
