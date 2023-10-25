from src.strategies import CreateFoodStrategy, DeleteFoodStrategy, UpdateFoodStockStrategy


class EventsHandler:
    _STRATEGIES = []

    def __init__(self):
        self._STRATEGIES = [
            CreateFoodStrategy,
            DeleteFoodStrategy,
            UpdateFoodStockStrategy
        ]

    def handle_event(self, event):
        # TODO: add logging
        event_type = event["event_type"]
        event_strategies = filter(lambda strategy: strategy.can_handle_event() == event_type, self._STRATEGIES)

        outcomes = {}
        for strategy in event_strategies:
            outcome = strategy.handle_event(event=event)
            outcomes[strategy.__name__] = outcome

        return outcomes
