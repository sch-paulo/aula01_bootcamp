# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, 
# imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em 
# comparação com o bônus recebido.

# O programa deve começar solicitando ao usuário que insira seu nome.
# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".

nome = str(input('Qual o seu nome? '))
salario = float(input('Qual o seu salário mensal? '))
bonus = float(input('E o seu bônus recebido? '))

kpi_bonus = 1000 + salario * bonus
kpi_bonus = round(kpi_bonus,2)

print(f'Olá, {nome}! O valor do seu bônus foi de {kpi_bonus} reais!')