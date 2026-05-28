def guess_number(number, low, up):
    """
    Arguments:
        number -- number that the program should guess
        low -- lower bound of an interval
        up -- upper bound of an interval

    Return the guessed number and a number of guessing attempts
    """
    count = 0
    for i in range(low, up, 1):
        count += 1
        if i == number:
            print(f"Ваше число: {x}! Количество попыток угадывания - {count}")
            break


print("Введите число")
x = int(input())
print("Введите нижнюю границу интервала, в котором загадано число")
y = int(input())
print("Введите верхнюю границу интервала, в котором загадано число")
z = int(input())

guess_number(x, y, z)
