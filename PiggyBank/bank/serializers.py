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