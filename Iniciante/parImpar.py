'''**Par ou Ímpar** | Informe se um número inteiro é par ou ímpar'''

# Pedir o usuário o número:

numero = int(input("Digite o seu número: "))

# Lógica para definir se par ou ímpar:

if numero % 2 == 0:
    print(f"Este número é par.")
else:
    print(f"Este número é ímpar.")

