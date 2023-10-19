from src.config import PERSISTENCY_DICT
from src.strategies import UpdateFoodStockStrategy


def test_update_food_stock_strategy_handle_event(persistency_dict_with_foods, update_food_stock_events):
    update_stock_event = update_food_stock_events[0]

    food_to_update = PERSISTENCY_DICT[update_stock_event['food_id']]
    actual_stock = food_to_update['stock']
    assert update_stock_event['stock'] != actual_stock

    UpdateFoodStockStrategy.handle_event(update_stock_event)

    food_to_update = PERSISTENCY_DICT[update_stock_event['food_id']]
    actual_stock = food_to_update['stock']
    assert update_stock_event['stock'] == actual_stock


def test_update_food_stock_strategy_handle_event_cant_update_stock(
        persistency_dict_with_foods, update_food_stock_events
    ):
    update_stock_event = update_food_stock_events[3]

    actual_keys = list(PERSISTENCY_DICT.keys())
    assert update_stock_event['food_id'] not in actual_keys

    succesfully_updated = UpdateFoodStockStrategy.handle_event(update_stock_event)

    assert not succesfully_updated
