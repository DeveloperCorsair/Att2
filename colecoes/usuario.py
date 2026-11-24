import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.database import db

colecao_usuario = db["usuario"]

# USUÁRIO
def delete_usuario(nome, sobrenome):
    #Delete
    global db
    colecao_usuario = db.usuario
    myquery = {"nome": nome, "sobrenome":sobrenome}
    mydoc = colecao_usuario.delete_one(myquery)
    print("Deletado o usuário ",mydoc)

def create_usuario():
    #Insert
    global db
    colecao_usuario = db.usuario
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    key = 1
    end = []
    while (key != 'N'):
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {        #isso nao eh json, isso é chave-valor, eh um obj
            "rua":rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco) #estou inserindo na lista
        key = input("Deseja cadastrar um novo endereço (S/N)? ")
    mydoc = { "nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end }
    x = colecao_usuario.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)

def read_usuario(nome):
    #Read
    global db
    colecao_usuario = db.usuario
    print("Usuários existentes: ")
    if not len(nome):
        mydoc = colecao_usuario.find().sort("nome")
        for x in mydoc:
            print(x["nome"],x["cpf"])
    else:
        myquery = {"nome": nome}
        mydoc = colecao_usuario.find(myquery)
        for x in mydoc:
            print(x)

def update_usuario(nome):
    #Read
    global db
    colecao_usuario = db.usuario
    myquery = {"nome": nome}
    mydoc = colecao_usuario.find_one(myquery)
    print("Dados do usuário: ",mydoc)
    nome = input("Mudar Nome:")
    if len(nome):
        mydoc["nome"] = nome

    sobrenome = input("Mudar Sobrenome:")
    if len(sobrenome):
        mydoc["sobrenome"] = sobrenome

    cpf = input("Mudar CPF:")
    if len(cpf):
        mydoc["cpf"] = cpf

    newvalues = { "$set": mydoc }
    colecao_usuario.update_one(myquery, newvalues)


print("Tchau Prof...")