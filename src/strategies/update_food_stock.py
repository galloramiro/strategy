from typing import Dict

from src.config import EventTypes, PERSISTENCY_DICT
from src.strategies.interface import StrategyInterface


class UpdateFoodStockStrategy(StrategyInterface):
    @classmethod
    def handle_event(cls, event: Dict) -> bool:
        """This method would handle the update_food_stock"""
        # TODO: Add logging
        try:
            food_to_update = PERSISTENCY_DICT[event['food_id']]
            food_to_update['stock'] = event['stock']
            return True
        except KeyError:
            return False

    @staticmethod
    def can_handle_event() -> str:
        """Would return the name of the event that this strategy is ment to handle"""
        return EventTypes.UPDATE_FOOD_STOCK.value
