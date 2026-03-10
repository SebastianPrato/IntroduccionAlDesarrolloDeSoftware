from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/hello')
def pepe():
    return "Hola, soy pepe  "

@app.route('/')
def hello_world():
    return render_template(
    'home.html', 
    nombre='pala',
    numeros=[1, 2, 3, 4, 5],
    diccionario={
        'nombre':'Pala',
        'apellido': 'Cabrera',
        'edad': 23,
    }
    )
    #return 'Hello World! :3'

if __name__ == '__main__':
    app.run("localhost", port=8081, debug=True)
