import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.database import db

colecao_produto = db["produto"]

# PRODUTO
def create_produto():
    global db
    mycol = db.produto
    nome = input("Nome do produto: ")
    valor_unitario = int(input("Qual o valor do produto: "))
    descricao = input("Dê uma descrição: ")
    marca = input("Qual a marca: ")
    instrucoes_de_uso = input("Tem instruções? Quais: ")
    categoria = input("Categoria: ")
    estoque = int(input("Estoque: "))
    ativo = bool()
    mydoc = {"nome": nome,
             "valor_unitario": valor_unitario,
             "descricao": descricao,
             "marca": marca,
             "instrucoes_de_uso": instrucoes_de_uso,
             "categoria": categoria,
             "estoque": estoque,
             "ativo": ativo
            }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)

def delete_produto(id):
    global db
    mycol = db.produto
    myquery = {" Qual o id do produto?\n": id}
    mydoc = mycol.delete_one(myquery)
    print("Produto deletado ",mydoc)

def read_produto(nome):
    global db
    mycol = db.produto
    print("Aqui estão os produtos existentes: ")
    if nome:
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_produto(nome):
    global db
    mycol = db.produto
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("Informações do produto: ",mydoc)
    nome = input("Mudar Nome:")
    if len(nome):
        mydoc["nome"] = nome

    """ valor_unitario = input("Mudar Valor Unitário:")
    if len(valor_unitario):
        mydoc["valor_unitario"] = valor_unitario

    descricao = input("Mudar a descricao do produto:")
    if len(descricao):
        mydoc["descricao"] = descricao

    marca = input("Mudar a marca do produto:")
    if len(marca):
        mydoc["marca"] = marca

    instrucao = input("Mudar a instrucao de uso do produto:")
    if len(instrucao):
        mydoc["instrucao"] = instrucao

    categoria = input("Mudar a categoria do produto:")
    if len(categoria):
        mydoc["categoria"] = categoria

    estoque = input("Mudar o volume de estoque do produto:")
    if len(estoque):
        mydoc["estoque"] = estoque """

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)