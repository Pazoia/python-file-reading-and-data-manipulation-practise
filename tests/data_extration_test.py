import unittest
from src.data_extration import DataExtraction
from unittest.mock import mock_open, patch

def test_get_data_from_file_returns_data():
    data_extraction = DataExtraction()
    
    mocked_data = "Some data returned"

    with patch("builtins.open", mock_open(read_data=mocked_data)):
        result = data_extraction.get_data_from_file("test_filename")
    
    assert result == "Some data returned"
        
    
