from flask import Flask

apito = Flask(__name__)

@apito.route('/doDeyv')
def ola():
    return 'Hola'

apito.run()