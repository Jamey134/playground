from flask import Flask, render_template
app = Flask(__name__)


# route to create three lightblue boxes
@app.route('/play')
def play():
    return render_template('index.html')

# route to create seven or any amount of boxes
@app.route('/play/<int:x>')
def play_x(x):
    return render_template('index_2.html', x = x)

# route to create various amount of boxes and change colors
@app.route('/play/<int:x>/<string:color>')
def play_x_color(x, color):
    return render_template('index_3.html', x = x, color = color)







if __name__=="__main__":
    app.run( debug=True, port=5001 )