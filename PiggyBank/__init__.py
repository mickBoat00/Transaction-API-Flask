from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bank.db"
    app.config["JWT_SECRET_KEY"] = "super-secret-mickeys"
    
    jwt.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)

    @app.before_first_request
    def create_db():
        db.create_all()

    from PiggyBank.bank.routes import bank


    @app.route('/two')
    def two():
        return {'success': 'another one'}, 200

    app.register_blueprint(bank)


    return app