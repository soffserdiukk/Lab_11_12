class RationalError(ZeroDivisionError):
    """Клас виключення для помилок у раціональних числах, пов'язаних із нульовим знаменником"""

    def __init__(self, message="Знаменник раціонального числа не може бути нулем"):
        self.message = message
        super().__init__(self.message)


class RationalValueError(ValueError):
    """Клас виключення для некоректних операцій з раціональними числами"""

    def __init__(self, message="Некоректна операція з раціональним числом"):
        self.message = message
        super().__init__(self.message)


class Rational:
    """Клас для роботи з раціональними числами"""

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise RationalError()
        self.numerator = numerator
        self.denominator = denominator
        self._normalize()

    def _normalize(self):
        """Скорочення дробу та нормалізація знаку"""
        gcd_value = self._gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= gcd_value
        self.denominator //= gcd_value

        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    @staticmethod
    def _gcd(a, b):
        """Обчислення найбільшого спільного дільника"""
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        if not isinstance(other, Rational):
            try:
                other = Rational(other)
            except (TypeError, ValueError):
                raise RationalValueError("Можна додавати тільки раціональні числа або цілі числа")

        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            try:
                other = Rational(other)
            except (TypeError, ValueError):
                raise RationalValueError("Можна множити тільки раціональні числа або цілі числа")

        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


class RationalList(list):
    """Клас списку раціональних чисел з перевіркою типів"""

    def append(self, item):
        if not isinstance(item, Rational):
            try:
                item = Rational(item)
            except (TypeError, ValueError, RationalError):
                raise RationalValueError(
                    "Можна додавати тільки раціональні числа або числа, які можна конвертувати в раціональні")
        super().append(item)

    def extend(self, items):
        for item in items:
            self.append(item)

    def __add__(self, other):
        new_list = RationalList(self)
        new_list.append(other)
        return new_list

    def __iadd__(self, other):
        self.append(other)
        return self


def main():
    """Головна функція для демонстрації роботи класів та запису результатів у файл"""
    with open('output_ex_7.3.1-3.txt', 'w', encoding='utf-8') as f:
        # Тестування RationalError
        f.write("1. Тестування RationalError:\n")
        try:
            f.write("Спроба створити Rational(1, 0):\n")
            r = Rational(1, 0)
        except RationalError as e:
            f.write(f"Помилка: {e}\n\n")

        # Тестування RationalValueError при додаванні
        f.write("2. Тестування RationalValueError при додаванні:\n")
        try:
            f.write("Спроба додати Rational(1, 2) + 'abc':\n")
            r1 = Rational(1, 2)
            r2 = r1 + "abc"
        except RationalValueError as e:
            f.write(f"Помилка: {e}\n\n")

        # Тестування RationalValueError у RationalList
        f.write("3. Тестування RationalValueError у RationalList:\n")
        try:
            f.write("Спроба додати 'xyz' до RationalList:\n")
            r_list = RationalList()
            r_list.append("xyz")
        except RationalValueError as e:
            f.write(f"Помилка: {e}\n\n")

        # Приклад коректного використання
        f.write("4. Приклади коректного використання:\n")
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        f.write(f"  - {r1} + {r2} = {r1 + r2}\n")

        r_list = RationalList()
        r_list.append(r1)
        r_list.append(2)  # ціле число буде конвертовано в Rational(2, 1)
        f.write(f"  - Список раціональних чисел: {[str(x) for x in r_list]}\n")


if __name__ == "__main__":
    main()
    print("Результати записано у файл 'output_ex_7.3.1-3.txt'")