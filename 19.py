num= int(input("digite um numero para sabe seu divisores: "))

print(f'Divisores de {num}')

for i in range(1, num+1):
    if num % i == 0:
        print(i)