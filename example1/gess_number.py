from unittest import mock
import pytest
import random


def guess_number(num):
    result = random.randint(1, 10)
    if result == num:
        return 'You won!'
    else:
        return 'You lost!'


@pytest.mark.parametrize('_input,expected', [(3, 'You won!'), (5, 'You lost!')])
@mock.patch('random.randint')
def test_guess_number(mock_randint, _input, expected):
    mock_randint.return_value = 3
    assert guess_number(_input) == expected
    mock_randint.assert_called_once()
