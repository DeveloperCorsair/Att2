# Conexão com o MongoDB
import pymongo
from pymongo.server_api import ServerApi
import CHAVE_DB

client = pymongo.MongoClient(CHAVE_DB)
db = client["mercado_livre"]

global mydb
mydb = client.mercadolivre