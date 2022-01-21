from src.data_manipulation import DataManipulation
from unittest.mock import mock_open, patch

def test_find_keywords_in_file():
    data_search = DataManipulation()

    m = mock_open(read_data="Some data to be searched")

    with patch("builtins.open", m) as mocked_open:
        actual = data_search.find_keyword_in_file("fake/file/path", "data")
        assert actual == "data"