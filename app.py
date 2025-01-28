from flask import Flask
from flask_mysqldb import MySQL
from routes.routes_videogames import bp_videogames
from routes.routes_auth import bp_auth

app = Flask(__name__, template_folder="views/templates", static_folder="views/static")
app.secret_key = 'MyProject'

app.register_blueprint(bp_auth)
app.register_blueprint(bp_videogames)


if __name__ == '__main__':
    app.run(debug=True, port=8000)