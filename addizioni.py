from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def addizioni():
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)
    if request.method == 'POST':
        if request.form['input'] == request.cookies.get('risultato'):
            return render_template("giusto.html", risultato=request.form['input'])
        else:
            return render_template("sbagliato.html", risultato_sbagliato=request.form['input'], risultato_corretto=request.cookies.get('risultato'))
    else:
        resp = make_response(render_template("index.html", numero1=str(n1), numero2=str(n2)))
        resp.set_cookie('risultato', str(n1+n2))
        return resp
