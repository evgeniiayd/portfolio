import unittest
from calculate import calculate


class TestCalculate(unittest.TestCase):
    def test_mult_by_zero(self):
        assert calculate(0, 0, "*") == 0, "Неправильное условие с нулем"

    def test_fraction_power(self):
        assert calculate(4, 0.5, "^") == 2, \
            "Нужна функция, вычисляющая корень"

    def test_zero_divided_by(self):
        assert calculate(0, 5, "/") == 0, "Неправильное деление нуля"

    def test_multiple_actions(self):
        assert calculate(0, 7, "*/") == "Такой операции не существует", \
            "Неправильное условие с нулем"

    def test_second_operand_is_zero(self):
        assert calculate(5, 0, "-") == 5, "Неправильное положение условия с нулем"

    def test_mult_negative(self):
        assert calculate(-1, -1, "*") == 1, "Неправильное умножение негативных чисел"

    def test_sum_two_int(self):
        assert calculate(1, 2, "+") == 3, "Неверная сумма"

    def test_minus_neg_n(self):
        assert calculate(1, -1, "-") == 2, "Вычитание отрицательных чисел (по сути - сложение)"

    def test_div_by_zero(self):
        assert calculate(10, 0, "/") == "Деление на ноль невозможно", "Деление на ноль"

    def test_sum_two_float(self):
        assert calculate(1.0, 1.0, "+") == 2.0, "Неверная сумма чисел с плавающей точкой"

    def test_op2_invalid_type(self):
        assert calculate(1, "0", "+") == "Ошибка во втором операнде", "тип операнда int или float"

    def test_op1_invalid_type(self):
        assert calculate("1", 0, "+") == "Ошибка в первом операнде", "тип операнда int или float"


class TestTolerance(unittest.TestCase):
    def test_decimal_fraction(self):
        assert calculate(1, 15, "/", tolerance=0.001) == 0.067, \
            "Нет возможности ввести десятичную дробь"

    def test_large_precision(self):
        assert calculate(1, 15, "/", tolerance=15) == "Неверная точность", \
            "Точность меньше единицы"

    def test_unnecessary_parametr(self):
        assert calculate(1, 2, "/") == 0.5, \
            "Точность не обязательно вводить"


class TestMore(unittest.TestCase):
    def test_fraction_result(self):
        assert calculate(1, 2, "medium", (3, 0)) == 1.5, \
            "Не считает нулевые значения"

    def test_variance(self):
        assert calculate(-1, -1, "variance", (-1, -1)) == 0, \
            "Неправильно высчитанная дисперсия при отрицательных значениях"

    def test_deviation(self):
        assert calculate(15, 15, "std_deviation", (15, 15)) == 0, \
            "Неправильное вычисление корня в отклонении"

    def test_median(self):
        assert calculate(7, 5, "median", (1, 3, 4, 6, 2)) == 4, \
            "Вычисление медианы в неупорядоченном ряду"

    def test_interquartile_range(self):
        assert calculate(7, 5, "interquartile_range", (1, 3, 4, 6, 2, 8)) == 4, \
            "Межквартильный размах в ряду, деляющемся на 4"
