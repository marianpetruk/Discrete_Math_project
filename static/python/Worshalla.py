import copy


def read_file(smatrix):
    '''
    (str) -> dict
    '''
    dmatrix = {}
    bCheckIsFirstEl = False
    bCheckIsSecondEl = False
    stringF = ''
    stringS = ''
    for el in smatrix:
        if el == ' ':
            pass
        elif el == '(':
            bCheckIsFirstEl = True
            # if write {(2,4),(5,6)}
            bCheckIsSecondEl = False
        elif bCheckIsFirstEl and el != ',' and el != ')':
            stringF += el
        elif el == ',':
            bCheckIsFirstEl = False
            bCheckIsSecondEl = True
        elif bCheckIsSecondEl and el != ')':
            stringS += el
        elif el == ')':
            if int(stringF) in dmatrix and int(stringS) not in dmatrix[int(stringF)]:
                dmatrix[int(stringF)].append(int(stringS))
            else:
                dmatrix[int(stringF)] = [int(stringS), ]
            stringF = ''
            stringS = ''
    return dmatrix


'''
def print_matrix_col(lpmcmat):
    #'''
# (list) -> None
'''
    for el in lpmcmat:
        print(el)
    print()
'''


def print_matrix(dmat):
    '''
    (dict) -> list
    '''
    dpmmat = {}
    lmat = []
    # print(dmat)
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
    # print(lmat)
    lmat = sorted(list(set(lmat)))
    # print(lmat)
    n = len(lmat)
    lmatrix2 = []
    for i in range(n):
        lmatrix2.append([0] * n)
    for key in dpmmat:
        for el in dpmmat[key]:
            # print(lmatrix)
            lmatrix2[lmat.index(key)][lmat.index(el)] = 1
    return lmatrix2


def worshalla_for_1_turn(lmatrix, k, n, i):
    '''
    (list, int, int) -> list
    :param lmatrix: list of matrix
    :param k: iteration of  worshalla's algoritm
    :param n: len matrix
    :return: modificated matrix
    '''
    for j in range(n):
        lmatrix[i][j] = 1 if lmatrix[i][j] or (lmatrix[i][k] and lmatrix[k][j])  else 0
    # print(lmatrix, 'n =', n, ' i = ', i)
    return lmatrix


def worshalla(lmatrix):
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
            lmatrix1 = worshalla_for_1_turn(lmatrix1, k, nlen, i)
        lmats.append(copy.deepcopy(lmatrix1))
        # print(lmats)
        # print_matrix_col( lmatrix)
    return lmats


def start():
    inp = input('Please write matrix as {(5, 7), (4, 7), (0, 5), (0 , 7)} or {(5, 7)(4, 7)(0, 5)(0,7)}:  ')
    lsmatrix = print_matrix(read_file(inp))
    # print(lsmatrix)
    # print_matrix_col(lsmatrix)
    l = copy.deepcopy(lsmatrix)
    return l, worshalla(lsmatrix)


# print(print_matrix(read_file('{(5, 7), (4, 7), (0, 5), (0 , 7)}')))
# [[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
# print(worshalla(print_matrix(read_file('{(5, 7), (4, 7), (0, 5), (5,4)}'))))
# (1,2)(2,4)(4,1)
# ([[0, 1, 0], [0, 0, 1], [1, 0, 0]], [[[0, 1, 0], [0, 0, 1], [1, 1, 0]], [[0, 1, 1], [0, 0, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]])
print(start())
