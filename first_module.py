name = "Dima"
surname = "Arnautov"


def get_sum(a, b):
    '''
    get sum from two numbers
    '''
    return a + b
print(get_sum(5, 10))

a = input("Введите первое число: ")
b = input("Введите второе число: ")
print(get_sum(int(a), int(b)))