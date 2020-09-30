def run():
    objective = int(input("reply: "))
    reply = 0

    while reply**2 < objective:
        print(reply)
        reply += 1

    if reply**2 == objective:
        print(f'La raiz cuadrada de {objective} es {reply}')
    else:
        print(f'{objective} does not have a Root square...')    


if __name__ == "__main__":
    run()