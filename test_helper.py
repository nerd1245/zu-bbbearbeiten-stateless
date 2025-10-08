import pytest
from helper import add, get_all, get, update, items

def setup_function():
    # Clear the items list before each test
    items.clear()

def test_add():
    add("buy bread")
    assert len(items) == 1
    assert items[0].text == "bbbuy bbbread"  # because 'b' → 'bbb'
    assert not items[0].isCompleted

def test_get_all():
    add("apple")
    add("banana")
    all_items = get_all()
    assert len(all_items) == 2
    assert all_items[0].text.startswith("a")

def test_get():
    add("milk")
    item = get(0)
    assert item.text == "milk"
    assert item.isCompleted == False

def test_update():
    add("eggs")
    assert not get(0).isCompleted
    update(0)
    assert get(0).isCompleted
    update(0)
    assert not get(0).isCompleted
