"""Відкриті приклади 10 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(10)

import inspect
import itertools

PUBLIC = [(('windows', [1, 2, 3, 4], 2), [(1, 2), (2, 3), (3, 4)]),
 (('run_lengths', 'aabccc'), [('a', 2), ('b', 1), ('c', 3)]),
 (('best_window', [1, 5, 2, 8, 1], 2), (2, 10)),
 (('best_window', [1], 3), None)]


@pytest.mark.parametrize("case,expected", PUBLIC)
def test_public(case, expected):
    name, *args = case
    result = getattr(M, name)(*args)
    if name in ("windows", "run_lengths"):
        result = list(result)
    assert result == expected


def test_functions_exist():
    for name in ('windows', 'run_lengths', 'best_window'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
