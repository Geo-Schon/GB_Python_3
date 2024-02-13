"""
1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
- Какие вещи взяли все три друга
- Какие вещи уникальны, есть только у одного друга
- Какие вещи есть у всех друзей кроме одного + имя того, у кого данная вещь отсутствует
- Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""
my_dict = {"Ира": ('палатка', 'спальный мешок', 'рюкзак'),
           "Борис": ('рюкзак', 'кружка', 'фонарик'),
           "Виктор": ('палатка', 'палка', 'фонарик', 'рюкзак')}
my_set = set(list(my_dict.values())[0])
print(my_set)
for elment in my_dict.values():
    my_set = my_set.intersection(set(elment))
print(my_set)
new_dict = {}
for value in my_dict.values():
    for item in value:
        if item not in new_dict:
            new_dict[item] = 0
        new_dict[item] += 1
    for key, value in new_dict.items():
        if value == 1:
            print(f'{key} есть только у одного')
    for key, value in new_dict.items():
        if value == 2:
            print(f'{key} есть только у двоих')
            for name, goods in my_dict.items():
                if key not in goods:
                    print(f'{name} не имеeт {key}')
                    break