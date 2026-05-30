from app.routers.counter import Counter


def test_counter_starts_at_zero():
    counter = Counter()
    assert counter.get_value() == 0


def test_counter_increment():
    counter = Counter()
    counter.set_value(counter.get_value() + 1)
    assert counter.get_value() == 1
