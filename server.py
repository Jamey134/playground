# from flask import Flask, render_template
# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("test.html", phrase="hello", times=5)	# notice the 2 new named arguments!
if __name__=="__main__":
    app.run(debug=True)




@app.route('/hello')

def hello_world():
    return'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}'


@app.route('/hello/<name>/<food>')
def hello_name_food(name, food):
    return f'Hello {name}, my favorite food is: {food}'



if __name__=="__main__":
        app.run( debug=True, port=5001 )