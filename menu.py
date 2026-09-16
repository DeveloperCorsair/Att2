from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://henriquemartins7t_db_user:fatec@cluster0.o4esj86.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercado_livre

# USUÁRIO
def delete_usuario(nome, sobrenome):
    #Delete
    global db
    mycol = db.usuario
    myquery = {"nome": nome, "sobrenome":sobrenome}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o usuário ",mydoc)

def create_usuario():
    #Insert
    global db
    mycol = db.usuario
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
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)

def read_usuario(nome):
    #Read
    global db
    mycol = db.usuario
    print("Usuários existentes: ")
    if not len(nome):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"],x["cpf"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_usuario(nome):
    #Read
    global db
    mycol = db.usuario
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
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
    mycol.update_one(myquery, newvalues)


print("Tchau Prof...")

# CRUD das entidades do banco mercado livre

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
    myquery = {" Qual o id do produto": id}
    mydoc = mycol.delete_one(myquery)
    print("Produto deletado ",mydoc)

def read_produto():
    global db
    mycol = db.usuario
    print("Aqui estão os produtos existentes: ")
    if not len(nome):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"],x["cpf"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_produto():
    global db
    mycol = db.usuario
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("Dados do usuário: ",mydoc)
    nome = input("Mudar Nome:")
    if len(nome):
        mydoc["nome"] = nome

    sobrenome = input("Mudar Sobrenome:")
    if len(sobrenome):
        mydoc["sobrenome"] = sobrenome

    cpf = input("Mudar nome do produto:")
    if len(nome):
        mydoc["nome"] = nome

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)

# FAVORITO
def create_favorito():
    global db

# COMPRA
def create_compra():
    global db

# VENDEDOR
def create_vendedor():
    global db


key = 0
sub = 0
while (key != 'S'):
    print("1-CRUD Usuário")
    print("2-CRUD Vendedor")
    print("3-CRUD Produto")
    key = input("Digite a opção desejada? (S para sair) ")

    if (key == '1'):
        print("Menu do Usuário")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create usuario")
            create_usuario()
            
        elif (sub == '2'):
            nome = input("Read usuário, deseja algum nome especifico? ")
            read_usuario(nome)
        
        elif (sub == '3'):
            nome = input("Update usuário, deseja algum nome especifico? ")
            update_usuario(nome)

        elif (sub == '4'):
            print("delete usuario")
            nome = input("Nome a ser deletado: ")
            sobrenome = input("Sobrenome a ser deletado: ")
            delete_usuario(nome, sobrenome)
            
    elif (key == '2'):
        print("Menu do Vendedor")        
    elif (key == '3'):
            print("Menu do Produto")
            print("1-Create Produto")
            print("2-Read Produto")
            print("3-Update Produto")
            print("4-Delete Produto")
            sub = input("Digite a opção desejada? (V para voltar) ")
            if (sub == '1'):
                print("Create produto")
                create_produto()
                
            elif (sub == '2'):
                nome = input("Read usuário, deseja algum nome especifico? ")
                read_produto(nome)
            
            elif (sub == '3'):
                nome = input("Update usuário, deseja algum nome especifico? ")
                update_produto(nome)
    
            elif (sub == '4'):
                print("delete produto")
                nome = input("Nome a ser deletado: ")
                sobrenome = input("Sobrenome a ser deletado: ")
                delete_produto(id, nome)

