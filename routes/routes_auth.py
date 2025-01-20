from flask import Blueprint, request, redirect, url_for, session, render_template
from passlib.hash import pbkdf2_sha256

bp_auth = Blueprint("bp_auth", __name__)

@bp_auth.route("/")
def PaginaPrincipal():
    if session.get('username') is None:
        return render_template("login.html")
    else:
        return redirect(url_for('bp_videogames.getVideogames'))

@bp_auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = pbkdf2_sha256.hash(request.form.get("password"))
        if username == 'user' and pbkdf2_sha256.verify(request.form.get("password"), pbkdf2_sha256.hash("admin")):
            print(password)
            session['username'] = username
            return redirect(url_for('bp_videogames.getVideogames'))
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos")
    else:
        return render_template("login.html")
    
@bp_auth.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('bp_auth.PaginaPrincipal'))