def run():
    # my_dict = {}

    # # Se guarda los valores del 1 al 100 al cubo
    # for i in range(1, 101):
    #     # Se excluyen los valores que son divisibles por 3
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dict)

    # RETO

    root_nums = {i: i ** (1/2) for i in range(1,1001)}
    print(root_nums)


if __name__ == '__main__':
    run()