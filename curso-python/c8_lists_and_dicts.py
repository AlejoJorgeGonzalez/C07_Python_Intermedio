def run():
    # Las listas se escribe dentro de corchetes
    my_list = [1, "Hello", True, 4.5]
    # Los diccionarios se escriben dentro de llaves
    my_dict = {"firstname": "Facundo", "lastname": "García"}

    # Se pueden crear listas que dentro de estas sean 
    # diccionarios
    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "García"}
    ]

    # Tambien se puede crear diccionarios que dentro de estas
    # sean listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    # Recuerda que para obtener llaves y valores dentro de un
    # diccionario, se escribe el metodo items
    for key, value in super_dict.items():
        print(key, "-", value)

    # Recuerda que para obtener llaves y valores dentro de un
    # diccionario, se escribe el metodo items
    for value in super_list:
        print(value)


if __name__ == '__main__':
    run()