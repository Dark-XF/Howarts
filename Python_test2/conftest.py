import pytest

@pytest.fixture(scope="function")
def Prefabrication():
    print("开始执行")
    yield
    print("\n执行结束")