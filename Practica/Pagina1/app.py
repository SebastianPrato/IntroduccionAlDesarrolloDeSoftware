from flask import Flask, redirect, render_template, request, url_for
import requests

app = Flask(__name__)

API_BASE = "http://localhost:5000"


def obtener_mensajes():
    response = requests.get(f"{API_BASE}/historial")
    if response.status_code == 200:
        return response.json()
    return None

def guardar_mensaje(mensaje):
    response = requests.post(
        f"{API_BASE}/guardar", 
        json={"mensaje":mensaje},
    )
    if response.status_code == 201:
        return True
    return None

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        mensaje = request.form.get("mensaje", "").strip()
        if mensaje:
            guardar_mensaje(mensaje)
        return redirect(url_for("home"))
    return render_template('index.html')



@app.route("/historial", methods=["GET"])
def mostrar_historial():
    mensajes = obtener_mensajes()
    return render_template('historial.html', mensajes=mensajes)

if __name__ == "__main__":
    app.run("127.0.0.1", port=3000, debug=True)