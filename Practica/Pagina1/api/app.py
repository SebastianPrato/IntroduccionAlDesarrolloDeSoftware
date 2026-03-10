from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

@app.route("/historial")
def obtener_mensajes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                   SELECT contenido 
                   FROM mensajes""")
    mensajes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(mensajes), 200

@app.route("/guardar", methods=["POST"])
def guardar_mensaje():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    mensaje = request.json.get("mensaje")
    cursor.execute("""
                    INSERT INTO mensajes (contenido)
                   VALUES (%s)
                   """, (mensaje, ))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"Mensaje": "Mensaje cargado a la base de datos con éxito"}), 201

if __name__ == '__main__':
    app.run(debug=True)