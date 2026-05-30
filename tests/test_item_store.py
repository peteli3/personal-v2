import pytest

from app.routers.table import ItemStore


def test_list_categories():
    store = ItemStore()
    assert store.list_categories() == ["Hardware", "Software", "Service"]


def test_add_item():
    store = ItemStore()
    initial = len(store.list_items())
    store.add_item("Widget", "Hardware", 10, "A widget")
    assert len(store.list_items()) == initial + 1


def test_add_duplicate_raises():
    store = ItemStore()
    store.add_item("Unique", "Software", 1, "desc")
    with pytest.raises(RuntimeError, match="same name"):
        store.add_item("Unique", "Software", 2, "other")


def test_delete_item():
    store = ItemStore()
    store.add_item("ToRemove", "Service", 5, "temporary")
    store.delete_item("ToRemove")
    names = [row[0] for row in store.list_items()]
    assert "ToRemove" not in names
