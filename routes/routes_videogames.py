from flask import request, jsonify, Blueprint, render_template, session
from models.repositories.repository import obtenerRepositoriovideogames
import datetime
repo_videogames = obtenerRepositoriovideogames()

bp_videogames = Blueprint("bp_videogames", __name__)

@bp_videogames.route("/videogames", methods=["GET"])
def getVideogames():
    if session.get("username") is not None:
        current_user = session.get("username")
        response = [videogame.toDict() for videogame in repo_videogames.getAllGames()]
        is_navigator = "Mozilla" in request.user_agent.string or "Chrome" in request.user_agent.string
        if is_navigator:
            return render_template("all_games.html", videogames=response, current_user=current_user)
        else:
            return jsonify(response), 200
    else:
        return render_template("login.html")

@bp_videogames.route("/videogames/<int:id>", methods = ["GET"])
def getVideogame(id):
    if session.get("username") is not None:
        try:
            current_user = session.get("username")
            videogame = repo_videogames.obtenerPorID(id)
            is_navigator = 'Mozilla' in request.user_agent.string or 'Chrome' in request.user_agent.string
            if repo_videogames.existeID(id):
                response = jsonify([videogame.toDict()])
                status_code = 200
                if is_navigator:
                    print(videogame.toDict())
                    return render_template("game.html",videogame=videogame.toDict(), current_user=current_user)
            else:
                response = jsonify({"error": "El videogame no existe"})
                status_code = 404
                if is_navigator:
                    return render_template("game.html", response=response, status_code=status_code, id=id)
            return response, status_code
        except Exception:
            return jsonify({"error": "Internal Server Error"}), 500
    else:
        return render_template("login.html")
    
@bp_videogames.route("/videogames/post-game")
def formAddVideogame():
    if session.get("username") is not None:
        return render_template("post_game.html")
    else:
        return render_template("login.html")

@bp_videogames.route("/videogames", methods = ["POST"])
def agregarvideogame():
    if session.get("username") is not None:
        is_navigator = "Mozilla" in request.user_agent.string or "Chrome" in request.user_agent.string
        try:
            data = request.form
            if not ("id" in data and "title" in data and "my_opinion" in data and "completed" in data and "my_score" in data and "favourite" in data):
                response = jsonify ({"error": "Faltan datos"})
                status_code = 400
            else:
                id = int(data["id"])
                title = data["title"]
                my_opinion = data["my_opinion"]
                completed = data.get("completed", "false").lower() == "true"
                my_score = int(data["my_score"])
                favourite = data.get("favourite", "false").lower() == "true"
                if repo_videogames.addVideogame(id, title, my_opinion, completed, my_score, favourite):
                    
                    videogames = [videogame.toDict() for videogame in repo_videogames.getAllGames()]
                    if is_navigator:
                        return render_template("all_games.html", videogames=videogames)
                    response = jsonify({"mensaje": "Juego agregado satisfactoriamente."}), 201
                    status_code = 201
                else:
                    if is_navigator:
                        return render_template("post_game.html", exists="error", id = id)
                    response = jsonify({"error": "El videogame ya existe."})
                    status_code = 400
            return response, status_code
        except Exception:
            if is_navigator:
                return render_template("post_game.html", error="error")
            return jsonify({"error": "Internal Server Error"}), 500
    else:
        return render_template("login.html")

@bp_videogames.route("/videogames/update-game")
def formUpdateVideogame():
    if session.get("username") is not None:
        videogames = [videogame.toDict() for videogame in repo_videogames.getAllGames()]
        return render_template("update_game.html", videogames = videogames)
    else:
        return render_template("login.html")

@bp_videogames.route("/videogames/<int:id>", methods = ["PUT"])
def updateVideogame(id):
    if session.get("username") is not None:
        try:
            data = request.json
            print(data)
            if not ("id" in data and "title" in data and "my_opinion" in data and "completed" in data and "my_score" in data and "favourite" in data):
                response = jsonify({"error": "Faltan datos"})
                status_code = 400
            else:
                id = int(data["id"])
                title = data["title"]
                my_opinion = data["my_opinion"]
                completed = str(data.get("completed", "false")).lower() == "true"
                my_score = int(data["my_score"])
                favourite = str(data.get("favourite", "false")).lower() == "true"
                if repo_videogames.updateVideogame(id, title, my_opinion, completed, my_score, favourite):
                    response = jsonify({"error": "videogame modificado satisfactoriamente"})
                    status_code = 200
                else:
                    response = jsonify({"error": "No se encontró el videogame"})
                    status_code = 404
            return response, status_code
        except Exception:
            return jsonify({"error": "Internal Server Error"}), 500
    else:
        return render_template("login.html")

@bp_videogames.route("/videogames/delete-game")
def formularioEliminarvideogame():
    if session.get("username") is not None:
        listado_videogames = [videogame.toDict() for videogame in repo_videogames.getAllGames()]
        return render_template("delete_game.html", videogames = listado_videogames)
    else:
        return render_template("login.html")

@bp_videogames.route("/videogames/<int:id>", methods = ["DELETE"])
def eliminarvideogame(id):
    if session.get("username") is not None:
        try:
            if repo_videogames.existeID(id):
                if repo_videogames.deleteVideogame(id):
                    response = jsonify({"mensaje": "videogame eliminado satisfactoriamente"})
                    status_code = 200
                else:
                    response = jsonify({"error": "No se pudo eliminar el videogame."})
                    status_code = 400
            else:
                response = jsonify({"error": "No se encontró el videogame"})
                status_code = 404
            return response, status_code
        except Exception:
            return jsonify({"error": "Internal Server Error"}), 500
    else:
        return render_template("login.html")
        
