from random import randint
import json
import os


class InvalidData(Exception):
    pass


def console_input() -> list:
    # ValueError is possible
    return list(map(int, input("Your data(spaces in between):\n").split()))


def random_input(n: int) -> list:
    return [randint(-100, 100) for _ in range(n)]


def file_input() -> list:
    filename = input("File name(e.x. test.txt): ")
    if not os.path.exists("./" + filename):
        print("No such file")
        raise FileNotFoundError
    f = open(filename, "r")
    line = f.readline()
    f.close()
    try:
        a = json.loads(line)
    except json.decoder.JSONDecodeError:
        print("Invalid data in the file")
        raise ValueError

    return a
