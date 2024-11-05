def print_numbers_beetwen(a, b):
    if a < b:
        for i in range(a + 1, b):
            print(i, end=" ")
        else:
            for i in range(b + 1, a):
                print(i, end=" ")


def main():
    a = int(input("Введите первое число(а): "))
    b = int(input("Введите второе число(b): "))
    print_numbers_beetwen(a, b)


if __name__ == '__main__':
    main()