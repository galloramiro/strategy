from typing import Dict

from src.config import EventTypes, PERSISTENCY_DICT
from src.strategies.interface import StrategyInterface


class CreateFoodStrategy(StrategyInterface):
    @classmethod
    def handle_event(cls, event: Dict) -> Dict:
        """This method would handle the create_food"""
        # TODO: add logging
        next_index = cls._get_new_index_for_dict()
        new_food = {"id": next_index, "name": event["name"], "stock": event["stock"]}
        PERSISTENCY_DICT[next_index] = new_food
        return new_food

    @staticmethod
    def can_handle_event() -> str:
        """Would return the name of the event that this strategy is ment to handle"""
        return EventTypes.CREATE_FOOD.value

    @staticmethod
    def _get_new_index_for_dict():
        """Would give you a new index base on the current index being used on the
        persistency dict"""
        # TODO: Add logging
        actual_keys = list(PERSISTENCY_DICT.keys())
        actual_keys.sort(reverse=True)
        try:
            last_index = actual_keys[0]
            return last_index + 1
        except IndexError:
            return 1
