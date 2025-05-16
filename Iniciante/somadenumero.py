'''**Soma de N Números** | Some N números fornecidos pelo usuário. |'''
soma = 0
qtdenumeros =int(input("Quantos números deseja somar? "))
for i in (1, qtdenumeros+1):
    numero = int(input(f"Digite o {i}º numero: "))
    soma+=numero
print(f"A soma de todos os numeros é {soma}")
                       

    





