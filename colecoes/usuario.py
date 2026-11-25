import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.database import db

colecao_usuario = db["usuario"]

# CRUD de USUÁRIO
def delete_usuario(nome, sobrenome):
    global db
    colecao_usuario = db.usuario
    myquery = {"nome": nome, "sobrenome":sobrenome}
    documento = colecao_usuario.delete_one(myquery)
    print("Deletado o usuário ",documento)

def create_usuario():
    global db
    colecao_usuario = db.usuario
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    key = 1
    favoritos = []
    end = []
    while (key != 'N'):
        rua = input("Rua: ")
        num = input("Número: ")
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
    documento = { 
            "nome": nome, 
             "sobrenome": sobrenome, 
             "cpf": cpf, 
             "end": end 
             }
    colecao = colecao_usuario.insert_one(documento)
    print("Documento inserido com ID ",colecao.inserted_id)

def read_usuario(nome):
    global db
    colecao_usuario = db.usuario
    print("Usuários existentes: ")
    if not len(nome):
        documento = colecao_usuario.find().sort("nome")
        for colecao in documento:
            print(colecao["nome"],colecao["cpf"])
    else:
        myquery = {"nome": nome}
        documento = colecao_usuario.find(myquery)
        for colecao in documento:
            print(colecao)

def update_usuario(nome):
    # Procura o nome do usuário dentro da coleção
    global db
    colecao_usuario = db.usuario
    myquery = {"nome": nome}
    documento = colecao_usuario.find_one(myquery)

    print("Dados do usuário: ",documento)

    # 
    # Altera os dados do usuário
    nome = input("Mudar Nome:")
    if len(nome):
        documento["nome"] = nome

    sobrenome = input("Mudar Sobrenome:")
    if len(sobrenome):
        documento["sobrenome"] = sobrenome

    cpf = input("Mudar CPF:")
    if len(cpf):
        documento["cpf"] = cpf

    newvalues = { "$set": documento }
    colecao_usuario.update_one(myquery, newvalues)

print("Até a próxima!")