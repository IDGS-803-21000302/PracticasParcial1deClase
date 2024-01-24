from  flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def formulario1():
    return render_template("formulario1.html")


@app.route("/resultado",methods=["GET","POST"])
def resultado():
    if request.method=="POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        operacion = request.form.get("operacion")

        if operacion == "mult":
            return "<h1>La multiplicacion es: {}<h1> ".format(str(int(num1)*int(num2)))
    
        elif operacion == "suma":
            return "<h1>La suma es: {}<h1> ".format(str(int(num1)+int(num2)))
    
        elif operacion == "resta":
            return "<h1>La diferencia es: {}<h1> ".format(str(int(num1)-int(num2)))
    
        elif operacion == "div":
            return "<h1>La divicion es: {}<h1> ".format(str(int(num1)/int(num2)))
    
        


if __name__== "__main__":
    app.run(debug=True)