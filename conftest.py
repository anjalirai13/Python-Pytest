import pytest


@pytest.fixture(scope="session", autouse=True)
def setup():
    fd = open("temp", "a+")
    fd.write("setup function\n")
    fd.close()

@pytest.fixture(scope="session", autouse=True)
def teardown():
    fd = open("temp", "a+")
    fd.write("before yield function\n")
    fd.close()
    yield
    fd = open("temp", "a+")
    fd.write("teardown function\n")
    fd.close()

@pytest.fixture(scope="function", autouse=True)
def inbetween_function():
    fd = open("temp", "a+")
    fd.write("inbetween function\n")
    fd.close()