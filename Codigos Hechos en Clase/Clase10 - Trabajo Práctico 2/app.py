from flask_mail import Mail, Message # type: ignore
from flask import Flask, render_template, request, redirect, flash
PORT = 8080



app = Flask(__name__)

app.secret_key = 'una_clave_super_secreta'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'dinosebas2002@gmail.com'  # reemplazá
app.config['MAIL_PASSWORD'] = 'neic idax widy eucd'
app.config['MAIL_DEFAULT_SENDER'] = 'dinosebas2002@gmail.com'

mail = Mail(app)

NOMBRE_CAFETERIA = "Usina Cafetera"
info_menu = {
        1:{
            "nombre": "Pollito con verduras:3",
            "precio": "$20.000",
            "descripcion": "Um pollito bn delicioso kkkkk con verduriñas",
            "imagen":"imagenPolloAsado.png"
        },
        2:{
            "nombre": "Salted Fried Chicken",
            "precio": "$18.500",
            "descripcion": "Polllito salteado frito para comer ñami",
            "imagen":"imagenPolloCrispy.png"
        },
        3:{
            "nombre": "Italian Sauce Mushroom",
            "precio": "$14.800",
            "descripcion": "Pasta de hongos deliciosa para que te re cagues de hambre viendo la foto JSJSJFD",
            "imagen":"imagenPastaConHongos.jpg"
        },
        4:{
            "nombre": "Fried Potato w/ Garlic",
            "precio": "$10.500",
            "descripcion": "PAPITAS CON CEBOLLITA CHUCHA QUE RICO",
            "imagen":"imagenPapasConCebolla.webp"
        },
        5:{
            "nombre": "Fideos de arroz con salteado de tofu y pimiento",
            "precio": "$15.000",
            "descripcion": "delicioso plato de fideos de arroz con tofu apto vegano + full proteinas",
            "imagen":"imagenTofuSalteado.png"
        },
        6:{
            "nombre": "Tuna Roast Beef",
            "precio": "$22.000",
            "descripcion": "filete de tuna nam nam le gustaría a tu gato creo",
            "imagen":"imagenTunaBeef.jpeg"
        },
        7:{
            "nombre": "Egg with Mushroom:3",
            "precio": "$12.000",
            "descripcion": "huevitos con hongos y tomates riquisimo uma delicia jjjjj",
            "imagen":"imagenHuevosHongos.jpg"
        }
    }


@app.route('/enviar-contacto', methods=['POST'])
def enviar_contacto():
    nombre = request.form['name']
    email = request.form['email']
    mensaje = request.form['message']

    msg = Message(f"Nuevo mensaje de {nombre}",
                  recipients=['dinosebas2002@gmail.com'])
    msg.body = f"Email: {email}\n\nMensaje:\n{mensaje}"

    mail.send(msg)

    flash("Mensaje enviado correctamente :D", "success")
    return redirect('/contact')

@app.route('/')
def index():
    
    return render_template('index.html', nombre_cafeteria=NOMBRE_CAFETERIA, menu=info_menu)

@app.route('/menu')
def menu():
    return render_template('menu.html', nombre_cafeteria=NOMBRE_CAFETERIA, menu=info_menu)

@app.route('/contact')
def contact():
    return render_template('contact.html', nombre_cafeteria=NOMBRE_CAFETERIA)

if __name__ == '__main__':
    app.run(debug=True, port=PORT)