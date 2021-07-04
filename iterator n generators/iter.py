list = list(range(1,21))

itera = iter(list)

# for i in itera:
#     print(i)


import sys

while True: 
    try:
        print(f"next ==> {next(itera)}")
    
    except StopIteration:
        sys.exit()