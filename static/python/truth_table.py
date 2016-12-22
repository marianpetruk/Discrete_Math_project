import sys


def gen_vals(s, order):
    vals = []
    symbs = ["(", ")", "^", "!", "V", ">", "~", "%", "T", "F"]
    for wrd in s:
        if wrd not in symbs:
            if wrd not in order:
                order.append(wrd)
                vals.append(wrd)
    dict = {}
    for i in range(len(vals)):
        dict[vals[i]] = []
        for col_fors in range(int((2 ** len(vals)) / (2 ** (len(vals) - i - 1)))):
            for j in range(int(2 ** (len(vals) - i - 1))):
                if col_fors % 2 == 0:
                    dict[vals[i]].append("T")
                else:
                    dict[vals[i]].append("F")
    return dict


def render_table(exps, order, vals):
    table = []
    exps_len = 0
    for el in exps.keys():
        exps_len = len(el)
    table.append([])
    for elem in order:
        table[0].append(elem)
    for i in range(int(2 ** len(vals))):
        count = 0
        table.append([])
        for elem in order:
            count += 1
            if elem in vals.keys():
                if count == len(vals):
                    table[i + 1].append(vals[elem][i])
                else:
                    table[i + 1].append(vals[elem][i])
            else:
                if count == len(vals):
                    table[i + 1].append(exps[elem][i])
                else:
                    table[i + 1].append(exps[elem][i])
    return table


def get_min_exp(s):
    if "(" in s:
        ind_s = -1
        ind_e = -1
        for i, word in enumerate(s):
            if word == "(":
                ind_s = i
        for i in range(ind_s + 1, len(s)):
            if s[i] == ")":
                ind_e = i
                break
        return s[ind_s + 1:ind_e]
    else:
        return s


def repl_vars(s, level, vals):
    repl = ""
    symbs = ["^", "!", "V", ">", "~", "%", "T", "F"]
    for ch in s:
        if ch not in symbs:
            repl += vals[ch][level]
        else:
            repl += ch
    return repl


def reverse(s):
    if s == "T":
        return "F"
    else:
        return "T"


def prepare(s, level, vals):
    repl = repl_vars(s, level, vals)
    what_ch = []
    for ind, ch in enumerate(repl):
        if ch == "!":
            what_ch.append(ind + 1)

    tm = ""
    for ind, ch in enumerate(repl):
        if ind in what_ch:
            tm += reverse(ch)
        else:
            tm += ch
    repl = tm
    repl = repl.replace("!", "")
    return repl


def op_and(fir, sec):
    if fir == "T" and sec == "T":
        return "T"
    else:
        return "F"


def op_or(fir, sec):
    if fir == "F" and sec == "F":
        return "F"
    else:
        return "T"


def op_imp(fir, sec):
    if fir == "T" and sec == "F":
        return "F"
    else:
        return "T"


def op_eqal(fir, sec):
    if fir == sec:
        return "T"
    else:
        return "F"


def op_xor(fir, sec):
    if fir == sec:
        return "F"
    else:
        return "T"


def repl_op(expr, full):
    res = ""
    if expr[1] == "^":
        res = op_and(expr[0], expr[2])
    if expr[1] == "V":
        res = op_or(expr[0], expr[2])
    if expr[1] == ">":
        res = op_imp(expr[0], expr[2])
    if expr[1] == "%":
        res = op_xor(expr[0], expr[2])
    if expr[1] == "~":
        res = op_eqal(expr[0], expr[2])
    return full.replace(expr, res)


def find_op(s):
    symbs = ["^", "!", "V", ">", "~", "%"]
    restart = True
    while restart:
        restart = False
        for ind, ch in enumerate(s):
            if ch in symbs:
                s = repl_op(s[ind - 1:ind + 2], s)
                restart = True
                break
    return s


def do_command(s):
    if s == "exit":
        sys.exit(0)
    if s == "help":
        print("Logical expressions solver.")
        print("You can use: ^(and), V(or), %(xor), ~(equal),")
        print("!(-)(not), ->(>)(implication), ()(brackets), T(True), F(False).")
        print("Use small letters, like: !p, o^r, (a^b)Vc, !!x, etc..")
        print("Commands: exit, help, about, print.")
        print("Enjoy program :)")
    if s == "about":
        print("Created by Roman Vey - 2016.")
    if s == "print":
        render_table()


def start(exp):
    vals = {}
    exps = {}
    order = []
    exp = exp.replace(" ", "")
    saved = exp
    exps[saved] = []
    exp = exp.replace("-", "!")
    exp = exp.replace("!>", ">")
    vals = gen_vals(exp, order)
    if saved not in order:
        order.append(saved)

    saved_prep = exp
    for curr in range(int(2 ** len(vals))):
        exp = saved_prep
        while True:
            min_exp = get_min_exp(exp)
            if min_exp == exp:
                tmp = min_exp
                tmp = tmp.replace("!!", "")
                tmp = prepare(tmp, curr, vals)
                tmp = find_op(tmp)
                exps[saved].append(tmp)
                break
            tmp = min_exp
            tmp = tmp.replace("!!", "")
            tmp = prepare(tmp, curr, vals)
            tmp = find_op(tmp)
            exp = exp.replace("(" + min_exp + ")", tmp)
    return render_table(exps, order, vals)
