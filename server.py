from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route('/dojo')
def dojo():
    return "<h1>Dojo!</h1>"

@app.route('/say/<string:name>')
def say_name(name):
    return f'<h1>Hi, {name}</h1>'

@app.route('/repeat/<int:number>/<string:word>')
def repeat_word(number,word):
    return (f'<h2>{word}</h2>' * number)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error="Page not found"),404


if __name__ == '__main__':
    app.run(debug=True)