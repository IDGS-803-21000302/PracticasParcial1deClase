from flask import Flask, render_template, request
import form
from math import sqrt


app = Flask(__name__)

@app.route("/cinepolis", methods=["GET", "POST"])
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
        descuento_adicional = 0.10 
        total_con_descuento -= (total_con_descuento * descuento_adicional)

    resultado = "El total a pagar por {} es: ${:.2f}".format(nombre, total_con_descuento)
    return render_template("formulario.html", resultado=resultado)


@app.route("/numeros",methods=["GET","POST"])
def num():
    numForm= form.NumsFrom(request.form)
    totalFinal=0
    if request.method=='POST':
        x1=numForm.x1.data
        x2=numForm.x2.data
        y1=numForm.y1.data
        y2=numForm.y2.data
        print("x1: {}".format(int(x1)))
        print("x2: {}".format(int(x2)))
        print("y1: {}".format(int(y1)))
        print("y2: {}".format(int(y2)))
        total1 = (int(x2)-int(x1))**2
        total2 = (int(y2)-int(y1))**2

        print("total1: {}".format(int(total1)))
        print("Total2: {}".format(int(total2)))

        total3 = int(total1)+int(total2)
        print("total primera parte {}".format(int(total3)))

        totalFinal = sqrt(total3)
        print("total {}".format(int(totalFinal)))

    return render_template("formularioDistancia.html",form=numForm,total=totalFinal)



@app.route("/resistencias",methods=["GET","POST"])
def resistencias():
    resistenciasForm= form.resistenciasForm(request.form)
    totalToleranciaMin=0
    totalToleranciaMax=0
    total1=0
    primeraBanda=''
    segundaBanda=''
    terceraBanda=''
    porcentaje =''
    colorbanda1=''
    colorbanda2=''
    colorbanda3=''
    colorTolerancia=''
    
    if request.method=='POST':
        primeraBanda = resistenciasForm.primeraBanda.data
        segundaBanda = resistenciasForm.segundaBanda.data
        terceraBanda = resistenciasForm.terceraBanda.data
        tolerancia = resistenciasForm.tolerancia.data
        print("x1: {}".format(primeraBanda))
        print("x2: {}".format(segundaBanda))
        print("y1: {}".format(terceraBanda))
        print("y2: {}".format(tolerancia))
        valorBanda1=0
        colorbanda1=''
        colorbanda2=''
        colorbanda3=''
        

        if primeraBanda == 'negro':
            valorBanda1=0
            colorbanda1='black'
        elif primeraBanda == 'cafe':
            valorBanda1=1
            colorbanda1='#8B4513'
        elif primeraBanda == 'rojo':
            valorBanda1=2
            colorbanda1='#FF0000'
        elif primeraBanda == 'naranja':
            valorBanda1=3
            colorbanda1= '#FFA500'
        elif primeraBanda == 'amarillo':
            valorBanda1=4
            colorbanda1='#FFFF00'
        elif primeraBanda == 'verde':
            valorBanda1=5
            colorbanda1='#008000'
        elif primeraBanda == 'azul':
            valorBanda1=6
            colorbanda1='#0000FF'
        elif primeraBanda == 'violeta':
            valorBanda1=7
            colorbanda1='#EE82EE'
        elif primeraBanda == 'gris':
            valorBanda1=8
            colorbanda1='#808080'
        elif primeraBanda == 'blanco':
            valorBanda1=9
            colorbanda1='#FFF'

        print("banda 1: {}".format(valorBanda1))

        valorBanda2=0
        
        if segundaBanda == 'negro':
            valorBanda2=0
            colorbanda2='black'
        elif segundaBanda == 'cafe':
            valorBanda2=1
            colorbanda2='#8B4513'
        elif segundaBanda == 'rojo':
            valorBanda2=2
            colorbanda2='#FF0000'
        elif segundaBanda == 'naranja':
            valorBanda2=3
            colorbanda2= '#FFA500'
        elif segundaBanda == 'amarillo':
            valorBanda2=4
            colorbanda2='#FFFF00'
        elif segundaBanda == 'verde':
            valorBanda2=5
            colorbanda2='#008000'
        elif segundaBanda == 'azul':
            valorBanda2=6
            colorbanda2='#0000FF'
        elif segundaBanda == 'violeta':
            valorBanda2=7
            colorbanda2='#EE82EE'
        elif segundaBanda == 'gris':
            valorBanda2=8
            colorbanda2='#808080'
        elif segundaBanda == 'blanco':
            valorBanda2=9
            colorbanda2='#FFF'
        print("banda 2: {}".format(valorBanda2))

        valorBanda3=0
        
        if terceraBanda == 'negro':
            valorBanda3=1
            colorbanda3='black'
        elif terceraBanda == 'cafe':
            valorBanda3=10
            colorbanda3='#8B4513'
        elif terceraBanda == 'rojo':
            valorBanda3=100
            colorbanda3='#FF0000'
        elif terceraBanda == 'naranja':
            valorBanda3=1000
            colorbanda3= '#FFA500'
        elif terceraBanda == 'amarillo':
            valorBanda3=10000
            colorbanda3='#FFFF00'
        elif terceraBanda == 'verde':
            valorBanda3=100000
            colorbanda3='#008000'
        elif terceraBanda == 'azul':
            valorBanda3=1000000
            colorbanda3='#0000FF'
        elif terceraBanda == 'violeta':
            valorBanda3=10000000
            colorbanda3='#EE82EE'
        elif terceraBanda == 'gris':
            valorBanda3=100000000
            colorbanda3='#808080'
        elif terceraBanda == 'blanco':
            valorBanda3=1000000000
            colorbanda3='#FFF'
        print("banda 3: {}".format(valorBanda3))

        totalConjunto = "{}{}".format(valorBanda1,valorBanda2)

        print("Total conjunto: {}".format(int(totalConjunto)))

        total1 = int(totalConjunto)*int(valorBanda3)

        print("Total : {}".format(int(total1)))

        totalTolerancia=0
        porcentaje=''
        colorTolerancia=''
        if tolerancia == 'oro':
            totalToleranciaPor= float(total1)*0.05
            print("TotalPor : {}".format(int(totalToleranciaPor)))
            totalToleranciaMin = float(total1)- float(totalToleranciaPor)
            totalToleranciaMax = float(total1)+ float(totalToleranciaPor)
            colorTolerancia='#CFB53B'
            porcentaje='5%'
        else:
            totalToleranciaPor= float(total1)*0.10
            print("TotalPor : {}".format(int(totalToleranciaPor)))
            totalToleranciaMin = float(total1)- float(totalToleranciaPor)
            totalToleranciaMax = float(total1)+ float(totalToleranciaPor)
            colorTolerancia='#C0C0C0'
            porcentaje='10%' 

        print("Total tolerancia min: {}".format(int(totalToleranciaMin)))
        print("Total tolerancia min: {}".format(int(totalToleranciaMax)))
        
        
    return render_template("formularioResistencias.html",form=resistenciasForm,totalToleranciaMin=totalToleranciaMin,totalToleranciaMax=totalToleranciaMax,total1=total1,primeraBanda=primeraBanda,segundaBanda=segundaBanda,terceraBanda=terceraBanda,porcentaje=porcentaje,colorbanda1=colorbanda1,colorbanda2=colorbanda2,colorbanda3=colorbanda3,colorTolerancia=colorTolerancia)






if __name__ == "__main__":
    app.run(debug=True)
