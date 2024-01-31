from flask import Flask, render_template, request
import form
from math import sqrt


app = Flask(__name__)

@app.route("/numeros",methods=["GET","POST"])
def num():
    numForm= form.NumsFrom(request.form)
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

    return render_template("formulario.html",form=numForm,total=totalFinal)



if __name__ == "__main__":
    app.run(debug=True)
