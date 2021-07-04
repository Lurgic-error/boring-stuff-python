dic = {'name':'joji', 'age':334}

print(dic['name'])

print(dic.get('age'))


print('name' in dic)

for item in dic.items():
    print(item)

for key in dic.keys():
    print(f'key ===> {key}')


for value in dic.values():
    print(f"{value}")