from flask import Flask, render_template

app = Flask(__name__)

@app.route('/rota1')
def home():
    return render_template('site.html')

app.run()

@app.route('/rota2')
def ola():
    return 'Hola'

app.run()