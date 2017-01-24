def change_matrix(mat1, mat2):
    """
    :param mat1: list(tuple(int, int))
    :param mat2: list(tuple(int, int))
    :return: list(list(1 or 0)), list(list(1 or 0)), int
    """
    max_num = 0
    for i in mat1:
        if i[0] > max_num:
            max_num = i[0]
        if i[1] > max_num:
            max_num = i[1]
    for i in mat2:
        if i[0] > max_num:
            max_num = i[0]
        if i[1] > max_num:
            max_num = i[1]
            
    new_matrix1 = [[0]*max_num for i in range(max_num)]
    new_matrix2 = [[0]*max_num for i in range(max_num)]
    for i in range(max_num):
        for j in range(max_num):
            if (i + 1, j + 1) in mat1:
                new_matrix1[i][j] = 1
            else:
                new_matrix1[i][j] = 0
            if (i + 1, j + 1) in mat2:
                new_matrix2[i][j] = 1
            else:
                new_matrix2[i][j] = 0
    return new_matrix1, new_matrix2, max_num
    
    
def rechange_matrix(mat):
    """
    :param mat: list(list(1 or 0))
    :return: list(tuple(int, int))
    """
    l = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1:
                l.append((i + 1, j + 1))
    return l


def break_matrix_a(mat):
    """
    :param mat:  list(list(1 or 0))
    :return: list(string)
    """
    l = []
    for i in mat:
        s = ''
        for j in i:
            s += str(j)
        l.append(s)
    return l


def break_matrix_b(mat):
    """
    :param mat: list(list(1 or 0))
    :return: list(string)
    """
    l = []
    max_num = len(mat)
    for i in range(max_num):
        s = ''
        for j in range(max_num):
            s += str(mat[j][i])
        l.append(s)
    return l


def compare_strings(s1, s2):
    """
    :param s1: string
    :param s2: string
    :return: bool
    """
    s1, s2 = list(s1), list(s2)
    for i in range(len(s1)):
        if s1[i] == '1' and s2[i] == '1':
            return True
    return False
    
    
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


def main(mat1, mat2, lg):
    """
    :param mat1: str(tuple(int,int))
    :param mat2: str(tuple(int,int))
    :param lg: 0 = english 1 = ukrainian
    """
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
                      
    mat1 = mat1.strip().replace(')(', '),(')
    mat2 = mat2.strip().replace(')(', '),(')    
    if mat1[:2] == '((' and mat1[-2:] == '))':
        mat1 = mat1[1:-1]
    if mat2[:2] == '((' and mat2[-2:] == '))':
        mat2 = mat2[1:-1]
    error1 = fails(mat1)
    error2 = fails(mat2)
    if error1:
        return None, errorslist[lg][error1]
    if error2:
        return None, errorslist[lg][error2]
    mat1 = eval('[' + mat1 + ']')
    mat2 = eval('[' + mat2 + ']')
    
    for i in mat1:
        if i[0] > 50 or i[1] > 50:
            return None, errorslist[lg][0]
        if len(i) > 2:
            return None, errorslist[lg][5]
        if i[0] == 0 or i[1] == 0:
            return None, errorslist[lg][6]
    
    for i in mat2:
        if i[0] > 50 or i[1] > 50:
            return None, errorslist[lg][0]
        if len(i) > 2:
            return None, errorslist[lg][5]
        if i[0] == 0 or i[1] == 0:
            return None, errorslist[lg][6]
            
    mat1, mat2, max_num = change_matrix(mat1, mat2)
    
    ######################
    # ACTION STARTS HERE #
    ######################
    
    new = []
    ch_mat1, ch_mat2 = break_matrix_a(mat1), break_matrix_b(mat2)
    for i in range(max_num):
        l = []
        for j in range(max_num):
            if compare_strings(ch_mat1[i], ch_mat2[j]):
                l.append(1)
            else:
                l.append(0)
        new.append(l)
    return new, None
