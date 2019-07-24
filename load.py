import sys
import time

lis = ['-', '\\', '|', '/'] # ギミック
while True:
    for num in lis:
        sys.stdout.write("\rNowloading...{}".format(num))
        # printだと強制改行になるのでsysで代用
        # \rで行頭に移動そしてもう一度同じ行に出力
        sys.stdout.flush()
        # バッファリングをしないコード
        time.sleep(0.1)
