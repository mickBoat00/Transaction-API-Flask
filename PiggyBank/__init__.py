from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bank.db"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from PiggyBank.bank.routes import bank

    @app.route('/two')
    def two():
        return {'success': 'another one'}, 200

    app.register_blueprint(bank)


    

    return app