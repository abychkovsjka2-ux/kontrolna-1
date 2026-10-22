"""Відкриті приклади 07 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(7)

PUBLIC = [((3, 4), [3, 6, 9, 12]), ((1, 0), [])]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    step, n = args
    assert M.apply_n(M.make_counter(step), n) == expected


def test_functions_exist():
    for name in ('make_counter', 'apply_n'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
