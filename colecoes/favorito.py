import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.database import db

colecao_favorito = db["favorito"]