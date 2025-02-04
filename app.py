from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_cors import CORS

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

cache_config = {"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 300}
app.config.from_mapping(cache_config)

db = SQLAlchemy()
db.init_app(app)
CORS(app)
cache = Cache(app)

with app.app_context():
    db.create_all()

    from flask_blueprints import weather_bp,vitals_bp

    app.register_blueprint(weather_bp.bp, url_prefix='/weather')
    app.register_blueprint(vitals_bp.bp, url_prefix='/vitals')
