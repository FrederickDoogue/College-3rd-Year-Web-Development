import pytest

import app as webapp

import DBcm

from data_utils import save_data, display_data


@pytest.fixture
def app():
    """This fixture creates the client object before each test runs, assuming the test references the client object."""
    app = webapp.app
    return app


"""
@pytest.fixture
def clean_up_db():
   #This code removes and and all test data from the database after the tests which refer to it run.
   
   yield
   
   with DBcm.UseDatabase(config) as db:
   SQL = "delete from comments where first = 'testing'"
   
   db.execyte(SQL)
"""
