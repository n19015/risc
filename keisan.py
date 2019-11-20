import random

def bina():
    a = random.randrange(10, 200)
    b = format(a, 'b')
    print("\033[1A\r2進数を10進数に変換")
    print(b)
    c = int(input())
    if a == c:
        print("sucees")
    else:
        print("not")

def octo():
    a = random.randrange(10, 200)
    b = format(a, 'o')
    print("\033[1A\r8進数を10進数に変換")
    print(b)
    c = int(input())
    if a == c:
        print("sucess")
    else:
        print("not")

def hexy():
    a = random.randrange(10, 200)
    b = format(a, 'x')
    print("\033[1A\r16進数を10進数に変換")
    print(b)
    c = int(input())
    if a == c:
        print("sucess")
    else:
        print("not")

def ten():
    a = random.randrange(10, 200)
    e = random.randrange(1, 4)
    if e == 1:
        print("\033[1A\r２進数に変換")
        b = format(a, 'b')
        print(a)
        f = int(input())
        j = str(f)
        if j  == b:
            print("sucess")
        else:
            print("not")
    if e == 2:
        print("\033[1A\r８進数に変換")
        c = format(a, 'o')
        print(a)
        g = int(input())
        k = str(g)
        if c == k:
            print("sucesse")
        else:
            print("not")
    if e == 3:
        print("\033[1A\r１６進数に変換")
        d = format(a, 'x')
        print(a)
        h = (input())
        if d == h:
            print("sucesse")
        else:
            print("not")

print("２進数：１　８進数：２ １６進数：３ １０進数：４")
num = int(input())
if num == 1:
    bina()
elif num == 2:
    octo()
elif num == 3:
    hexy()
elif num == 4:
    ten()
