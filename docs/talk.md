# Strategy pattern why, when and how

## Index
- [What](#what)
- [Why](#why)
- [When](#when)
- [How](#how)
  - [Interface](#interface)
  - [Strategies](#strategies)
  - [Teting your strategies](#testing-your-stratgies)
  - [Selecting your strategy](#selecting-your-strategy)

## What
A simple and smart way to work with similar objects in different ways base on different condition... haha 
wanna know more? use this [link](https://refactoring.guru/design-patterns/strategy) 

## Why?
Are you tired of endless functions with endless ifs followed by complex logic?
```python
def im_super_great_amazing_and_complex(complex_object):
    if complex_object.name == "Juancito":
        # do some pretty complex stuff

    if complex_object.last_name == "Pica piedra" and complex.object.name == "Pedor":
        # do some more complex stuff

    if complex_object.name == "Juancito" and complex_object.last_name == "Zambuzzeti":
        # do some more super pretty complex stuff

    # and so on.... and so on....
    # .... 2k lines latter
    return complex_object
```
Strategy pattern is your solution!!

Are you tired of trying to test this kind of logic and have a lot of dependencies and complex tests that dont let you fully understand your code?  
Strategy pattern is your solution!!!

Are you tired of trying to separate the work on atomic tasks and end up all bloqued because all work on the same file? 
Strategy pattern is your solution!!!!

## When
Do you have a logic that have a bunch of if with complex logic?
Do you need to provided flexibility base on different things?
Do you need to do a bunch of different not related things to a same object?

## How
You could do this with or without using an abstract class but I would suggest using one to be more clear and in this example I would use one.


### Interface
```python
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
```

### Strategies
Now using this base class you could implement the main and public methods, and I would suggest using the `_` to put complex logic on the "private" methods.  
Here is an example of what you could do:
```python
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
```

### Testing your strategies
One of my most loved parts... tests! 
If you like to do TDD this would help a lot, now you can create a file with the test that you need your strategy to pass and you can start developing base on that:  
- Sure that you would no breake anithing else
- Sure that you would not interfere with other people 
- Sure that your unit of code works
Here is an example of how this would look like:  
```python
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
```

### Selecting your strategies
This is where all can be confusing but one you understand the thing would be simple.
Remember the `can_handle_event()` function? the idea is that there you could put the event name that your strategy would handle, and this event handler class would have the logic to 
choose the strategy that you need, so you can pass the event or the parametters that you need and base on that you can know if that works or not. 
In this case, because I use this patter to work with events I use the event name and I match this with the class, and using the filter I can get how many strategies I want to use with an specific event. 
Here is an example of the code:
```python
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
```
Now there are 2 other things important in this class:
- How we build this object
- What we choose to return
In this case I chose to build the thing in the init, but you can have a build method, but tipicaly the structure would be prettey similar to this.  
On the other side I choose to return each strategy with the result, just for testing sake, but its not necesesary because this thing is ussualy a fire and forget.

Lastly, but not less important the test of the event handler would look pretty simple because the only thing that you need to test is that the strategy is able to apply the correct strategies, all the hard work has is tested on the strategies itself.
```python
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
```

