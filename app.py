from unicodedata import name
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
   if request.method == "POST":
        return render_template("/fase1")
   return render_template("index.html")

@app.route("/fase1", methods=["GET", "POST"])
def fase1(): 
    if request.form.get("resposta1") == "8d9" or request.form.get("resposta1") == "8D9":
        return redirect("/fase2")  
    return render_template("fase1.html")        

@app.route("/fase2", methods=["GET", "POST"])
def fase2():
    if request.form.get("resposta2") == "10":
        return redirect("/fase3")
    return render_template("fase2.html")

@app.route("/fase3", methods=["GET", "POST"])
def fase3():
    if request.form.get("resposta3") == "9":
        return redirect("/fase4")
    return render_template("fase3.html")

@app.route("/fase4", methods=["GET", "POST"])
def fase4():
    if request.form.get("resposta4") == "d" or request.form.get("resposta1") == "D":
        return redirect("/fase5")
    return render_template("fase4.html")    

@app.route("/fase5", methods=["GET", "POST"])
def fase5():
    if request.form.get("resposta5") == "8113":
        return redirect("/fase6")
    return render_template("fase5.html")

@app.route("/fase6", methods=["GET", "POST"])
def fase6():
    if request.form.get("resposta6") == "33":
        return redirect("/fase7")
    return render_template("fase6.html")

@app.route("/fase7", methods=["GET", "POST"])   
def fase7():
    if request.form.get("resposta7") == "90":
        return redirect("/fase8")
    return render_template("fase7.html") 

@app.route("/fase8", methods=["GET", "POST"])    
def fase8():
    if request.form.get("resposta8") == "20":
        return redirect("/fase9")
    return render_template("fase8.html")

@app.route("/fase9", methods=["GET", "POST"])    
def fase9():
    if request.form.get("resposta9") == "14":
        return redirect("/fase10")
    return render_template("fase9.html")

@app.route("/fase10", methods=["GET", "POST"])    
def fase10():
    if request.form.get("resposta10") == "6":
        return redirect("/fim")
    return render_template("fase10.html")

@app.route("/fim", methods=["GET", "POST"])
def fim():
    return render_template("fim.html")

if __name__ == '__main__':
    app.run()    