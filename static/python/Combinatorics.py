import math


def combinations(n, m, r, lg):
    """
    (int, int, str, int) -> int, str

    Computes combinations with and without repetitions.

    Argument lg means language:
    0 - english
    1 - ukrainian (українська)

    >>> combinations(5, 2, "no", 0)
    10, 'Combination of 5 things taken 2 at a time = 10'
    >>> combinations(5, 2, "yes", 0)
    15, 'Combination of 6 things taken 2 at a time = 15'
    >>> combinations(100, 5, "no", 0)
    75287520, '
Combination of 100 things taken 5 at a time = 75287520'
    >>> combinations(100, 5, "yes", 0)
    91962520, 'Combination of 104 things taken 5 at a time = 91962520'

    """
    if r == "no":
        if (m > n):
            return None, "!!! m < n !!!"
        if m == n:
            if lg == 0:
                return 1, "Combination of " + str(n) + " things taken " + str(m) + " at a time = " + str(1)
            elif lg == 1:
                return 1, "Комбінація з " + str(n) + " елементів по " + str(m) + " = " + str(1)

        if lg == 0:
            return int(math.factorial(n) / (math.factorial(m) * math.factorial(n-m))), "Combination of " + str(n) + " things taken " + str(m) + " at a time = " + str(int(math.factorial(n) / (math.factorial(m) * math.factorial(n-m))))
        elif lg == 1:
            return int(math.factorial(n) / (math.factorial(m) * math.factorial(n-m))), "Комбінація з " + str(n) + " елементів по " + str(m) + " = " + str(int(math.factorial(n) / (math.factorial(m) * math.factorial(n-m))))
    elif r == "yes":
        return combinations(n+m-1, m, "no", lg)
    return None


def permutations(n, m, r, lg):
    """
    (int, int, str, int) -> int, str

    Computes permutations with and without repetitions.

    Argument lg means language:
    0 - english
    1 - ukrainian (українська)

    >>> permutations(5, 2, "no", 0)
    20, '2-permutations of 5 without repetitions = 20'
    >>> permutations(5, 2, "yes", 0)
    25, '2-permutations of 5 with repetitions = 25'
    >>> permutations(100, 5, "no", 0)
    9034502400, '5-permutations of 100 without repetitions = 9034502400'
    >>> permutations(100, 5, "yes", 0)
    10000000000, '5-permutations of 100 with repetitions = 10000000000'

    """
    if r == "no":
        if (m > n):
            return None, "!!! m < n !!!"
        if n == m:
            if lg == 0:
                return int(math.factorial(n)), str(m) + "-permutations of " + str(n) + " without repetitions = " + str(int(math.factorial(n)))
            elif lg == 1:
                return int(math.factorial(n)), str(m) + "-розміщення з " + str(n) + " без повторень = " + str(int(math.factorial(n)))
        if lg == 0:
            return int(math.factorial(n) / math.factorial(n-m)), str(m) + "-permutations of " + str(n) + " without repetitions = " + str(int(math.factorial(n) / math.factorial(n-m)))
        elif lg == 1:
            return int(math.factorial(n) / math.factorial(n-m)), str(m) + "-розміщення з " + str(n) + " без повторень = " + str(int(math.factorial(n) / math.factorial(n-m)))
    elif r == "yes":
        if lg == 0:
            return n ** m, str(m) + "-permutations of " + str(n) + " with repetitions = " + str(n ** m)
        elif lg == 1:
            return n ** m, str(m) + "-розміщення з " + str(n) + " із повтореннями = " + str(n ** m)
    return None


def main(m, n, order, repeat, lg):
    """
    (int, int, str, str) -> str

    Computes combinatorics:
    combinations and permuatitions

    >>> main(5, 100, "yes", "yes", 0)
    10000000000, '5-permutations of 100 with repetitions = 10000000000'
    >>> main(2, 5, "no", "yes", 0)
    15, 'Combination of 6 things taken 2 at a time = 15'

    """
    if type(eval(m)) != int or type(eval(n)) != int:
        if lg == 0:
            return None, "Enter an integer number"
        elif lg == 1:
            return None, "Введіть натуральне число"
    n = eval(n)
    m = eval(m)
    if n < 1:
        if lg == 0:
            return None, "Enter n > 1"
        elif lg == 1:
            return None, "Введіть n > 1"
    if order == "no":
        answer, result = combinations(n, m, repeat, lg)
    elif order == "yes":
        answer, result = permutations(n, m, repeat, lg)
    else:
        answer, result = None, None
    return answer, result, None
