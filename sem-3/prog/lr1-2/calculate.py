def convert_precision(tolerance):
    """
    Argument:
        tolerance -- precision for calculation answer

    Return a number of digits after a coma
    """
    tolerance = float(tolerance)
    if (tolerance <= 0) or (tolerance >= 1):
        return "Неверная точность"
    order = 0
    while tolerance != 1:
        tolerance = tolerance * 10
        order += 1
    return order


def calculate(first, second, action, *args, tolerance=1e-6):
    """
    Execute calculation such as: addition(+), subtraction(-), multiplication(*),
    division(/), exponentiation(^), medium, variance, std_deviation, median,
    interquartile_range

    Arguments:
        first -- first number, float
        second -- second number, float
        action -- action indication, string
        args -- more numbers (unnecessary)
        tolerance -- degree of accuracy

    Return result of chosen calculation method
    """
    precision = convert_precision(tolerance)
    list_of_args = list(*args)
    result = 0
    if type(precision) is str:
        return precision
    if type(first) is str:
        return "Ошибка в первом операнде"
    elif type(second) is str:
        return "Ошибка во втором операнде"
    elif second == 0 and action == "/":
        return "Деление на ноль невозможно"
    elif action == "+":
        result = first + second
    elif action == "-":
        result = first - second
    elif action == "*":
        result = first * second
    elif action == "^":
        result = first ** second
    elif action == "/":
        result = first / second
    elif action == "medium" or action == "variance" or action == "std_deviation":
        sum_args = 0
        i = 0
        for i in list_of_args:
            sum_args += i
        result = (first + second + sum_args)/(2 + len(list_of_args))
        if action == "variance" or action == "std_deviation":
            t = (first - result)
            t = t * t
            sum_variance = t
            t = (second - result)
            t = t * t
            sum_variance += t
            for i in list_of_args:
                t = i - result
                sum_variance += t * t
            result = sum_variance/(len(list_of_args) + 1)
            if action == "std_deviation":
                result = result ** 0.5
    elif action == "median" or action == "interquartile_range":
        list_of_args.append(first)
        list_of_args.append(second)
        for j in range(0, len(list_of_args)-1, 1):
            for i in range(j+1, len(list_of_args), 1):
                if list_of_args[j] > list_of_args[i]:
                    p = list_of_args[j]
                    list_of_args[j] = list_of_args[i]
                    list_of_args[i] = p
        if action == "median":
            if len(list_of_args) % 2 == 1:
                result = list_of_args[len(list_of_args) // 2]
                return result
            if len(list_of_args) % 2 == 0:
                result = (list_of_args[len(list_of_args) // 2] + list_of_args[len(list_of_args) // 2 - 1])/2
                return result
        else:
            remaining_length = 0
            if len(list_of_args) % 2 == 1:
                remaining_length = (len(list_of_args) - 1) // 2
            if len(list_of_args) % 2 == 0:
                remaining_length = len(list_of_args) // 2
            if remaining_length % 2 != 0:
                first_position = remaining_length // 2
                second_position = (len(list_of_args) - 1) - first_position
                q1 = list_of_args[first_position]
                q3 = list_of_args[second_position]
                result = q3 - q1
                return result
            if remaining_length % 2 == 0:
                second_position = remaining_length // 2
                first_position = second_position - 1
                q1 = (list_of_args[first_position] + list_of_args[second_position])/2
                third_position = len(list_of_args) - second_position
                forth_position = third_position - 1
                q3 = (list_of_args[forth_position] + list_of_args[third_position]) / 2
                result = q3 - q1
                return result
    else:
        return "Такой операции не существует"
    result = round(result, precision)
    return result
