immutable_var = 1, 'ghost', 32, True, 85.6
print(immutable_var)

#immutable_var[0] = 4  строка кода будет подчеркиваться, как ошибочная, так как кортеж константная коллекция
# и изменить ее элементы невозможно

mutable_list = [132, "cafe", False, 32.7, 23]
print(mutable_list)
mutable_list[4] = 42
mutable_list[1] = "coffee"
print(mutable_list)