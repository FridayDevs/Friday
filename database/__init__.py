

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import logging
from main_startup.config_var import Config
from main_startup import mongo_client


db_x = mongo_client["Friday"]
