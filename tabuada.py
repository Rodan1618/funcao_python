### TABUADA do 1 até o 10 ###

def tabuada_um_ao_dez():
    for i in range(1, 11):
        print(f"Tabuada do número {i}")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
    tabuada_um_ao_dez()
# Aqui é apenas um exeplo: 
### Tabuada do número 1
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10

def mostra_tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
mostra_tabuada(9)

# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81
# 9 x 10 = 90

def mostra_tabuada(nome, numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
mostra_tabuada("Por que ", 9)