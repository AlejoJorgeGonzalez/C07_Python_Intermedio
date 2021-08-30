def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():
    num = input('Ingresa un número: ')
    # Se agrega el assert, en el cuál agregamos la función 
    # de python isnumeric que no va a evaluar si un valor es 
    # númerico, es de anotar que se evalua un string, si esto
    # nos da verdadero este string se convierte en número
    assert num.isnumeric(), 'Debes ingresar un número positivo'
    num = int(num)
    assert num > 0, 'Debes ingresar un número positivo'
    print(divisor(num))
    print('Terminó mi programa')
   

if __name__ == '__main__':
    run()