from PiggyBank import db
from datetime import datetime

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False,)
    transactions = db.relationship('Transaction', backref='currency', lazy=True)

    def __repr__(self) -> str:
        return f"Currency(code={self.code}, name={self.name})"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    transactions = db.relationship('Transaction', backref='category', lazy=True)

    def __repr__(self) -> str:
        return f"Category(name={self.name})"


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    description = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Transaction(amount={self.amount}, currency={self.currency.code}, date={self.date})"