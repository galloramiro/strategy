from src.config import PERSISTENCY_DICT
from src.events_handler import EventsHandler
from src.strategies import CreateFoodStrategy,DeleteFoodStrategy,UpdateFoodStockStrategy


def test_event_handler_handle_event_get_correct_strategy(
        empty_persistency_dict, create_food_events, delete_food_events, update_food_stock_events
    ):
    # Create food_id 1 Gnocchi
    create_food_event = create_food_events[0]
    handler = EventsHandler()
    event_outcomes = handler.handle_event(event=create_food_event)

    assert len(event_outcomes) == 1

    strategy_outcome = event_outcomes[CreateFoodStrategy.__name__]
    assert strategy_outcome
    assert strategy_outcome["name"] == "Gnocchi"
    assert strategy_outcome["stock"] == 15

    # Trying to delete food_id 2 expected result False
    delete_food_event = delete_food_events[0]
    event_outcomes = handler.handle_event(event=delete_food_event)

    assert len(event_outcomes) == 1

    strategy_outcome = event_outcomes[DeleteFoodStrategy.__name__]
    assert not strategy_outcome

    updated_food_event = update_food_stock_events[0]
    event_outcomes = handler.handle_event(event=updated_food_event)

    assert len(event_outcomes) == 1

    strategy_outcome = event_outcomes[UpdateFoodStockStrategy.__name__]
    assert strategy_outcome
