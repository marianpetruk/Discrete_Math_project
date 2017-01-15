def reflexive_relation(mat):
    """
    :param mat: list(tuple(int,int))
    :return: bool

    >>> reflexive_relation([(1,1)])
    True

    >>> reflexive_relation([(2,3),(3,3),(2,2)])
    True

    >>> reflexive_relation([(2,3),(3,2),(2,2)])
    False
    """
    pool = []
    for i in mat:
        for j in i:
            if j not in pool:
                pool.append(j)
    for i in pool:
        if (i, i) not in mat:
            return False
    return True


def anti_reflexive_relation(mat):
    """
    :param mat: list(tuple(int,int))
    :return: bool

    >>> anti_reflexive_relation([(1,1)])
    False

    >>> anti_reflexive_relation([(2,3), (3,3), (2,2)])
    False

    >>> anti_reflexive_relation([(2,3), (3,2), (1,2)])
    True
    """

    for i in mat:
        if i[0] == i[1]:
            return False
    return True


def symmetric_relation(mat):
    """
    :param mat: list(tuple(int,int))
    :return: bool

    >>> symmetric_relation([(1,1)])
    True

    >>> symmetric_relation([(2,3), (4,3), (3,2), (3,4)])
    True

    >>> symmetric_relation([(2,3), (4,2), (2,4), (3,4)])
    False

    """
    pool = []
    for i in mat:
        pool.append((i[1], i[0]))
    for i in pool:
        if i not in mat:
            return False
    return True


def asymmetric_relation(mat):
    """
    :param mat: list(tuple(int,int))
    :return: bool

    >>> asymmetric_relation([(1,3)])
    True

    >>> asymmetric_relation([(2,3), (4,5), (5,5)])
    False

    >>> asymmetric_relation([(2,3), (3,4), (4,3)])
    False
    """
    pool = []
    for i in mat:
        pool.append((i[1], i[0]))
    for i in pool:
        if i in mat:
            return False
    return True


def anti_symmetric_relation(mat):
    """
    :param mat: list(tuple(int,int))
    :return: bool


    >>> anti_symmetric_relation([(1,1)])
    True

    >>> anti_symmetric_relation([(2,3), (4,5), (5,5)])
    True

    >>> anti_symmetric_relation([(2,3), (3,4), (4,3)])
    False
    """
    pool = []
    for i in mat:
        if i[0] != i[1]:
            pool.append((i[1], i[0]))
    for i in pool:
        if i in mat:
            return False
    return True


def transitive_relation(mat):
    """
    :param mat: list(tuple(int,int))
    :return: bool

    >>> transitive_relation([(2,3), (3,4), (2,4)])
    True

    >>> transitive_relation([(3,3)])
    True

    >>> transitive_relation([(3,4), (4,3), (3,3)])
    False
    """
    pool = []
    for i in mat:
        for j in mat:
            if i[1] == j[0]:
                pool.append((i[0], j[1]))
    for i in pool:
        if i not in mat:
            return False
    return True


def anti_transitive_relation(mat):
    """
    :param mat: list(tuple(int,int))
    :return: bool

    >>> anti_transitive_relation([(1,3)])
    True

    >>> anti_transitive_relation([(1,3), (3,1), (1,1)])
    False

    >>> anti_transitive_relation([(2,2)])
    False
    """
    pool = []
    for i in mat:
        for j in mat:
            if i[1] == j[0]:
                pool.append((i[0], j[1]))
    for i in pool:
        if i in mat:
            return False
    return True


