import random

a = int(input("何回まわす？1~10 "))
if a <= 10:
    for i in range(a):
        word = random.sample(('さ', 'う', 'の', 'ぎ', 'く', 'に', 'れ', 'ば', 'な'), 9)
        print(''.join(word))
elif a == 999:
    print("うさぎのにくばなれ")
else:
    print("お金がたりないよ")
