from abc import ABC, abstractmethod
from typing import Dict


class StrategyInterface(ABC):  # pragma: no cover
    """Base for creating different strategies.
    Ideally this class would have only 2 public methods:
      - handle_event: class method, that would parse the event.
      - can_handle_event: would return the name of the event that this strategy is ment to handle
    """

    @classmethod
    @abstractmethod
    def handle_event(cls, event: Dict):
        """This method is ment to have all the logic that involve the
        handle of the event.
        In case of to complex logic, you can create private methods (dunderscore methods)
        to help the readability, and allowing only expose this one.
        """
        return event

    @staticmethod
    @abstractmethod
    def can_handle_event() -> str:
        """Would return the name of the event that this strategy is ment to handle"""
        return "EVENT_NAME"
