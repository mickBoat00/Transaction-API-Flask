from flask import Blueprint
from flask_restful import Resource, Api, marshal_with

from PiggyBank import db

from PiggyBank.bank.models import Currency, Category, Transaction
from PiggyBank.bank.parsers import currency_post_parser, category_post_parser
from PiggyBank.bank.serializers import currency_fields, category_fields

bank = Blueprint('bank', __name__, url_prefix='/api')

api = Api(bank)


class CurrencyList(Resource):
    @marshal_with(currency_fields)
    def get(self):
        currencies = Currency.query.all()
        return currencies, 200

    @marshal_with(currency_fields)
    def post(self):
        args = currency_post_parser.parse_args()
        currency = Currency(**args)
        db.session.add(currency)
        db.session.commit()
        return currency, 200

api.add_resource(CurrencyList, '/currencies/')


class CategoryList(Resource):
    @marshal_with(category_fields)
    def get(self):
        categories = Category.query.all()
        return categories, 200

    @marshal_with(category_fields)
    def post(self):
        args = category_post_parser.parse_args()
        category = Category(**args)
        db.session.add(category)
        db.session.commit()
        return category, 200


class CategoryResource(Resource):
    @marshal_with(category_fields)
    def get(self, category_id):
        category = Category.query.filter_by(id=category_id).first_or_404(description=f'No category with id {category_id}')
        return category, 200

    @marshal_with(category_fields)
    def put(self, category_id):
        args = category_post_parser.parse_args()
        category = Category.query.filter_by(id=category_id).first_or_404(description=f'No category with id {category_id}')
        category.name = args.get('name', '')
        db.session.commit()
        return category, 201

    @marshal_with(category_fields)
    def delete(self, category_id):
        category = Category.query.filter_by(id=category_id).first_or_404(description=f'No category with id {category_id}')
        db.session.delete(category)
        db.session.commit()
        return category, 204

api.add_resource(CategoryList, '/categories/')
api.add_resource(CategoryResource, '/categories/<int:category_id>/')