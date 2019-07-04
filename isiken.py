import random

print("じゃんけんしようよ。 最初はグー ジャンケンポン")
while True:
    a = input("g: グー t:チョキ p:パー ")
    if a == "g":
        num = random.randint(1, 3)
        if num == 1:
            print("グー。あいこだねもう一度やるよ。")
        elif num == 2:
            print("チョキ。あーあ負けちゃった。もう一回やろうよ。")
        elif num == 3:
            print("パー。 僕の勝ちだねもう一度勝負だ。")
    elif a == "t":
        num = random.randint(1, 3)
        if num == 1:
            print("グー。 僕の勝ちだねもう一度勝負だ。")
        elif num == 2:
            print("チョキ。あいこだねもう一度やるよ。")
        elif num == 3:
            print("パー。あーあ負けちゃった。もう一回やろうよ。")
    elif a == "p":
        num = random.randint(1, 3)
        if num == 1:
            print("グー。あーあ負けちゃった。もう一回やろうよ。")
        elif num == 2:
            print("チョキ。僕の勝ちだねもう一度勝負だ。")
        elif num == 3:
            print("パー。あいこだねもう一度やるよ。")
    else:
        print("ちゃんとじゃんけんしてよ。もう一度やるよ。")
        print("最初はグー ジャンケンポン")
