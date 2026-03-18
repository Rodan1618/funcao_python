### Definição de função:
#Função são blocos de códicos nomeados capazes de realizar uma ação específica, se quisermos excutar essa ação específica, é só "Chamar" excrevendo o nome da função.
### SINTAXE: 
# def nome_da_funcao():
    #código
#nome_da_funcao

def saudacao(nome):
    print("Ola,", nome, "seja bem-vindo")
saudacao("Rodan")
saudacao("Lucas")
saudacao("José") 


def apresentar_usuario(nome, idade):
    print(f"Usuário: {nome}, Idade: {idade} anos")

    apresentar_usuario("Rodan", 30)
#com um único print podemos colocar vários nome
#ou 2° opção abaixo:

def apresentar_usuario():
    nome = input("Insira seu nome de usuário: ")
    idade = int(input("Digite sua idade: "))
    print(f"Usuário: {nome}, Idade: {idade} anos")

    apresentar_usuario()

def somar(a, b):
    return a + b
resultado = somar(20, 30)
print("O resultado é:", resultado)


for i in range(1, 11):
    print(f"Tabuada de {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

