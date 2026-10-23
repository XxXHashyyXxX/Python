#!/usr/bin/env python


def calculate(user_input: str) -> tuple[float, float] | None:
    try:
        value = float(user_input)
    except ValueError:
        print(f"Could not convert {user_input} to a number")
        return None

    third_power = value * value * value
    return (value, third_power)


def loop(end: str = "stop"):
    while True:
        user_input = input("Provide a number or type 'stop' to finish the execution")

        if user_input == end:
            print("Finishing the program")
            return

        values = calculate(user_input)
        if values is None:
            continue

        value = values[0]
        third_power = values[1]

        print(f"The number: {value}, the third power: {third_power}")


if __name__ == "__main__":
    loop()
