# Solicita o nome e a quantidade de experiência do herói ao usuário
nome = input("Digite o nome do herói: ")
vitorias = int(input("Digite a quantidade de vitorias do herói: "))
derrotas = int(input("Digite a quantidade de derrotas do herói: "))
saldoVitorias = vitorias - derrotas

# Estrutura de decisão para determinar o nível do herói com base na quantidade de vitorias
if vitorias < 10:
    nivel = 'Ferro'
elif 11 <= vitorias <= 20:
    nivel = 'Bronze'
elif 21 <= vitorias <= 50:
    nivel = 'Prata'
elif 51 <= vitorias <= 80:
    nivel = 'Ouro'
elif 81 <= vitorias <= 90:
    nivel = 'Diamante'
elif 91 <= vitorias <= 100:
    nivel = 'Lendário'
else:
    nivel = 'Imortal'


# Exibe a mensagem final
print(f"O Herói {nome} tem saldo de {saldoVitorias} está no nível de {nivel}")
