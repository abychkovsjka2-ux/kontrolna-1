"""Відкриті приклади 08 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(8)

PUBLIC = [((['Python', 'Web', ' ai'], ['web', 'AI', 'ML']),
  {'only_first': ['python'], 'only_second': ['ml'], 'both': ['ai', 'web'], 'similarity': 0.5}),
 (([], []), {'only_first': [], 'only_second': [], 'both': [], 'similarity': 0.0})]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert M.compare_tags(*args) == expected


def test_functions_exist():
    for name in ('compare_tags',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
