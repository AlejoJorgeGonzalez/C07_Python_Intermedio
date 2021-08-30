# Base de datos de personas, recuerda que por convención cuando
# se coloca una variable en mayúsculas, estamos diciendo que es
# constante
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

# Función principal 
def run():
    # primera solución con list comprehensions
    all_python_devs = [worker['name'] for worker in DATA 
                        if worker['language'] == 'python']
    # Todos los trabajadores de platzi
    all_Platzi_devs = [worker['name'] for worker in DATA 
                        if worker['organization'] == 'Platzi']
    
    # Todos los adultos de la base de datos, pero esta vez con
    # la función filter, para obtener la información de los 
    # trabajadores mayores de 18 
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    # Filtramos para solo tener el nombre del trabajor, 
    # eliminando la demas información
    adults = list(map(lambda worker: worker['name'], adults))

    # Se crea una lista con la funcióion list que tiene por dentro
    # una función map, que a su vez recibe dos parametros, una
    # función y un iterable DATA, la función toma los valores 
    # de DATA y los tranforma en una nueva lista que agrega un 
    # diccionario con llave old y valor boleano dependiendo 
    # si es mayor a 70. Note que aparece un simbolo ** que siginifica
    # que suma un nuevo valor al diccionario, en python 3.9 se utiliza 
    # un |
    old_people = list(map(lambda worker: {**worker, 
                            **{'old': worker ['age'] > 70}}, DATA))
    # old_people = list(map(lambda worker: worker | 
    #                         {'old': worker ['age'] > 70}, DATA))                        

    # for worker in all_python_devs:
    # for worker in all_Platzi_devs:
    # for worker in adults:
    for worker in old_people:
        print(worker)

    # RETO
    # all_python_dev con filter y map
    all_python_devs = list(filter(lambda worker: 
                            worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker: worker['name'], 
                                all_python_devs))
    print('all_python_devs:')
    for worker in all_python_devs:
        print(worker)
    print('')

    # all_Platzi_workers con filter y map
    all_Platzi_devs = list(filter(lambda worker: 
                        worker['organization'] == 'Platzi', DATA))
    all_Platzi_devs = list(map(lambda worker: 
                                worker['name'], all_Platzi_devs))
    print('all_Platzi_devs:')
    for worker in all_Platzi_devs:
        print(worker)
    print('')

    # old_people con list comprehensions
    old_people = [{**worker, **{'old': worker['age'] > 70}} 
                    for worker in DATA]
    
    print('old_people:')
    for worker in old_people:
        print(worker)
    print('')

    # adults en list compregensions
    adults = [worker['name'] for worker in DATA 
                if worker['age'] > 18]
    print('adults:')
    for worker in adults:
        print(worker)
    print('')
    

# Punto de entrada del programa
if __name__ == "__main__":
    run()