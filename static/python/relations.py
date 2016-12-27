def change_matrix(matrix_):
    """
    list(tuple(int, int)) -> list(list(int {1 or 0}))
    change type of matrix

    >>> change_matrix([(1,1),(2,3),(1,2)])
    [[1, 1, 0], [0, 0, 1], [0, 0, 0]]

    ! ! ! ATTENTION ! ! !  all modules work only with matriсes like
    [[1, 1, 0], [0, 0, 1], [0, 0, 0]]
    """
    width = 0
    for i in matrix_:
        if max(i) > width:
            width = max(i)
    lines = [[0 for i in range(width)] for i in range(width)]
    for i in matrix_:
        lines[i[0] - 1][i[1] - 1] = 1
    return lines


def reflexive_relation(lines):
    """
    list(list(int {1 or 0})) -> bool
    """

    if not lines[0]:
        return False
    lst = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]:
                lst.append(j)
                lst.append(i)
    for i in lst:
        if not lines[i][i]:
            return False
    return True


def symmetric_relation(lines):
    """
    list(list(int {1 or 0})) -> bool
    """
    if not lines[0]:
        return True
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not j == i:
                if lines[j][i] != lines[i][j]:
                    return False
    return True


def asymmetric_relation(lines):
    """
    list(list(int {1 or 0})) -> bool
    """
    if not lines[0]:
        return True
    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] and lines[j][i]:
                return False
    return True


def anti_symmetric_relation(lines):
    """
    list(list(int {1 or 0})) -> bool
    """
    if not lines[0]:
        return True
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j and (lines[i][j] and lines[j][i]):
                return False
    return True


def transitive_relation(lines):
    """
    list(list(int {1 or 0})) -> bool
    contains warshall algorithm
    """
    from copy import deepcopy
    if not lines[0]:
        return True
    save = deepcopy(lines)
    for i in range(len(lines)):
        for j in range(len(lines)):
            for k in range(len(lines)):
                lines[j][k] = lines[j][k] or (lines[j][i] and lines[i][k])
    return save == lines


def return_text(question, lg):
    """
    function(matrix_) -> str {'yes' or 'no'}
    no need to import this module, it's only helpful part for main() module
    """
    if question:
        return ['Yes', "Так"][lg]
    return ['No', "Ні"][lg]


def main(matrix_, lg):
    """
    string - > list(string)
    if you have to work with matrix like (1,1),(2,3),(1,2), necessarily use module change_matrix() before using this

    >>> main('[[1, 1, 0], [0, 0, 1], [0, 0, 0]]')
    ['relations of your matrix:', 'reflexive relation: no', 'symmetric relation: no', 'asymmetric relation: no',
    ... 'anti symmetric relation: yes', 'transitive relation: no', '']

    >>> main('(1,1),(2,3),(1,2)')
    ['relations of your matrix:', 'reflexive relation: no', 'symmetric relation: no', 'asymmetric relation: no',
    ... 'anti symmetric relation: yes', 'transitive relation: no', '']

    """
    try:
        matrix_ = matrix_.strip()
        if matrix_[0] == '(':
            b = 0
            a = 0
            open_num = 0
            close_num = 0
            for i in matrix_:
                if i == '(':
                    open_num += 1
                elif i == ')':
                    close_num += 1
            if not close_num or not open_num or open_num != close_num:
                return None, ['  Something wrong with brackets, please try again',
                              "  Щось пішло не так з дужками, спробуйте ще раз"][lg]
            for i in range(len(matrix_)):
                if matrix_[i] == '(':
                    a = i
                if matrix_[i] == ')':
                    b = i
                if b:
                    if ',' not in matrix_[a + 1:b]:
                        return None, ['  There is no comma between some numbers, please try again',
                                      '  Немає коми між числами, спробуйте ще раз'][lg]
                    else:
                        a = 0
                        b = 0

            matrix_ = matrix_.replace(')(', '),(')
            matrix_ = matrix_.replace(' ', '')
            matrix_ = '[' + matrix_ + ']'
            matrix_ = eval(matrix_)
            matrix_ = change_matrix(matrix_)
        else:
            matrix_ = eval(matrix_)
        if lg == 0:
            text = 'Reflexive relation: {0}\n' \
                   'Symmetric relation: {1}\n' \
                   'Asymmetric relation: {2}\n' \
                   'Antisymmetric relation: {3}\n' \
                   'Transitive relation: {4}'.format(return_text(reflexive_relation(matrix_), lg),
                                                     return_text(symmetric_relation(matrix_), lg),
                                                     return_text(asymmetric_relation(matrix_), lg),
                                                     return_text(anti_symmetric_relation(matrix_), lg),
                                                     return_text(transitive_relation(matrix_), lg))
        else:
            text = 'Рефлексивне відношення: {0}\n' \
                   'Симетричне відношення: {1}\n' \
                   'Асиметричне відношення: {2}\n' \
                   'Антисиметричне відношення: {3}\n' \
                   'Транзитивне відношення: {4}'.format(return_text(reflexive_relation(matrix_), lg),
                                                     return_text(symmetric_relation(matrix_), lg),
                                                     return_text(asymmetric_relation(matrix_), lg),
                                                     return_text(anti_symmetric_relation(matrix_), lg),
                                                     return_text(transitive_relation(matrix_), lg))

    except:
        return None, ["  Something wrong, please try again", '  Щось не так, спробуйте ще раз'][lg]
    return text.split('\n'), None
