#Работа со словарями
my_dict = {'Иван':2000, 'Екатерина':1995, 'Сергей':1999}
print(my_dict)

print(my_dict.get('Сергей'))
print(my_dict.get('Евгения'))

my_dict ['Анастасия'] = 2001
my_dict ['Светлана'] = 1980

del my_dict ['Екатерина']
print (my_dict.get('Екатерина', 'Такого ключа нет'))

print(my_dict)


#Работа с множествами
my_set = {1, 2, 2, 1.3, 1.3, 1.5, 'Hello', 'Hello', False, (1, 2, 3)}
print(my_set)

print(my_set.add(5))
print(my_set.add('Bye'))
print(my_set.remove(1.3))
print(my_set)