from isbn_checker import is_valid_isbn


def test_valid_isbn():
    assert is_valid_isbn("0306406152") is True


def test_valid_isbn_with_hyphens():
    assert is_valid_isbn("0-306-40615-2") is True


def test_invalid_isbn():
    assert is_valid_isbn("1234567890") is False


def test_invalid_length():
    assert is_valid_isbn("12345") is False
