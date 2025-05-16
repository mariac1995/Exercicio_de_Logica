'''**Tabuada** | Mostre a tabuada de 1 a 10 de um número informado.''' 
numero = int(input("Digite o número: "))

for n in range (1, 10+1):
    resultado = numero * n 
    print(f"{numero} X {n} = {resultado}")