import threading
import webbrowser
from flask import Flask, render_template, request
from tools import bmi_calculate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    message = "hello"
    message_class = ""
    if request.method =="POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        bmi = round(bmi_calculate(weight, height),2)
        if bmi < 18:
            message = "You have underweight - eat more!"
            message_class = "too-thin"
        elif bmi >= 18 and bmi <= 24:
            message = "You have normal weight - great!"
            message_class = "normal"

        elif bmi > 24:
            message = "You are too fat - eat less!"
            message_class = "too-fat"

    return render_template("index.html", bmi=bmi, message=message, message_class=message_class)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")
    
if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(debug=True, use_reloader=False)
