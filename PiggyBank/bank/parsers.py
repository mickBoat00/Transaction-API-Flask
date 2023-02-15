from flask_restful import reqparse

currency_post_parser = reqparse.RequestParser()
currency_post_parser.add_argument('code', required=True, help='Currency code must be provided.')
currency_post_parser.add_argument('name', required=True, help='Currency name must be provided.')

category_post_parser = reqparse.RequestParser()
category_post_parser.add_argument('name', required=True, help='Category name must be provided.')