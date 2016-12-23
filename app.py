from flask import Flask, render_template, request
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'static', 'python'))
import truth_table, relations, Worshalla


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
        return render_template('pages/placeholder.truth_table.html', result=None)
    data = request.form.get('formula')
    if data == "" or data == None:
        return render_template('pages/placeholder.truth_table.html', result=None)
    else:
        return render_template('pages/placeholder.truth_table.html', result=truth_table.start(data))


@app.route('/worshell', methods=['GET', 'POST'])
def worshell():
    if request.method == 'GET':
        return render_template('pages/placeholder.worshell.html', result=None)
    data = request.form.get('worshalla')
    if data == "" or data == None:
        return render_template('pages/placeholder.worshell.html', result=None)
    else:
        return render_template('pages/placeholder.worshell.html', result=Worshalla.start(data))


@app.route('/relations', methods=['GET', 'POST'])
def check_relation():
    if request.method == 'GET':
        return render_template('pages/placeholder.relations.html', result=None)
    data = request.form.get('relation')
    if data == "" or data == None:
        return render_template('pages/placeholder.relations.html', result=None)
    else:
        print(relations.main(data))
        return render_template('pages/placeholder.relations.html', result=relations.main(data))


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()