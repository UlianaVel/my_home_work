calls = -1
def count_calls():
    global calls
    calls +=1
    return (calls)


def string_info():
    string = input('введите значение строки string функции string_info: ')
    string_tuple = (len(string), string.upper(), string.lower())
    print(string_tuple)
    count_calls()


def is_contains():
    string = input('введите значение строки string функции is_contains: ')

    ist_to_search = []
    n = int(input('введите количество элементов списка ist_to_search: '))

    for i in range(n):
        ist_to_search.append(input(f'введите значение {i+1} элемента списка ist_to_search: '))
        i +=1

    if string in ist_to_search:
        is_contains_ = True
    else:
        is_contains_ = False


    #print(ist_to_search)
    print(is_contains_)
    count_calls()


a = int(input('введите количество вызовов функции string_info: '))
for i in range(a):
    string_info()
    i +=1

b = int(input('введите количество вызовов функции is_contains: '))
for i in range(b):
    is_contains()
    i +=1

print(count_calls())
