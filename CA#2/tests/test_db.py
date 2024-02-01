from data_utils import display_data


def test_data_access():
    """Tests if data is being returned as a list from server."""
    db_data = display_data()
    assert isinstance(db_data, list) == True
