global a

a = 3

print(f'print at the start, a = {a}')

def test_global():
    a = 5
    print(f'print in the func, a = {a}')
    return

test_global()

print(f'print at the end, a = {a}')




b = 3

print(f'print at the start, b = {b}')

def test_global():
    global b
    b = 5
    print(f'print in the func, b = {b}')
    return

test_global()

print(f'print at the end, b = {b}')