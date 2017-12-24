import pytest
from fixture.application import Application

fixture = None

@pytest.fixture(scope="session")
def app():
    global fixture
    fixture = Application()
    return fixture