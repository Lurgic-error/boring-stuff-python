import sys 

def fibo(n):
    a, b, counter = 0, 1, 0

    while True: 
        if(counter > n):
            return
        print(f'a ===> {a}')
        yield a
        a, b, = b, a + b
        counter += 1


f = fibo(50)

while True:
    try:
        print(f"yeilded ===> {next(f)}")

    except StopIteration:
        sys.exit()