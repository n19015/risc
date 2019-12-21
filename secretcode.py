kont = []
item = input('文字を入力してください。')
for i in range(len(item)):
    ints = ord(item[i])  # アスキーコードに変換
    binary = '{:b}'.format(ints)  # ２進数に変換
    hexs = format(int(binary, 2), 'x')   # ２進数を１０進数に変換して１６進数に変換
    lis = hexs.split()
    code = kont.append(hexs)
print("".join(map(str, kont)))
