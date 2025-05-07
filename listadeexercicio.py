# EXERCÍCIO 1 #
print("HELO STORE")
print("----------------")
menu = int(input("Qual produto você deseja comprar? Digite abaixo o número referente ao produto:"
                 "\n[1] - produto A"
                 "\n[2] - produto B"
                 "\n[3] - produto C\n"))
if menu ==1:
    produtoA = 5*2
    print(f"Você escolheu o produto A e irá pagar R${produtoA:.2f}")
elif menu == 2:
    produtoB = 8*2
    print(f"Você escolheu o produto B e irá pagar R${produtoB:.2f}")
elif menu ==3:
    produtoC = 12*2
    print(f"Você escolheu o produto C e irá pagar R${produtoC:.2f}")
else:
    print(f"Você escolheu o número {menu} e essa é uma opção inválida, por favor escolha o valor dentro das opções.")

# EXERCÍCIO 2 #
print("CURSO DA HELOISA")
print("----------------------------")
alunos_matriculados = ["João", "Maria", "Carlos"]
print("Bem-vindos ao curso online!")
for aluno in alunos_matriculados:
    print(f"Olá, {aluno}! Seja bem-vindo(a) ao curso!")

# EXERCÍCIO 4 #
numeros = [4, 7, 10]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é par: jogador AVANÇA.")
    else:
        print(f"{numero} é ímpar: jogador RECUA.")


# EXERCÍCIO 5 #
numero =int(input("Escolha um dos números a seguir para gerar a tabuada:"
                  "\n[2] - tabuada do 2"
                  "\n[3] - tabuada do 3"
                  "\n[4] - tabuada do 4\n"))
tabuada = 1
for x in range (1,11):
    tabuada = numero * x
    print(numero, "x", x, "=", numero*x)

# EXERCÍCIO 6 #
print("CINEMA DA HELO")
print("-------------------")
idades = [8,15,20]
for idade in idades:
    if idade < 18:
        print(f"Você tem {idade} anos, sendo assim não pode assistir ao filme pois é menor de idade")
    else:
        print(f"Você tem {idade} anos, logo pode assistir ao filme")

# EXERCÍCIO 7 #
print("HELO STORE")
print("----------------")
menu = int(input("Qual produto você deseja comprar? Digite abaixo o número referente ao produto:"
                 "\n[1] - produto 1"
                 "\n[2] - produto 2"
                 "\n[3] - produto 3\n"))
if menu ==1:
    produto1 = 50*0.1
    produto1total = 50 - produto1
    print(f"Você escolheu o produto A e irá pagar R${produto1total:.2f}")
elif menu == 2:
    produto2 = 120*0.1
    produto2total= 120 - produto2
    print(f"Você escolheu o produto B e irá pagar R${produto2total:.2f}")
elif menu ==3:
    produto3 = 200*0.1
    produto3total = 200-produto3
    print(f"Você escolheu o produto C e irá pagar R${produto3total:.2f}")
else:
    print(f"Você escolheu o número {menu} e essa é uma opção inválida, por favor escolha o valor dentro das opções.")

# EXERCÍCIO 8 #
palavras = ["casa", "paralelepípedo", "python"]
for palavra in palavras:
    print(f'A palavra "{palavra}" tem {len(palavra)} letras.')

# EXERCÍCIO 9 #
temperaturas_celsius = [30, 100, 0]
for c in temperaturas_celsius:
    f = (9/5) * c + 32
    print(f"{c}°C = {f:.1f}°F")

# EXERCÍCIO 10 #
numeros = [3, 9, 12]
for numero in numeros:
    if numero <= 5:
        classificacao = "Pequeno"
    elif numero <= 10:
        classificacao = "Médio"
    else:
        classificacao = "Grande"   
    print(f"O número {numero} é classificado como: {classificacao}")

# EXERCÍCIO 11 #
titulos = ["Ana Ana", "1DSTB-SENAI", "Subi no Onibus"]
for titulo in titulos:
    titulo_limpo = ''.join(char.lower() for char in titulo if char.isalnum())
    if titulo_limpo == titulo_limpo[::-1]:
        print(f'"{titulo}" é um palíndromo.')
    else:
        print(f'"{titulo}" NÃO é um palíndromo.')


# EXERCÍCIO 12 #
def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um número: "))

if numero < 0:
    print("Não existe a possibilidade de descobrir o fatorial desse número! Tente novamente!")
elif numero == 3:
    resultado = calcular_fatorial(numero)
    print("O fatorial de", numero, "é", resultado)
elif numero == 7:
    resultado = calcular_fatorial(numero)
    print("O fatorial de", numero, "é", resultado)
elif numero == 9:
    resultado = calcular_fatorial(numero)
    print("O fatorial de", numero, "é", resultado)
elif numero == 25:
    resultado = calcular_fatorial(numero)
    print("O fatorial de", numero, "é", resultado)
elif numero == 26:
    resultado = calcular_fatorial(numero)
    print("O fatorial de", numero, "é", resultado)
else:
    print("Número inválido, escolha algum número entre: 3,7,9,25,26")
