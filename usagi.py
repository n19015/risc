import random

a = int(input("何回まわす？1~10 "))
if a <= 10:
    for i in range(a):
        #一文字ずつ取り出す関数
        word = random.sample(('さ', 'う', 'の', 'ぎ', 'く', 'に', 'れ', 'ば', 'な'), 9)
        print(''.join(word))
        #でない人用
elif a == 999:
    print("うさぎのにくばなれ")
else:
    print("お金がたりないよ")
