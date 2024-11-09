def print_params(a = 1, b= 'string', c = True):
    print(a, b, c)

print_params()
print_params(a = 2, b= 'Строка', c = False)
print_params(b = 25)
print_params(c = [1, 2 ,3])

values_list = (2, 'Value', False)
values_dict = {'a' : 3, 'b' : "dict", 'c' : False}

print_params(*values_list)
print_params(**values_dict)

values_list2 = ('True', False)
print_params(*values_list2, 42)
