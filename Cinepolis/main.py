from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        return procesar(request.form)
    else:
        return render_template("formulario.html")

def procesar(form_data):
    nombre = form_data.get("nombre")
    cantidad_boletos = int(form_data.get("nBoletos"))
    cantidad_compradores = int(form_data.get("nCompradores"))
    tarjeta_cineco = form_data.get("tarjetaCineco") == "si"

    if cantidad_compradores > 7:
        return render_template("formulario.html", resultado="Error: No se puede tener más de 7 compradores.")

    precio_boleto = 12.0
    total = precio_boleto * cantidad_boletos
    
    if cantidad_boletos > 5:
        descuento = 0.15  
    elif 3 <= cantidad_boletos <= 5:
        descuento = 0.10 
    else:
        descuento = 0.0

    total_con_descuento = total - (total * descuento)

    if tarjeta_cineco:
        descuento_adicional = 0.10  # 10% adicional
        total_con_descuento -= (total_con_descuento * descuento_adicional)

    resultado = "El total a pagar por {} es: ${:.2f}".format(nombre, total_con_descuento)
    return render_template("formulario.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
