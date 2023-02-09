import main
import pytest


def test_data_items():
    data_10 = main.get_wufoo_data()
    assert len(data_10) == 10
