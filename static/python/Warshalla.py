import copy
from string import ascii_letters


def read_file(smatrix):
    '''
    (str) -> dict
    '''
    dmatrix = {}
    bCheckIsFirstEl = False
    bCheckIsSecondEl = False
    stringF = ''
    stringS = ''
    # bCheckIsFirstEl = True
    inuml = 0
    inumr = 0
    bstartmatrix = False
    for el in smatrix:
        if el == ' ':
            pass
        elif el in ascii_letters:
            return "Your input is incorrect. Please don\'t use letters and try again."
        elif el == '(':
            bCheckIsFirstEl = True
            # if write {(2,4),(5,6)}
            bCheckIsSecondEl = False
            inuml += 1
            bstartmatrix = True
        elif not bstartmatrix:
            pass
        elif bCheckIsFirstEl and el != ',' and el != ')':
            stringF += el
        elif el == ',':
            if bCheckIsFirstEl or not bCheckIsSecondEl or inuml - inumr <= 1:
                bCheckIsFirstEl = False
                bCheckIsSecondEl = True
            else:
                return "Your input is incorrect. You may miss ',' between numbers. Please try again."
        elif bCheckIsSecondEl and el != ')' :
            if inuml > 0:
                stringS += el
        elif el == ')':
            inumr += 1

            if inuml >= inumr:
                if stringF != '' and stringS != '':
                    if int(stringF) in dmatrix:
                        if int(stringS) not in dmatrix[int(stringF)]:
                            dmatrix[int(stringF)].append(int(stringS))

                    else:
                        dmatrix[int(stringF)] = [int(stringS), ]
                    # print(dmatrix)
                    stringF = ''
                    stringS = ''
                else:
                    return "Your input is incorrect. You may miss number or some of them. Please try again."
            else:
                return "Your input is incorrect. Please check '(' and ')'."
        else:
            return "Your input is incorrect. Please try again."
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
        # print(key)
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
    '''
        n = len(lmat)
        lmatrix2 = []
        for i in range(n):
            lmatrix2.append([0] * n)
        for key in dpmmat:
            for el in dpmmat[key]:
                # print(lmatrix2)
                lmatrix2[lmat.index(key)][lmat.index(el)] = 1
        # print(lmatrix2)
        '''
    n = pmmax
    lmatrix2 = []
    for i in range(n):
        lmatrix2.append([0] * n)
    for key in dpmmat:
        for el in dpmmat[key]:
            # print(lmatrix2)
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
        lmatrix[i][j] = 1 if lmatrix[i][j] or (lmatrix[i][k] and lmatrix[k][j])  else 0
    # print(lmatrix, 'n =', n, ' i = ', i)
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
        # print(lmats)
        # print_matrix_col( lmatrix)
    return lmats


def start(inp):
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
    lsmatrix = read_file(inp)
    if type(lsmatrix) != str:
        lsmatrix = print_matrix(lsmatrix)
        # print(lsmatrix)
        # print_matrix_col(lsmatrix)
        l = copy.deepcopy(lsmatrix)
        l = [l] + warshella(lsmatrix)
        return l
    elif lsmatrix[:10] != 'Your input':
        return lsmatrix


# print(print_matrix(read_file('{(5, 7), (4, 7), (0, 5), (0 , 7)}')))
# [[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
# print(warshalla(print_matrix(read_file('{(5, 7), (4, 7), (0, 5), (5,4)}'))))

print(start('6(2,3)(3,2)(3,4)( 4, 2)(3,4)'))
