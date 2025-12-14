import pytest

@pytest.fixture()
def before_after():
    print( 'Completed before test' )

    print( '\nТут выполнется код' )

    print( '\ncompleted after test' )


def test_demo1():
    assert 1 == 1


def test_demo2( before_after ):
    assert 2 == 2