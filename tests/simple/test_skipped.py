import pytest

# пример тестов, которые будут скипаться. Тесты как бы есть, но они в работе

@pytest.mark.skip
def test_skipped1():
    pass

@pytest.mark.skip
def test_skipped2():
    pass

@pytest.mark.skip
def test_skipped3():
    pass