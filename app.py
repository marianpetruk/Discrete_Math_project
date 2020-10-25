from flask import Flask, render_template, request
import os
import sys
from copy import deepcopy as dc
sys.path.append(os.path.join(os.path.dirname(__file__), 'static', 'python'))
import truth_table
import relations
import Warshalla
import Combinatorics
import multimatrix
import Bell_Stirling_numbers
import fibonacci

app = Flask(__name__)


def compose_path(where, lang):
    return 'pages/placeholder.' + where + ("_"+lang)*bool(lang) + '.html'


@app.route('/')
def home():
    lg = request.args.get('lg')
    return render_template(compose_path('home', lg), lg=lg)


@app.route('/about')
def about():
    lg = request.args.get('lg')
    return render_template(compose_path('about', lg), lg=lg)


@app.route('/help')
def help():
    lg = request.args.get('lg')
    return render_template(compose_path('help', lg), lg=lg)


@app.route('/truth_table', methods=['GET', 'POST'])
def truth():
    lg = request.form.get('lg')
    path = compose_path('truth_table', lg)
    if request.method == 'GET':
        return render_template(path, result=None, errors=None, query="", lg=lg if lg else "en")
    data = request.form.get('formula')
    lg_val = 1 if lg == "uk" else 0
    if not data:
        return render_template(
            path,
            result=None,
            errors=["  Expression can`t be empty", "  Вираз не може бути порожнім"][lg_val],
            query="",
            lg=lg if lg else "en"
        )

    try:
        res, e = truth_table.start(data, lg_val)
    except:
        res, e = None, ["  Incorrect input", '  Некоректний ввід'][lg_val]
    return render_template(path, result=res, errors=e, query=data.replace(" ", ""), lg=lg if lg else "en")


@app.route('/warshall', methods=['GET', 'POST'])
def warshall():
    lg = request.form.get('lg')
    path = compose_path('warshall', lg)
    if request.method == 'GET':
        return render_template(path, result=None, errors=None, query="", lg=lg if lg else "en")
    data = request.form.get('warshalla')
    lg_val = 1 if lg == "uk" else 0
    if not data:
        return render_template(
            path,
            result=None,
            query="",
            errors=["  Expression can`t be empty", "  Вираз не може бути порожнім"][lg_val],
            lg=lg if lg else "en"
        )

    try:
        res, e = Warshalla.start(data, lg_val)
    except:
        res, e = None, ["  Incorrect input", '  Некоректний ввід'][lg_val]
    return render_template(path, result=res, query=data.replace(" ", ""), errors=e, lg=lg if lg else "en")


@app.route('/relations', methods=['GET', 'POST'])
def check_relation():
    lg = request.args.get('lg')
    path = compose_path('relations', lg)
    if request.method == 'GET':
        return render_template(path, result=None, query="", errors=None, lg=lg if lg else "en")
    data = request.form.get('relation')
    lg_val = 1 if lg == "uk" else 0
    if not data:
        return render_template(
            path,
            result=None,
            query="",
            errors=["  Expression can`t be empty", "  Вираз не може бути порожнім"][lg_val],
            lg=lg if lg else "en"
        )

    res, e = relations.main(data, lg_val)
    return render_template(path, result=res, query=data.replace(" ", ""), errors=e, lg=lg if lg else "en")


@app.route('/fibonacci', methods=['GET', 'POST'])
def fibo():
    lg = request.args.get('lg')
    path = compose_path("fibonacci", lg)
    if request.method == 'GET':
        return render_template(path, result=None, query="", errors=None, lg=lg if lg else "en")
    data = request.form.get('fibo')
    lg_val = 1 if lg == "uk" else 0
    if not data:
        return render_template(
            path,
            result=None,
            query="",
            errors=["  Expression can`t be empty", "  Вираз не може бути порожнім"][lg_val],
            lg=lg if lg else "en"
        )

    res, e = fibonacci.fibo(data, lg_val)
    return render_template(path, result=res, query=data.replace(" ", ""), errors=e, lg=lg if lg else "en")


@app.route('/bell_stirling_numbers', methods=['GET', 'POST'])
def bs_numbers():
    lg = request.args.get('lg')
    path = compose_path("bell_stirling_numbers", lg)
    if request.method == 'GET':
        return render_template(path, result=None, query="", errors=None, lg=lg if lg else "en")
    data = request.form.get('bs_numbers')
    lg_val = 1 if lg == "uk" else 0
    if data == "" or data is None:
        return render_template(
            path,
            result=None,
            query="",
            errors=["  Expression can`t be empty", "  Вираз не може бути порожнім"][lg_val],
            lg=lg if lg else "en"
        )

    res, e = Bell_Stirling_numbers.main(data, lg_val)
    return render_template(path, result=res, query=data.replace(" ", ""), errors=e, lg=lg if lg else "en")


