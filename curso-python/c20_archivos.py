def read():
    numbers = []
    # Llamamos el archivo de los números, note que se agrega
    # un encoding de utf-8 con el fin de tener caracteres
    # especiales
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        # Se recorre cada linea del archivo numbers.txt
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['facundo', 'Miguel', 'Pepe', 'Christian', 'Rocío']
    with open('./archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            # El método write permite escribir sobre el archivo
            f.write(name)
            f.write('\n')


def run():
    #read()
    write()


if __name__ == '__main__':
    run()