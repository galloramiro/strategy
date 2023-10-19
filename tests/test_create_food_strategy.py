from src.strategies import CreateFoodStrategy


def test_create_food_strategy__get_new_index_for_dict(persistency_dict_with_foods):
    next_index = CreateFoodStrategy._get_new_index_for_dict()

    assert next_index == 6


def test_create_food_strategy__get_new_index_for_dict_when_no_values_persisted(empty_persistency_dict):
    next_index = CreateFoodStrategy._get_new_index_for_dict()

    assert next_index == 1


def test_create_food_strategy_handle_event(empty_persistency_dict, create_food_events):
    create_food_event = create_food_events[0]
    food = CreateFoodStrategy.handle_event(create_food_event)

    assert food['id'] == 1

    create_food_event = create_food_events[1]
    food = CreateFoodStrategy.handle_event(create_food_event)

    assert food['id'] == 2
