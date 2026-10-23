#!/usr/bin/env python


def solution_with_for():
    for num in range(31):
        if num % 3 != 0:
            print(num)


def solution_with_while():
    num = 0
    while num <= 30:
        if num % 3 != 0:
            print(num)
        num += 1


if __name__ == "__main__":
    print("--- Solution with for: ---")
    solution_with_for()

    print("--- Solution with while: ---")
    solution_with_while()
