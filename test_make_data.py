import pytest
import os
import pandas as pd
from unittest.mock import patch, MagicMock
from make_data import write_inaugural_addresses


@pytest.fixture
def mock_response():
    """Mock a successful HTTP response for web scraping."""
    mock_resp = MagicMock()
    mock_resp.content = """
    <html>
        <h3 class="diet-title"><a>George Washington</a></h3>
        <div class="diet-by-line president">President 1</div>
        <span class="date-display-single" content="1789-04-30"></span>
        <div class="field-docs-content">Four score and seven years ago...</div>
    </html>
    """
    return mock_resp


def test_write_inaugural_addresses_creates_csv(mock_response):
    """Test that write_inaugural_addresses creates a CSV file."""
    with patch("make_data.requests.get", return_value=mock_response):
        with patch("make_data.time.sleep"):  # Skip sleep delays
            write_inaugural_addresses(n_speeches=1)
    
    # Check that the file was created
    assert os.path.exists("data/inaugural_address.csv")
    
    # Clean up
    if os.path.exists("data/inaugural_address.csv"):
        os.remove("data/inaugural_address.csv")


def test_write_inaugural_addresses_output_structure(mock_response):
    """Test that the output CSV has the correct structure and columns."""    
    with patch("make_data.requests.get", return_value=mock_response):
        with patch("make_data.time.sleep"):
            write_inaugural_addresses(n_speeches=1)
    
    df = pd.read_csv("data/inaugural_address.csv")
    
    # Check expected columns
    expected_columns = ["president_name", "president_number", "date", "text"]
    assert list(df.columns[1:]) == expected_columns  # Skip index column
    
    # Check that we have one row
    assert len(df) == 1
    
    # Check that data is not empty
    assert df["president_name"].iloc[0] == "George Washington"
    assert df["president_number"].iloc[0] == 1
    
    # Clean up
    if os.path.exists("data/inaugural_address.csv"):
        os.remove("data/inaugural_address.csv")
