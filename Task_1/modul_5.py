'''
Задание № 5
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
'''

__all__ = ['print_desc']

desc = 'Задание № 5 \
Добавьте в модуль с загадками функцию, которая хранит словарь списков. \
Ключ словаря - загадка, значение - список с отгадками. \
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.'

liric = 'Там лес и дол видений полны; \
Там о заре прихлынут волны \
На брег песчаный и пустой,'

def print_desc():
    print(desc)

def print_liric():
    print(liric)

if __name__ == '__main__':
    print_desc()