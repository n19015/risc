import sys, time, threading


lis = ['-', '\\', '|', '/'] # ギミック
right = True


def fnc(): # 別のスレッドで終了フラグの管理
    global right
    time.sleep(5)
    right = False


thread = threading.Thread(target=fnc)
thread.start()
while right:
    for num in lis:
        sys.stdout.write("\rNowloading...{}".format(num))
        # printだと強制改行になるのでsysで代用
        # \rで行頭に移動そしてもう一度同じ行に出力
        sys.stdout.flush()
        # バッファリングをしないコード
        time.sleep(0.1)


print("\r\033[Khoge") # ここをアンコメントするとloadingを消しながらprintされる
# print("\nhoge") # ここをアンコメントするとloadingを残してprintされる