@app.route('/composition', methods=['GET', 'POST'])
def composition():
    lg = request.args.get('lg')
    path = compose_path("composition", lg)
    if request.method == 'GET':
        return render_template(path, result=None, query1="", query2="", errors=None, lg=lg if lg else "en")
    mat = request.form.get('matrix1')
    pwr = request.form.get('power')
    lg_val = 1 if lg == "uk" else 0
    if mat == "" or mat is None:
        return render_template(
            path,
            result=None,
            query1="",
            query2="",
            errors=["  Expression can`t be empty", "  Вираз не може бути порожнім"][lg_val],
            lg=lg if lg else "en"
        )

    test_er = multimatrix.main(mat, '(1, 1)', lg_val)[1]
    if test_er is not None:
        e = test_er
        return render_template(
            path,
            result=None,
            query1=mat.replace(" ", ""),
            query2=pwr,
            errors=e,
            lg=lg if lg else "en"
        )

    mat = mat.replace(')(', '),(')
    maxim = multimatrix.change_matrix(eval('[' + mat + ']'), [(1, 1)])[2]
    res = dc(mat)
    pwr = int(pwr)
    e = None
    for i in range(pwr - 1):
        if res == '' and e is None:
            return render_template(
                path,
                result=[[0]*maxim]*maxim,
                query1=mat.replace(" ", ""),
                query2=pwr,
                errors=None,
                lg=lg if lg else "en"
            )
        elif e is not None:
            return render_template(
                path,
                result=None,
                query1=mat.replace(" ", ""),
                query2=pwr,
                errors=e,
                lg=lg if lg else "en"
            )

        res, e = multimatrix.main(res, mat, lg_val)
        res = multimatrix.rechange_matrix(res)
        tres = ''
        for j in res:
            tres += str(j)
        res = dc(tres)
    res = res.replace(')(', '),(')
    res = eval('[' + res + ']')
    res = multimatrix.change_matrix(res, [(1, 1)])[0]
    res = multimatrix.add_to(res, maxim)
    return render_template(
        path,
        result=res,
        query1=mat.replace(" ", ""),
        query2=pwr,
        errors=e,
        lg=lg if lg else "en"
    )


@app.route('/multiplication', methods=['GET', 'POST'])
def multiplication():
    lg = request.args.get('lg')
    path = compose_path("multiplicaton", lg)
    if request.method == 'GET':
        return render_template(path, result=None, query1="", query2="", errors=None, lg=lg if lg else "en")

    data1 = request.form.get('matrix1')
    data2 = request.form.get('matrix2')
    lg_val = 1 if lg == "uk" else 0
    if not data1 or not data2:
        return render_template(
            path,
            result=None,
            query1="",
            query2="",
            errors=["  Expression can`t be empty", "  Вираз не може бути порожнім"][lg_val],
            lg=lg if lg else "en"
        )

    res, e = multimatrix.main(data1, data2, lg_val)
    return render_template(
        path,
        result=res,
        query1=data1.replace(" ", ""),
        query2=data2.replace(" ", ""),
        errors=e,
        lg=lg if lg else "en"
    )


@app.route('/combinatorics', methods=['GET', 'POST'])
def combinatorics():
    lg = request.args.get('lg')
    path = compose_path("combinatorics", lg)
    if request.method == 'GET':
        return render_template(
            path,
            result=None,
            query1="",
            query2="",
            query_repeat="yes",
            query_order="yes",
            errors=None,
            lg=lg if lg else "en"
        )
    data_m = request.form.get('M_value')
    data_n = request.form.get('N_value')
    data_repeat = request.form.get('repeat')
    data_order = request.form.get('order')
    lg_val = 1 if lg == "uk" else 0
    if not data_m or not data_n:
        return render_template(
            path,
            result=None,
            query1="",
            query2="",
            query_repeat="yes",
            query_order="yes",
            errors=["  Expression can`t be empty", "  Вираз не може бути порожнім"][lg_val],
            lg=lg if lg else "en"
        )

    answer, res, e = Combinatorics.main(data_m, data_n, data_order, data_repeat, lg_val)
    data = [res, data_m, data_n, data_order, data_repeat, answer]
    return render_template(
        path,
        result=data,
        errors=e,
        lg=lg if lg else "en",
        query1=data_m.replace(" ", ""),
        query2=data_n.replace(" ", ""),
        query_repeat=data_repeat,
        query_order=data_order
    )


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
