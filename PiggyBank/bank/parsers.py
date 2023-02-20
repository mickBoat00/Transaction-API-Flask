from flask_restful import reqparse

currency_post_parser = reqparse.RequestParser()
currency_post_parser.add_argument('code', required=True, help='Currency code must be provided.')
currency_post_parser.add_argument('name', required=True, help='Currency name must be provided.')

category_post_parser = reqparse.RequestParser()
category_post_parser.add_argument('name', required=True, help='Category name must be provided.')

transaction_post_parser = reqparse.RequestParser()
transaction_post_parser.add_argument('amount', required=True, help='Amount must be provided.')
transaction_post_parser.add_argument('currency_id', required=True, help='Currency must be provided.')
transaction_post_parser.add_argument('category_id', required=True, help='Category must be provided.')
transaction_post_parser.add_argument('description', required=True, help='Description must be provided.')
transaction_post_parser.add_argument('date', help='Date must be provided.')
