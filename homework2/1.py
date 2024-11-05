def infinite_loop(func):
    """Декаратор"""
    def wrapper(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                print(result)
            except ValueError:
                print("Error! Please enter integers")
            continue_loop = input("Contienue (yes/no)?")
            if continue_loop.lower() != "yes":
                break
        return wrapper


@infinite_loop
def sum_of_two_numbers():
    num1 = int(input("Напиши первое число: "))
    num2 = int(input("Напиши второе число: "))
    return f"Cумма чисел: {num1 + num2}"


def main():
    sum_of_two_numbers()


if __name__ == '__main__':
    main()
