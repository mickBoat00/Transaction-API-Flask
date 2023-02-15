from flask import Blueprint

bank = Blueprint('bank', __name__)

@bank.route("/")
def home():
    return {'success': 'New one'}, 200