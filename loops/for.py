numbers = list(range(1, 10))

for number in numbers:
    pass
#     print(f'{number}')


# Iterating by Sequence Index

fruits = ['apples', 'banana', 'mangoes', 'pineapples']

for index in range(len(fruits)):
    print(f'{index} - {fruits[index]}')



for i in range(9):
    if(i == 2):
        print('about to conti....')
        # continue
        break
    print(f'\n {i+11}')
print("shit broke")