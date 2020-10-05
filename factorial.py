def factorial(n):
    """calcula el factorial de n

    n int > 0
    returns n!
    """
    print(n)
    if n == 1:
        return 1
    return n * factorial(n - 1)    

n = int(input('Ingresa un numero: '))

print(f'el factorial de {n} es: ')
print(factorial(n))