import pytest
from chromia.utils import limit

limit_data = [
    (0, 0),
    (1, 1),
    (-1, 0),
    (10, 1),
    (-1.0, 0.0),
    (0.0, 0.0),
    (1.0, 1.0),
    (1.1, 1.0),
    (0.5, 0.5),
]


@pytest.mark.parametrize("test_input,expected", limit_data)
def test_limit_default(test_input, expected):
    result = limit(test_input)
    assert result == expected
    assert isinstance(result, type(test_input))
