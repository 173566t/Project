from flask import Flask,render_template

app = Flask(__name__)


@app.route('/homepage')
def homepage():
    return render_template('draft_homepage.html')

@app.route('/fixedDeposit')
def fixedDeposit():
    return render_template('draft_FD.html')

@app.route('/topUp')
def topupAmt():
    return render_template('draft_fdPart2.html')


if __name__ == '__main__':
    app.run()
