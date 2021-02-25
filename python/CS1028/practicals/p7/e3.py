# Author: Zsolt Kébel
# Date: 18/11/2020

total = 0


def read_in_num():
    global total

    try:
        text = input()
        if text == "":
            return

        num = float(text)

        total += num
        print(total)
    except ValueError:
        print("Not a valid number")

    read_in_num()


read_in_num()
