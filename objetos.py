import hashlib
nome = input("Digite o Nome: ")
sobrenome = input("Digite o Sobrenome: ")
end = []

# Objeto criado a partir das informações digitadas pelo usuário
key = 1
while (key != 'N'):
    rua = input("Digite a Rua: ")
    num = input("Digite o Número: ")
    bairro = input("Digite o Bairro: ")
    cidade = input("Digite a Cidade: ")
    cep = input("Digite o CEP: ")
    # Cria o objeto e coloca o mesmo no final de uma lista
    endereco = {
                'rua' : rua, 
                'num' : num, 
                'bairro' : bairro,
                'cidade' : cidade,
                'cep' : cep
    }
    end.append(endereco)
    key = input("Digitar outro endereço (S/N)?")

email = input("Digite o E-mail:")
senha = hashlib.sha256(input("Digiete a senha:").encode()).hexdigest()

# Usa o objeto anterior para popular um objeto maior
usuario = {
            'nome' : nome,
            'sobrenome' : sobrenome,
            'endereco' : end,
            'e-mail' : email, 
            'senha': senha
          }

print(usuario)


