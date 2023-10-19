import pytest
import json

from src.config import MAIN_DIR, EventTypes, PERSISTENCY_DICT

FIXTURES_DIR = f"{MAIN_DIR}/tests/fixtures/"


@pytest.fixture
def events():
    with open(f'{FIXTURES_DIR}events.json', "r") as file_to_read:
        current_file = json.load(file_to_read)
    return current_file


@pytest.fixture
def create_food_events(events):
    return events[EventTypes.CREATE_FOOD.value]


@pytest.fixture
def delete_food_events(events):
    return events[EventTypes.DELETE_FOOD.value]


@pytest.fixture
def update_food_stock_events(events):
    return events[EventTypes.UPDATE_FOOD_STOCK.value]


@pytest.fixture
def empty_persistency_dict():
    PERSISTENCY_DICT.clear()
    return PERSISTENCY_DICT


@pytest.fixture
def persistency_dict_with_foods(empty_persistency_dict):
    PERSISTENCY_DICT[1] = {"name": "Pizza", "stock": 2}
    PERSISTENCY_DICT[2] = {"name": "Burger", "stock": 15}
    PERSISTENCY_DICT[3] = {"name": "Gnocchi", "stock": 5}
    return PERSISTENCY_DICT
