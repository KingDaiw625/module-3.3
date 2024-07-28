def print_params(a=1, b='строка', c=True):
    print(a, b, c)


value_list = (2, 'слово', False)
value_dict = {'a': 3, 'b': 'два слова', 'c': True}
value_list_2 = (4, 'пять')

print_params()
print_params(a=2, b='слово')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*value_list)
print_params(**value_dict)
print_params(*value_list_2, 42)
