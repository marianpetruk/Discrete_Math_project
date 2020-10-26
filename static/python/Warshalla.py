import copy
from string import ascii_letters


def read_file(smatrix, lg):
    '''
    (str) -> dict
    '''
    dmatrix = {}
    bCheckIsFirstEl = False
    bCheckIsSecondEl = False
    stringF = ''
    stringS = ''
    inuml = 0
    inumr = 0
    bstartmatrix = False
    endmatrix = False

    for el in smatrix:
        if el == ' ' or endmatrix:
            continue
        elif el in ascii_letters or el.lower() in 'йцукенгшщзхїфівапролджєячсмитью':
            return ["  Your input is incorrect. Please don\'t use letters and try again.",
                    "  Ваш ввід некоректний. Не використвуйте букви та спробуйте ще раз."][lg]
        elif el == '(':
            bCheckIsFirstEl = True
            bCheckIsSecondEl = False
            inuml += 1
            bstartmatrix = True
            endmatrix = False
        elif not bstartmatrix:
            if (el != '{') and (el != '(') and (el != '['):
                return ["  Your input is incorrect. Please check is your input starts with '(', '{' or '[' .",
                    "  Ваш ввід некоректний. Будь ласка перевірте чи ваш ввід починається '(', '{' або '['."][lg]

        elif bCheckIsFirstEl and el != ',' and el != ')':
            stringF += el
        elif el == ',':
            if bCheckIsFirstEl or not bCheckIsSecondEl or inuml - inumr <= 1:
                bCheckIsFirstEl = False
                bCheckIsSecondEl = True
            else:
                return ["  Your input is incorrect. You may miss ',' between numbers. Please try again.",
                        "  Ваш ввід некоректний. Можливо ви пропустили ',' між цифрами. Спробуйте ще раз."][lg]
        elif bCheckIsSecondEl and el != ')':
            if inuml > 0:
                stringS += el
        elif el == ')' and not endmatrix:
            inumr += 1
            endmatrix = True
            if inuml >= inumr:
                if stringF != '' and stringS != '':
                    if int(stringF) > 9 or int(stringS) > 9:
                        return ["  Your input is incorrect. Your input integer is bigger than 9. ",
                            "  Ваш ввід некоректний. Найбільше число вашого вводу перевищує 9. "][lg]
                    elif int(stringF) < 1 or int(stringS) < 1:
                        return ["  Your input is incorrect. Your input integer is negative or 0. ",
                            "  Ваш ввід некоректний. Найменше число вашого вводу менше 1. "][lg]
                    if int(stringF) in dmatrix:
                        if int(stringS) not in dmatrix[int(stringF)]:
                            dmatrix[int(stringF)].append(int(stringS))

                    else:
                        dmatrix[int(stringF)] = [int(stringS), ]
                    stringF = ''
                    stringS = ''
                else:
                    return ["  Your input is incorrect. You may miss number or some of them. Please try again.",
                            "  Ваш ввід некоректний. Можливо ви пропустили яке-небудь число. Спробуйте ще раз."][lg]
            else:
                return ["  Your input is incorrect. Please check '(' and ')'.",
                        "  Ваш ввід некоректний. Перевірте '(' і ')'."][lg]
        else:
            return ["  Your input is incorrect. Please try again.",
                    "  Ваш ввід некоректний. Спробуйте ще раз."][lg]
    return dmatrix


def print_matrix(dmat):
    '''
    (dict) -> list
    '''
    dpmmat = {}
    lmat = []
    pmmin = min(dmat)
    pmmax = max(dmat)
    for key in sorted(dmat):
        lmat += dmat[key]
        lmat.append(key)
        dpmmat[key] = sorted(dmat[key])
        if dpmmat[key][0] < pmmin:
            pmmin = dpmmat[key][0]
        if dpmmat[key][-1] > pmmax:
            pmmax = dpmmat[key][-1]
    n = pmmax
    lmatrix2 = [[0] * n for _ in range(n)]
    for key in dpmmat:
        for el in dpmmat[key]:
            lmatrix2[key-1][el-1] = 1
    return lmatrix2


def warshella_for_1_turn(lmatrix, k, n, i):
    '''
    (list, int, int) -> list
    :param lmatrix: list of matrix
    :param k: iteration of  warshella's algoritm
    :param n: len matrix
    :return: modificated matrix
    '''
    for j in range(n):
        lmatrix[i][j] = 1 if lmatrix[i][j] or (lmatrix[i][k] and lmatrix[k][j]) else 0
    return lmatrix


def warshella(lmatrix):
    '''
    (list) -> None
    :param lmatrix:
    :return:
    '''
    nlen = len(lmatrix)
    lmats = []
    lmatrix1 = lmatrix
    for k in range(nlen):
        for i in range(nlen):
            lmatrix1 = warshella_for_1_turn(lmatrix1, k, nlen, i)
        lmats.append(copy.deepcopy(lmatrix1))
    return lmats


def start(inp, lg):
    '''
    input should look like:
    [(3,4)(4,5)]
    [(3,4),(4,5)]
    {(3,4),(5,6)}
    ((4,5)(5,6))
    :param inp: str
    :return: tuple/ str
    >>> start('(1,2)(2,4)(4,1)')
    ([[0, 1, 0], [0, 0, 1], [1, 0, 0]], [[[0, 1, 0], [0, 0, 1], [1, 1, 0]], [[0, 1, 1], [0, 0, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]])
    >>> start('{(5, 7), (4, 7), (0, 5), (0 , 7)}')
    ([[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]], [[[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]], [[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]], [[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]], [[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]])
    >>> start('(1,1)(1,4)(2, 1)(2,3)(3,1)(3,2)(3,4)( 4, 2)')
    ([[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 0, 0]], [[[1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 0, 0]], [[1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[1, 0, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]])
    >>> start('(2, 1)(2,3)(3,1)(3,2)(3,4)( 4, 2)(3,4)')
    ([[0, 0, 0, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 0, 0]], [[[0, 0, 0, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 0, 0]], [[0, 0, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1], [1, 1, 1, 0]], [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]])

    '''
    lsmatrix = read_file(inp, lg)
    if type(lsmatrix) != str:
        lsmatrix = print_matrix(lsmatrix)
        l = copy.deepcopy(lsmatrix)
        l = [l] + warshella(lsmatrix)
        return l, None
    elif lsmatrix[:12] == '  Your input' or lsmatrix[:11] == '  Ваш ввід ':
        return None, lsmatrix
    else:
        return None, ["  Please change your input. I am not ready for these. ",
                      "  Будь ласка змініть свій ввід. Я не готовий до такого. "][lg], lsmatrix
