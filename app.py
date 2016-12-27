from flask import Flask, render_template, request
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'static', 'python'))
import truth_table
import relations
import Warshalla

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


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
