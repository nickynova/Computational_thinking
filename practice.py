def main():
    """
    retomando coding

    """
    # add = input('Escribe s si quieres sumar: ')

    # if add == 's':
    #     user_input = int(input('Escribe el numero: '))
    #     print(suma(user_input))
    # else:
    #     print('thanks for your time')    
    

    # for i in range(1, 100, 2):
    #     print(i)


    diccionario = {
        'ferrari': 10,
        'lambo': 9,
    }

    user_car = input('que marca prefieres: ')

    if user_car == 'f':
        for car, rate in diccionario.items():
            print(car, rate)


def suma(n):
    return n + 2 


if __name__ == "__main__":
    main()