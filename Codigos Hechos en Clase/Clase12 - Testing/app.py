from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify('pong'),200

datos = {
    "capital_inicial": None,
    "tasa": None,
    "anios": None,
    "monto_final": None,
}

@app.route('/interes', methods=['POST'])
def calcular_interes():
    body = request.get_json()
    datos['capital_inicial'] = body['capital_inicial']
    datos['tasa'] = body['tasa']
    datos['anios'] = body['anios']
    datos['monto_final'] = datos['capital_inicial']*(1+(datos['tasa']/100))**datos['anios']
    return jsonify({
        "capital_inicial": datos['capital_inicial'],
        "tasa": datos['tasa'],
        "anios": datos['anios'],
        "monto_final": datos['monto_final']
    }), 201

@app.route('/mostrarinteres', methods=['GET'])
def mostrar():
    return jsonify({
        "capital_inicial": datos['capital_inicial'],
        "tasa": datos['tasa'],
        "anios": datos['anios'],
        "monto_final": datos['monto_final'],
    }), 200




if __name__ == '__main__':
    app.run(port=8080, debug=True)