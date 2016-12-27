from flask import Flask, render_template, request
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'static', 'python'))
import truth_table, relations, Warshalla


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/truth_table', methods=['GET', 'POST'])
def truth():
    if request.method == 'GET':
        return render_template('pages/placeholder.truth_table.html', result=None, errors=None, query="")
    data = request.form.get('formula')
    if data == "" or data == None:
        return render_template('pages/placeholder.truth_table.html', result=None, errors="Expression can`t be empty", query="")
    else:
        try:
            res, e = truth_table.start(data)
        except:
            res, e = None, "Incorrect input"
        return render_template('pages/placeholder.truth_table.html', result=res, errors=e, query=data)


@app.route('/warshall', methods=['GET', 'POST'])
def warshall():
    if request.method == 'GET':
        return render_template('pages/placeholder.warshall.html', result=None, query="")
    data = request.form.get('warshalla')
    if data == "" or data == None:
        return render_template('pages/placeholder.warshall.html', result=None, query="")
    else:
        return render_template('pages/placeholder.warshall.html', result=Warshalla.start(data), query=data)


@app.route('/relations', methods=['GET', 'POST'])
def check_relation():
    if request.method == 'GET':
        return render_template('pages/placeholder.relations.html', result=None, query="")
    data = request.form.get('relation')
    if data == "" or data == None:
        return render_template('pages/placeholder.relations.html', result=None, query="")
    else:
        return render_template('pages/placeholder.relations.html', result=relations.main(data), query=data)


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
