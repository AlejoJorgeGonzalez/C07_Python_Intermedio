def run():
    # squares = []

    # El range va a esta el numero - 1 que se le de
    # for i in range(1,101):
        # Agregamos al cuadrado el numero de la iteración
        # squares.append(i**2)

        #SOLUCIÓN RETO
        # if i % 3 != 0:
        #     squares.append(i**2)
    
    squares = [i**2 for i in range(1,101) if i % 3 != 0]

    list_nums = [i for i in range(1,100000) if (i % 4 == 0 
                                            and i % 6 == 0
                                            and i % 9 == 0)] 

    print(squares)

    print('list_nums: ', list_nums)

if __name__ == '__main__':
    run()