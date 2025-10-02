// Buscador de temas
document.getElementById("search").addEventListener("keypress", function(e) {
  if (e.key === "Enter") {
    const query = this.value.toLowerCase();
    if (query.includes("impropia")) {
      window.location.href = "pages/impropias.html";
    } else if (query.includes("partes")) {
      window.location.href = "pages/partes.html";
    } else if (query.includes("sustituc")) {
      window.location.href = "pages/sustituciones.html";
    } else if (query.includes("fracciones")) {
      window.location.href = "pages/fracciones.html";
    } else if (query.includes("área") || query.includes("area")) {
      window.location.href = "pages/area.html";
    } else if (query.includes("volumen")) {
      window.location.href = "pages/volumen.html";
    } else {
      window.location.href = "#temas"; // por defecto lo manda al índice
    }
  }
});

// Calculadora con Sympy vía API de Python (ejemplo básico)
async function calcular() {
  let expr = document.getElementById("expression").value;
  let op = document.getElementById("operation").value;
  let resultado = document.getElementById("resultado");
  let pasos = document.getElementById("pasos");

  // Aquí se podría integrar Pyodide o un backend en Flask/Django
  if (op === "derivada") {
    resultado.innerHTML = `Derivada de ${expr}: 2x + 3 (ejemplo estático)`;
    pasos.innerHTML = "Paso 1: Diferenciar x² → 2x<br>Paso 2: Diferenciar 3x → 3<br>Paso 3: Sumar → 2x + 3";
  } else {
    resultado.innerHTML = `Integral de ${expr}: (x³/3) + (3x²/2) + C (ejemplo estático)`;
    pasos.innerHTML = "Paso 1: Integrar x² → x³/3<br>Paso 2: Integrar 3x → (3x²/2)<br>Paso 3: Sumar + C";
  }
}