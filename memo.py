import sys


def gameframe():
    for i in range(21):
        sys.stdout.write("-")
    print()
    for i in range(5):
        sys.stdout.write("|")
        sys.stdout.write("\033[19C")
        print("|")
    for i in range(21):
        sys.stdout.write("-")
    print()


def iput():
    sys.stdout.write("\033[6A")
    for i in range(5):
        sys.stdout.write("\033[1C")
        mozi = input()
        if len(mozi) > 19:
            sys.stdout.write("\033[1F")
            sys.stdout.write("\033[20C")
            sys.stdout.write("\033[K")
            print("|")
    sys.stdout.write("\033[5B")


gameframe()
iput()
