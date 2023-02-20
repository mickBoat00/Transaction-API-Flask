from flask_restful import fields

currency_fields = {
    'id': fields.Integer,
    'code': fields.String,
    'name': fields.String,
}

category_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

transaction_fields = {
    'id': fields.Integer,
    'category': fields.Nested(category_fields),
    'currency': fields.Nested(currency_fields),
    'amount': fields.Float,
    'description': fields.String,
    'date': fields.DateTime, 
}