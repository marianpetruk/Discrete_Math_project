def fibo(n, lg):
    n = int(n)
    if abs(n) > 1000:
        return None, ["n not bigger than 1000", "n не більша за 1000"][lg]
    try:
        res = int(round((((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / 5 ** 0.5, 1))
        return res, None
    except:
        return None, ["Please, enter a number", "Будь ласка, введіть число"][lg]


