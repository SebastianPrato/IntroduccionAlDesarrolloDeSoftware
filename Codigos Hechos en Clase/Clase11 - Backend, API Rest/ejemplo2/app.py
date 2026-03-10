from flask import Flask, render_template, request

import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/formulario', methods=['GET', 'POST'])
def enviar_formulario():
    if request.method == 'POST':
        return enviar_formulario_post()
    return enviar_formulario_get()

def enviar_formulario_post():
    error = None
    resultado = None
    response = requests.get('http://localhost:8080/response')
    if response.status_code != 200:
        error = "Algo salio mal"
    else:
        resultado = f'request enviada. Respuesta: {response.json()}'
    return render_template('formulario.html', error=error, resultado=resultado)

def enviar_formulario_get():
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
