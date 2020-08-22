from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/../index.html', methods=['GET', 'POST'])
def form():
    return render_template('/../index.html')


@app.route('/../index.html#contact', methods=['GET', 'POST'])
def submit():
    return render_template('/index.html', say=request.form['say'], to=request.form['to'])


if __name__ == "__main__":
    app.run()
