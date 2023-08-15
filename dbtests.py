import cx_Oracle
import pytest

# test_example.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
# test_functions.py
def capitalize(text):
    return text.capitalize()

def test_capitalize():
    assert capitalize("hello") == "Hello"
    assert capitalize("world") == "World"
# test_exceptions.py
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
# test_fixtures.py


@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_list_length(sample_list):
    assert len(sample_list) == 5

def test_list_sum(sample_list):
    assert sum(sample_list) == 15

# test_mocking.py
from unittest.mock import Mock
import requests

def get_data(url):
    response = requests.get(url)
    return response.json()

def test_get_data(monkeypatch):
    mock_response = Mock()
    mock_response.json.return_value = {"key": "value"}
    monkeypatch.setattr(requests, "get", lambda x: mock_response)

    result = get_data("http://example.com")

    assert result == {"key": "value"}
