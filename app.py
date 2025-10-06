from flask import Flask, render_template, request, jsonify
import sympy as sp

app = Flask(__name__)

# Rutas para tus páginas
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/tecnicas")
def tecnicas():
    return render_template("tecnicas.html")

@app.route("/definida")
def definida():
    return render_template("pages/definida.html")

@app.route("/indefinida")
def indefinida():
    return render_template("pages/indefinida.html")

@app.route("/partes")
def partes():
    return render_template("pages/partes.html")

@app.route("/sustitucion")
def sustitucion():
    return render_template("pages/sustitucion.html")
@app.route("/Volumen")
def volumen():
    return render_template("pages/volumen.html")
@app.route("/impropias")
def impropias():
    return render_template("pages/impropias.html")
    




# --------------------------
# API para calcular integrales
# --------------------------

@app.route("/api/integral_definida", methods=["POST"])
def integral_definida():
    data = request.json
    expr_str = data.get("funcion", "")
    a = float(data.get("a", 0))
    b = float(data.get("b", 0))

    x = sp.symbols('x')
    try:
        expr = sp.sympify(expr_str)
        integral = sp.integrate(expr, (x, a, b))
        pasos = f"∫[{a},{b}] {expr_str} dx = {integral}"
        return jsonify({
            "resultado": str(integral),
            "pasos": pasos
        })
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/api/integral_indefinida", methods=["POST"])
def integral_indefinida():
    data = request.json
    expr_str = data.get("funcion", "")

    x = sp.symbols('x')
    try:
        expr = sp.sympify(expr_str)
        integral = sp.integrate(expr, x)
        pasos = f"∫ {expr_str} dx = {integral} + C"
        return jsonify({
            "resultado": str(integral),
            "pasos": pasos
        })
    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == "__main__":
    app.run(debug=True)
    