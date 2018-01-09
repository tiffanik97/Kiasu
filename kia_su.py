from flask import Flask,render_template

app = Flask(__name__)

@app.route('/password')
def password():
    return render_template('password.html')

@app.route('/')
def Login():
    return render_template('Login.html')

@app.route('/Home')
def Home():
    return render_template('Home.html')



@app.route('/Planner')
def Planner():
    return render_template('Planner.html')

@app.route('/Incentive')
def Incentive():
    return render_template('Incentive.html')

@app.route('/Expenses(setlimit)')
def setlimit():
    return render_template('Expenses(setlimit).html')

@app.route('/Expenses')
def Expenses():
    return render_template('Expenses.html')

@app.route('/User_Profile')
def User_Profile():
    return render_template('User_Profile.html')

@app.route('/ExchangeRate')
def ExchangeRate():
    return render_template('ExchangeRate.html')

@app.route('/saving')
def saving():
    return render_template('saving.html')

@app.route('/Confirmation1')
def confirmation1():
    return render_template('Confirmation1.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/redemption')
def redemption():
    return render_template('redemption.html')

@app.route('/redemption_cart')
def redemption_cart():
    return render_template('redemption_cart.html')

@app.route('/incentives')
def incentives():
    return render_template('incentives.html')

@app.route('/promotion')
def promotion():
    return render_template('promotion.html')

@app.route('/Topup')
def Topup():
    return render_template('Topup.html')
@app.route('/img')
def img():
    return render_template('img.html')

if __name__ == '__main__':
    app.run(debug=True)
