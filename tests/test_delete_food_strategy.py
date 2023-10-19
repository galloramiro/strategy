from src.config import PERSISTENCY_DICT
from src.strategies import DeleteFoodStrategy


def test_delete_food_strategy_handle_event_works_as_expected(persistency_dict_with_foods, delete_food_events):
    delete_event = delete_food_events[0]
    food_deleted = DeleteFoodStrategy.handle_event(delete_event)

    assert food_deleted

    actual_keys = list(PERSISTENCY_DICT.keys())
    assert delete_event['food_id'] not in actual_keys


def test_delete_food_strategy_handle_event_cant_delete_food(persistency_dict_with_foods, delete_food_events):
    delete_event = delete_food_events[2]

    actual_keys = list(PERSISTENCY_DICT.keys())
    assert delete_event['food_id'] not in actual_keys

    food_deleted = DeleteFoodStrategy.handle_event(delete_event)

    assert not food_deleted




