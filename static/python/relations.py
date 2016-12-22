def change_matrix(matrix_):
    '''
    list(tuple(int, int)) -> list(list(int {1 or 0}))
    change type of matrix
    
    >>> change_matrix([(1,1),(2,3),(1,2)])
    [[1, 1, 0], [0, 0, 1], [0, 0, 0]]
    
    ! ! ! ATTENTION ! ! !  all modules work only with matriсes like 
    [[1, 1, 0], [0, 0, 1], [0, 0, 0]]
    '''
    width = 0
    for i in matrix_:
        if max(i) > width:
            width = max(i)
    lines = [[0 for i in range(width)] for i in range(width)]
    for i in matrix_:
        lines[i[0] - 1][i[1] - 1] = 1
    return lines


def reflexive_relation(lines):
    '''
    list(list(int {1 or 0})) -> bool
    '''
    if not lines[0]:
        return False
    for i in range(len(lines)):
        if not lines[i][i]:
            return False
    return True


def symmetric_relation(lines):
    '''
    list(list(int {1 or 0})) -> bool
    '''
    if not lines[0]:
        return True
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not j == i:
                if lines[j][i] != lines[i][j]:
                    return False
    return True


def asymmetric_relation(lines):
    '''
    list(list(int {1 or 0})) -> bool
    '''
    if not lines[0]:
        return True
    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] and lines[j][i]:
                return False
    return True


def anti_symmetric_relation(lines):
    '''
    list(list(int {1 or 0})) -> bool
    '''
    if not lines[0]:
        return True
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j and (lines[i][j] and lines[j][i]):
                return False
    return True


def transitive_relation(lines):
    '''
    list(list(int {1 or 0})) -> bool
    contains warshall algorithm
    '''
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
    '''
    function(matrix_) -> str {'yes' or 'no'}
    no need to import this module, it's only helpful part for main() module
    '''
    if question:
        return 'yes'
    return 'no'


def main(matrix_):
    '''
    string - > list(string)
    if you have to work with matrix like (1,1),(2,3),(1,2), necessarily use module change_matrix() before using this
    
    >>> main('[[1, 1, 0], [0, 0, 1], [0, 0, 0]]')
    ['relations of your matrix:', 'reflexive relation: no', 'symmetric relation: no', 'asymmetric relation: no',
    ... 'anti symmetric relation: yes', 'transitive relation: no', '']
    
    >>> main('(1,1),(2,3),(1,2)')
    ['relations of your matrix:', 'reflexive relation: no', 'symmetric relation: no', 'asymmetric relation: no', 
    ... 'anti symmetric relation: yes', 'transitive relation: no', '']
    
    '''
    if matrix_[0] == '(':
        matrix_ = '[' + matrix_ + ']'
        matrix_ = eval(matrix_)
        matrix_ = change_matrix(matrix_)
    else:
        matrix_ = eval(matrix_)
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
