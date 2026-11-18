# Conexão com o MongoDB
import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://henriquemartins7t_db_user:fatec@cluster0.o4esj86.mongodb.net/?appName=Cluster0", server_api=ServerApi('1'))
db = client.test

global mydb
mydb = client.mercadolivre