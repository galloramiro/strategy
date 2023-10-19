from typing import Dict

from src.config import EventTypes, PERSISTENCY_DICT
from src.strategies.interface import StrategyInterface


class DeleteFoodStrategy(StrategyInterface):
    @classmethod
    def handle_event(cls, event: Dict) -> bool:
        """This method would handle the delete_food"""
        # TODO: Add logging
        try:
            PERSISTENCY_DICT.pop(event['food_id'])
            return True
        except KeyError:
            return False

    @staticmethod
    def can_handle_event() -> str:
        """Would return the name of the event that this strategy is ment to handle"""
        return EventTypes.DELETE_FOOD.value
