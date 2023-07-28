import uuid

from flask import Flask, render_template
from flask_cors import CORS
from flask_restx import Api

from api.models import setup_db
from api.routes.posts import posts_bp
from api.schemas import setup_marshmallow
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
api.add_namespace(posts_bp)

setup_db(app)
setup_marshmallow(app)

cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/api/uuid/", methods=["GET"])
def get_uuid():
    return str(uuid.uuid4())


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5002, debug=True)
