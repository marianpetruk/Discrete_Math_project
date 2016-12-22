def read_file(smatrix):
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
                dmatrix[int(stringF)] = [int(stringS),]
            stringF = ''
            stringS = ''
    return dmatrix
    
def print_matrix_col(lpmcmat):
    for el in lpmcmat:
        print(el)
    print()
    
    
def print_matrix(dmat):
    dpmmat = {}
    lmat = []
    #print(dmat)
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
    #print(lmat)
    lmat = sorted(list(set(lmat)))
    #print(lmat)
    n = len(lmat)
    lmatrix = []
    for i in range(n):
        lmatrix.append([0]*n)
    for key in dpmmat:
        for el in dpmmat[key]:
            #print(lmatrix)
            lmatrix[lmat.index(key)][lmat.index(el)] = 1
    return lmatrix


def worshalla_for_1_turn(lmatrix, k, n):
    for i in range(n):
        for j in range(n):
            lmatrix[i][j] = 1 if lmatrix[i][j] or (lmatrix[i][k] and lmatrix[k][j])  else 0
    return lmatrix
    
def worshalla(lmatrix):
    nlen = len(lmatrix)
    for k in range(nlen):
        lmatrix = worshalla_for_1_turn(lmatrix, k, nlen)
        print_matrix_col( lmatrix)
        
def start():
    inp = input('Please write matrix as {(5, 7), (4, 7), (0, 5), (0 , 7)} or {(5, 7)(4, 7)(0, 5)(0,7)}:  ')
    lsmatrix = print_matrix(read_file(inp))
    print_matrix_col(lsmatrix)
    worshalla(lsmatrix)

#print(print_matrix(read_file('{(5, 7), (4, 7), (0, 5), (0 , 7)}')))
#[[0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
#print(worshalla(print_matrix(read_file('{(5, 7), (4, 7), (0, 5), (5,4)}'))))
start()
