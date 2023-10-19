# import logging
import os
from enum import Enum
# from logging import config

# ENVIRONMENT VARIABLES
MAIN_DIR = "/app"

# LOGGER CONFIG
# TODO: Fix logger, its giving async error thing
# config.fileConfig("/app/logging.conf")
# LOGGER = logging.getLogger("strategyPatternExample")

# PERSISTENCE
PERSISTENCY_DICT = {}


class EventTypes(Enum):
    CREATE_FOOD = "create_food"
    DELETE_FOOD = "delete_food"
    UPDATE_FOOD_STOCK = "update_food_stock"
