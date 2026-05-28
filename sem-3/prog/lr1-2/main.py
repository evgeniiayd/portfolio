from calculate import calculate


def main():
    """
    Function as a user's interface

    Return an answer
    """
    print("Введите первое число: ")
    x = float(input())
    print("Введите второе число: ")
    y = float(input())
    print("Введите тип операции: ")
    z = str(input())
    print("Введите точность вычисления (по умолчанию 1e-6)")
    tolerance = input()
    print("Введите дополнительные числа через запятую(при надобности)")
    arr = input()
    if arr != "":
        arr = tuple(map(float, arr.split(',')))
    if not tolerance:
        res = calculate(x, y, z, arr)
    else:
        res = calculate(x, y, z, arr, tolerance=tolerance)
    print("Ответ: ", res)


if __name__ == '__main__':
    main()
