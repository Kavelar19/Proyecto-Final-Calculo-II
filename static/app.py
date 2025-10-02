from flask import Flask, render_template, request, jsonify
import sympy as sp

app = Flask(__name__)

# Rutas para tus páginas
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/definida")
def definida():
    return render_template("definida.html")

@app.route("/indefinida")
def indefinida():
    return render_template("indefinida.html")

@app.route("/partes")
def partes():
    return render_template("partes.html")

@app.route("/sustitucion")
def sustitucion():
    return render_template("sustitucion.html")

# API para cálculo de integrales definidas
@app.route("/calcular_integral_def", methods=["POST"])
def calcular_integral_def():
    try:
        data = request.json
        funcion = data["funcion"]
        a = float(data["a"])
        b = float(data["b"])

        x = sp.Symbol("x")
        expr = sp.sympify(funcion)

        # Integral definida
        integral = sp.integrate(expr, (x, a, b))
        pasos = f"∫[{a},{b}] {funcion} dx = {integral}"

        return jsonify({"resultado": str(integral), "pasos": pasos})
    except Exception as e:
        return jsonify({"error": str(e)})

# API para cálculo de integrales indefinidas
@app.route("/calcular_integral_indef", methods=["POST"])
def calcular_integral_indef():
    try:
        data = request.json
        funcion = data["funcion"]

        x = sp.Symbol("x")
        expr = sp.sympify(funcion)

        # Integral indefinida
        integral = sp.integrate(expr, x)
        pasos = f"∫ {funcion} dx = {integral} + C"

        return jsonify({"resultado": str(integral), "pasos": pasos})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)