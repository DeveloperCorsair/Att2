# Responsável pela comunicação com o cliente
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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
    print("Produto deletado ", mydoc)

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

key = 0
sub = 0

while (key != 'S'):
    print("1-CRUD Usuário")
    print("2-CRUD Vendedor")
    print("3-CRUD Produto")
    print("4-CRUD Compra")
    print("5-CRUD Favorito")

    key = input("Digite a opção desejada? (Pressione S para sair)")

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
                nome = input("Read Produto, deseja algum nome especifico? ")
                read_produto(nome)
            
            elif (sub == '3'):
                nome = input("Update Produto, deseja algum nome especifico? ")
                """ valor_unitario = input("Update Produto, deseja algum valor_unitario especifico? ")
                descricao = input("Update Produto, deseja algum descricao especifico? ")
                marca = input("Update Produto, deseja algum marca especifico? ")
                instrucao = input("Update Produto, deseja algum instrucao especifico? ")
                categoria = input("Update Produto, deseja algum categoria especifico? ")
                estoque = input("Update Produto, deseja algum estoque especifico? ") """
                update_produto(nome)
    
            elif (sub == '4'):
                print("delete produto")
                nome = input("Nome a ser deletado: ")
                delete_produto(id, nome)
