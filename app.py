from flask import Flask, render_template, request
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'static', 'python'))
import truth_table
import relations
import Warshalla
import Combinatorics
import multimatrix

app = Flask(__name__)


@app.route('/')
def home():
    lg = request.args.get('lg')
    add = "_uk" if lg == "uk" else ""
    where = 'home'
    path = 'pages/placeholder.' + where + add + '.html'
    return render_template(path, lg=lg)


@app.route('/about')
def about():
    lg = request.args.get('lg')
    add = "_uk" if lg == "uk" else ""
    where = 'about'
    path = 'pages/placeholder.' + where + add + '.html'
    return render_template(path, lg=lg)


@app.route('/truth_table', methods=['GET', 'POST'])
def truth():
    if request.method == 'GET':
        lg = request.args.get('lg')
        add = "_uk" if lg == "uk" else ""
        where = 'truth_table'
        path = 'pages/placeholder.' + where + add + '.html'
        return render_template(path, result=None, errors=None, query="", lg=lg if lg else "en")
    data = request.form.get('formula')
    lg = request.form.get('lg')
    add = "_uk" if lg == "uk" else ""
    lg_val = 1 if lg == "uk" else 0
    where = 'truth_table'
    path = 'pages/placeholder.' + where + add + '.html'
    if data == "" or data is None:
        return render_template(path, result=None, errors=["  Expression can`t be empty", "  Вираз не може бути пустим"][lg_val], query="", lg=lg if lg else "en")
    else:
        try:
            res, e = truth_table.start(data, lg_val)
        except:
            res, e = None, ["  Incorrect input", '  Некоректний ввід'][lg_val]
        return render_template(path, result=res, errors=e, query=data, lg=lg if lg else "en")


@app.route('/warshall', methods=['GET', 'POST'])
def warshall():
    if request.method == 'GET':
        lg = request.args.get('lg')
        add = "_uk" if lg == "uk" else ""
        where = 'warshall'
        path = 'pages/placeholder.' + where + add + '.html'
        return render_template(path, result=None, errors=None, query="", lg=lg if lg else "en")
    data = request.form.get('warshalla')
    lg = request.form.get('lg')
    add = "_uk" if lg == "uk" else ""
    lg_val = 1 if lg == "uk" else 0
    where = 'warshall'
    path = 'pages/placeholder.' + where + add + '.html'
    if data == "" or data is None:
        return render_template(path, result=None, query="", errors=["  Expression can`t be empty",
                                                                    "  Вираз не може бути пустим"][lg_val], lg=lg if lg else "en")
    else:
        try:
            res, e = Warshalla.start(data, lg_val)
        except:
            res, e = None, ["  Incorrect input", '  Некоректний ввід'][lg_val]
        return render_template(path, result=res, query=data, errors=e, lg=lg if lg else "en")


@app.route('/relations', methods=['GET', 'POST'])
def check_relation():
    if request.method == 'GET':
        lg = request.args.get('lg')
        add = "_uk" if lg == "uk" else ""
        where = 'relations'
        path = 'pages/placeholder.' + where + add + '.html'
        return render_template(path, result=None, query="", errors=None, lg=lg if lg else "en")
    data = request.form.get('relation')
    lg = request.form.get('lg')
    add = "_uk" if lg == "uk" else ""
    lg_val = 1 if lg == "uk" else 0
    where = 'relations'
    path = 'pages/placeholder.' + where + add + '.html'
    if data == "" or data is None:
        return render_template(path, result=None, query="", errors=["  Expression can`t be empty",
                                                                    "  Вираз не може бути пустим"][lg_val], lg=lg if lg else "en")
    else:
        res, e = relations.main(data, lg_val)
        return render_template(path, result=res, query=data, errors=e, lg=lg if lg else "en")


@app.route('/multiplication', methods=['GET', 'POST'])
def multiplication():
    if request.method == 'GET':
        lg = request.args.get('lg')
        add = "_uk" if lg == "uk" else ""
        where = 'multiplication'
        path = 'pages/placeholder.' + where + add + '.html'
        return render_template(path, result=None, query1="", query2="", errors=None, lg=lg if lg else "en")

    data1 = request.form.get('matrix1')
    data2 = request.form.get('matrix2')
    lg = request.form.get('lg')
    add = "_uk" if lg == "uk" else ""
    lg_val = 1 if lg == "uk" else 0
    where = 'multiplication'
    path = 'pages/placeholder.' + where + add + '.html'
    if (data1 == "" or data1 is None) or (data2 == "" or data2 is None):
        return render_template(path, result=None, query1="", query2="", errors=["  Expression can`t be empty",
                                                                                "  Вираз не може бути пустим"][lg_val], lg=lg if lg else "en")
    else:
        res, e = multimatrix.main(data1, data2, lg_val)
        return render_template(path, result=res, query1=data1, query2=data2, errors=e, lg=lg if lg else "en")


@app.route('/combinatorics', methods=['GET', 'POST'])
def combinatorics():
    if request.method == 'GET':
        lg = request.args.get('lg')
        add = "_uk" if lg == "uk" else ""
        where = 'combinatorics'
        path = 'pages/placeholder.' + where + add + '.html'
        return render_template(path, result=None, query="", errors=None, lg=lg if lg else "en")
    data_m = request.form.get('M_value')
    data_n = request.form.get('N_value')
    data_repeat = request.form.get('repeat')
    data_order = request.form.get('order')
    lg = request.form.get('lg')
    add = "_uk" if lg == "uk" else ""
    lg_val = 1 if lg == "uk" else 0
    where = 'combinatorics'
    path = 'pages/placeholder.' + where + add + '.html'
    if data_m == "" or data_m is None or data_n == "" or data_n is None:
        return render_template(path, result=None, query="", errors=["  Expression can`t be empty",
                                                                    "  Вираз не може бути пустим"][lg_val], lg=lg if lg else "en")
    else:
        answer, res, e = Combinatorics.main(data_m, data_n, data_order, data_repeat, lg_val)
        data = [res, data_m, data_n, data_order, data_repeat, answer]
        return render_template(path, result=data, errors=e, lg=lg if lg else "en")



@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
