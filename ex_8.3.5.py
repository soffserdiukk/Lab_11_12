import math


def calculate_sequence_element(x, k):
    """Обчислення елемента послідовності x_k = x^(2k)/(2k)!"""
    numerator = x ** (2 * k)
    denominator = math.factorial(2 * k)
    return numerator / denominator


def calculate_product(n):
    """Обчислення добутку P_n = (1 + 1/1²)*(1 + 1/2²)*...*(1 + 1/n²)"""
    product = 1.0
    for i in range(1, n + 1):
        term = 1 + 1 / (i ** 2)
        product *= term
    return product


def calculate_determinant(n, a, b):
    """Обчислення визначника тридіагональної матриці"""
    if n == 1:
        return a + b
    elif n == 2:
        return (a + b) ** 2 - a * b

    d_prev_prev = a + b
    d_prev = (a + b) ** 2 - a * b

    for i in range(3, n + 1):
        d_current = (a + b) * d_prev - a * b * d_prev_prev
        d_prev_prev, d_prev = d_prev, d_current

    return d_prev


def calculate_sum(n):
    """Обчислення суми S_n = sum(a_k/2^k) з рекурентною послідовністю"""
    if n == 0:
        return 0.0

    a = [0] * (n + 1)
    a[1] = a[2] = a[3] = 1

    for k in range(4, n + 1):
        a[k] = a[k - 1] + a[k - 3]

    total = 0.0
    for k in range(1, n + 1):
        total += a[k] / (2 ** k)

    return total


def taylor_ln_function(x, epsilon=1e-6):
    """Обчислення ln((1+x)/(1-x)) за допомогою ряду Тейлора"""
    if abs(x) >= 1:
        raise ValueError("|x| має бути менше 1")

    result = 0.0
    k = 1
    while True:
        term = 2 * (x ** k) / k
        result += term

        if abs(term) < epsilon:
            break

        k += 2

    return result


def main():
    """Головна функція для обчислення всіх завдань та запису результатів"""
    with open('output_file_8.3.5.txt', 'w', encoding='utf-8') as f:
        # Завдання a)
        f.write("Завдання a) Обчислення елементів послідовності:\n")
        x_a = 2.5
        for k in range(0, 5):
            result = calculate_sequence_element(x_a, k)
            f.write(f"x_{k} = {result:.6f}\n")
        f.write("\n")

        # Завдання b)
        f.write("Завдання b) Обчислення добутку:\n")
        n_b = 5
        result = calculate_product(n_b)
        f.write(f"P_{n_b} = {result:.6f}\n\n")

        # Завдання c)
        f.write("Завдання c) Обчислення визначника:\n")
        n_c, a_c, b_c = 4, 2.0, 3.0
        result = calculate_determinant(n_c, a_c, b_c)
        f.write(f"Визначник порядку {n_c} (a={a_c}, b={b_c}) = {result:.6f}\n\n")

        # Завдання d)
        f.write("Завдання d) Обчислення суми:\n")
        n_d = 10
        result = calculate_sum(n_d)
        f.write(f"S_{n_d} = {result:.6f}\n\n")

        # Завдання e)
        f.write("Завдання e) Обчислення функції ln((1+x)/(1-x)):\n")
        x_e = 0.5
        epsilon = 1e-8
        our_result = taylor_ln_function(x_e, epsilon)
        exact_result = math.log((1 + x_e) / (1 - x_e))
        f.write(f"Наше обчислення: {our_result:.8f}\n")
        f.write(f"Точне значення:  {exact_result:.8f}\n")
        f.write(f"Різниця:         {abs(our_result - exact_result):.2e}\n")


if __name__ == "__main__":
    main()
    print("Результати записано у файл 'output_file_8.3.5.txt'")