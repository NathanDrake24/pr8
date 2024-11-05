def summa():
    total_sum = 0

    while True:
        user_input = input("Введите число (или 'stop'/'end' для завершения): ")

        if user_input.lower() in ["stop", "end"]:
            print(f"Сумма всех введенных чисел: {total_sum}")
            print("Завершение программы.")
            break

        try:
            number = float(user_input)
            total_sum += number
            print(f"Текущая сумма: {total_sum}")
        except ValueError:
            print("Ошибка: введите число или 'stop'/'end' для выхода.")


def main():
    summa()


if __name__ == '__main__':
    main()