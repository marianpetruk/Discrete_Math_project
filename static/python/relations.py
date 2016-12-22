def change_matrix(matrix_):
    width = 0
    for i in matrix_:
        if max(i) > width:
            width = max(i)
    lines = [[0 for i in range(width)] for i in range(width)]
    for i in matrix_:
        lines[i[0] - 1][i[1] - 1] = 1
    return lines


def reflexive_relation(lines):
    if not lines[0]:
        return False
    for i in range(len(lines)):
        if not lines[i][i]:
            return False
    return True


def symmetric_relation(lines):
    if not lines[0]:
        return True
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not j == i:
                if lines[j][i] != lines[i][j]:
                    return False
    return True


def asymmetric_relation(lines):
    if not lines[0]:
        return True
    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] and lines[j][i]:
                return False
    return True


def anti_symmetric_relation(lines):
    if not lines[0]:
        return True
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j and (lines[i][j] and lines[j][i]):
                return False
    return True


def transitive_relation(lines):
    from copy import deepcopy
    if not lines[0]:
        return True
    save = deepcopy(lines)
    for i in range(len(lines)):
        for j in range(len(lines)):
            for k in range(len(lines)):
                lines[j][k] = lines[j][k] or (lines[j][i] and lines[i][k])
    return save == lines


def return_text(question):
    if question:
        return 'yes'
    return 'no'


def main(matrix_):
    matrix_ = eval(matrix_)
    matrix_ = change_matrix(matrix_)
    text = 'relations of your matrix:\n' \
           'reflexive relation: {0}\n' \
           'symmetric relation: {1}\n' \
           'asymmetric relation: {2}\n' \
           'anti symmetric relation: {3}\n' \
           'transitive relation: {4}\n'.format(return_text(reflexive_relation(matrix_)),
                                             return_text(symmetric_relation(matrix_)),
                                             return_text(asymmetric_relation(matrix_)),
                                             return_text(anti_symmetric_relation(matrix_)),
                                             return_text(transitive_relation(matrix_)))
    return text.split('\n')
