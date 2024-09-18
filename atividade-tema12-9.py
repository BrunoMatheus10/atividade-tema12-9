# Solicita ao usuário que insira o peso e a altura, garantindo que sejam maiores que 0
peso = float(input("Digite o seu peso (kg): "))
while peso <= 0:
    print("Peso deve ser maior que 0.")
    peso = float(input("Digite o seu peso (kg): "))

altura = float(input("Digite a sua altura (m): "))
while altura <= 0:
    print("Altura deve ser maior que 0.")
    altura = float(input("Digite a sua altura (m): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Classifica o IMC com base na tabela fornecida
if imc < 16:
    classificacao = "Muito abaixo do peso"
elif imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Acima do peso"
elif imc < 35:
    classificacao = "Obesidade Grau I"
elif imc <= 40:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

# Exibe o valor do IMC e a classificação
print(f"Seu IMC é: ", imc)
print(f"Classificação: ",classificacao)
