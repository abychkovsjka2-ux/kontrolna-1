"""Відкриті приклади 09 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(9)

INDEX_DOCS = [(1, 'Python це мова програмування.'), (2, 'Мова Python проста!'), (3, 'Мова C складна')]

INDEX_EXPECTED = {'c': [3],
 'python': [1, 2],
 'мова': [1, 2, 3],
 'програмування': [1],
 'проста': [2],
 'складна': [3],
 'це': [1]}

PUBLIC = [(([(1, 'Python це мова програмування.'), (2, 'Мова Python проста!'), (3, 'Мова C складна')],
   'мова python'),
  [1, 2]),
 (([(1, 'Python це мова програмування.'), (2, 'Мова Python проста!'), (3, 'Мова C складна')],
   'мова -python'),
  [3])]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    docs, query = args
    assert M.search(M.build_index(docs), query) == expected


def test_public_index():
    assert M.build_index(INDEX_DOCS) == INDEX_EXPECTED


def test_functions_exist():
    for name in ('build_index', 'search'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
