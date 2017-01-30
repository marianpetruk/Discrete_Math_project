import re

def B(n):
    if n > 20 or n < 0:
        return "BIG"
    sum = 0
    try:
        for i in range(n + 1):
            sum += S(n, i)
        return sum
    except:
        return "INVALID"


def S(n, k):
    if k > n:
        return "ERR"
    if n > 20 or k > 20 or n < 0 or k < 0:
        return "BIG"
    if k == n:
        return 1
    if n > 0 and k == 0:
        return 0
    return S(n - 1, k - 1) + k * S(n - 1, k)


def main(s, lg):
    start = s + "="
    s = s.replace("b", "B")
    s = s.replace("s", "S")
    bell = re.compile('B\(-*\d+\)')
    stirling = re.compile('S\(-*\d+,\s*-*\d+\)')
    res_bell = bell.findall(s)
    res_stirling = stirling.findall(s)
    for elem in res_bell:
        val = str(eval(elem))
        s = s.replace(elem, val, 1)
    for elem in res_stirling:
        val = str(eval(elem))
        s = s.replace(elem, val, 1)
    if len(s) > 75:
        return None, ["Result contains more than 75 symbols", "Результат містить більше 75 знаків"][lg]
    if s.find("ERR") != -1:
        return None, ["n can`t be bigger than k", "n не може бути більшим за k"][lg]
    if s.find("BIG") != -1:
        return None, ["n(k) can`t be bigger than 20 or smaller than 0", "n(k) не може бути більшим за 20 чи меншим 0"][lg]
    try:
        res = str(eval(s))
        return [start, res if s != res else "", s.replace(" ", "") + "="], None
    except:
        return None, ["Incorrect expression", "Некорентий вираз"][lg]


