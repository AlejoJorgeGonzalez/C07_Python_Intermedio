def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():
    try:
        num = int(input('Ingresa un número: '))
        try:
            if num <= 0:
                raise ValueError('Ingresar un número positivo')
            print(divisor(num))
            print('Terminó mi programa')
        except ValueError as ve:
            print(ve)
    except ValueError:
        print('Debes ingresar un número')


if __name__ == '__main__':
    run()