def fails(mat):
    """
    :param mat: str
    :return: int or False
    False if matrix is correct
    str with error code, if matrix is wrong
    error codes:
    1 - something wrong with brackets
    2 - there is no comma between some numbers
    3 - missed number
    4 - unknown error
    """
    mat = str(mat)
    mat = mat.strip()
    if mat[:2] == '((' and mat[-2:] == '))':
        mat = mat[1:-1]
    counter = 0
    b_opened = 0
    b_closed = 0
    for i in mat:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
        if counter < 0 or counter > 1:
            return 1
    if counter != 0:
        return 1
    for i in range(len(mat)):
        if mat[i] == '(':
            b_opened = i
        if mat[i] == ')':
            b_closed = i
        if b_closed:
            if ',' not in mat[b_opened + 1:b_closed]:
                return 2
            else:
                c = mat[b_opened:b_closed + 1].index(',') + b_opened
                if b_opened + 1 == c or b_closed - 1 == c:
                    return 3
                else:
                    b_opened = 0
                    b_closed = 0

    try:
        eval(mat)
    except SyntaxError:
        return 4
    return False


def main(mat, lg):
    """
    :param mat: string
    :param lg: 0 (english) or 1 (ukrainian)
    :return: None, list(string) or string, None
    """
    try:
        errorslist = [["Your number(s) is(are) too big, numbers less than 51"
                       " are only required",
                       "Something wrong with brackets, please try again",
                       "Somewhere comma between numbers is missed,"
                       " please try again",
                       "Number is missed somewhere, please try again",
                       "Something wrong, please try again ",
                       "Each tuple can not contain more than 2 numbers",
                       "Matrix can not contain zero"],
                      ["Числа у Вашій матриці завеликі, максимально"
                       " дозволене число: 50",
                       "Щось пішло не так з дужками, спробуйте ще раз",
                       "Пропущена кома між числами, спробуйте ще раз",
                       "Десь пропущене число, спробуйте ще раз",
                       "Щось пішло не так, спробуйте ще раз",
                       "Кортежі не можуть містити більше двох чисел,"
                       " спробуйте ще раз",
                       "Матриця не може містити нуль спробуйте ще раз"]
                      ]

        mat = mat.strip()
        mat = mat.replace(')(', '),(')
        if mat[:2] == '((' and mat[-2:] == '))':
            mat = mat[1:-1]

        error = fails(mat)
        if error:
            return None, errorslist[lg][error]
        mat = '[' + mat + ']'
        mat = eval(mat)
        for i in mat:
            if i[0] > 50 or i[1] > 50:
                return None, errorslist[lg][0]
            if len(i) > 2:
                return None, errorslist[lg][5]
            if i[0] == 0 or i[1] == 0:
                return None, errorslist[lg][6]

        answers = [['No', 'Yes'], ['Ні', 'Так']]
        reflexive = answers[lg][int(reflexive_relation(mat))]
        anti_reflexive = answers[lg][int(anti_reflexive_relation(mat))]
        symmetric = answers[lg][int(symmetric_relation(mat))]
        asymmetric = answers[lg][int(asymmetric_relation(mat))]
        anti_symmetric = answers[lg][int(anti_symmetric_relation(mat))]
        transitive = answers[lg][int(transitive_relation(mat))]
        anti_transitive = answers[lg][int(anti_transitive_relation(mat))]

        text = ['Reflexive relation: {0}\n'
                'Anti reflexive relation: {1}\n'
                'Symmetric relation: {2}\n'
                'Asymmetric relation: {3}\n'
                'Antisymmetric relation: {4}\n'
                'Transitive relation: {5}\n'
                'Anti transitive relation: {6}'.format(reflexive,
                                                       anti_reflexive,
                                                       symmetric,
                                                       asymmetric,
                                                       anti_symmetric,
                                                       transitive,
                                                       anti_transitive),
                'Рефлексивне відношення: {0}\n'
                'Антирефлексивне відношення: {1}\n'
                'Симетричне відношення: {2}\n'
                'Асиметричне відношення: {3}\n'
                'Антисиметричне відношення: {4}\n'
                'Транзитивне відношення: {5}\n'
                'Антитранзитивне відношення: {6}'.format(reflexive,
                                                         anti_reflexive,
                                                         symmetric,
                                                         asymmetric,
                                                         anti_symmetric,
                                                         transitive,
                                                         anti_transitive)
                ]
    except:
        return None, ['Something wrong, please try again',
                      'Щось не так, спробуйте ще раз'][lg]

    return text[lg].split('\n'), None
