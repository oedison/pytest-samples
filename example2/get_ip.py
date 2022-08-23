from unittest import mock

import requests


def get_ip():
    response = requests.get('https://httpbin.org/ip')
    if response.status_code == 200:
        return response.json()['origin']


@mock.patch('requests.get')
def test_get_ip(mock_request_get):
    expected = '0.0.0.0'

    mock_response = mock.Mock(name='response')
    mock_response.status_code = 200
    mock_response.json.return_value = {'origin': expected}

    mock_request_get.return_value = mock_response

    assert get_ip() == expected
    mock_request_get.assert_called_once_with('https://httpbin.org/ip')
    mock_response.json.assert_called_once()
