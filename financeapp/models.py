from financeapp import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
  return User.query.get(int(id))
  # Keeps track of the log in user by storing its unique identifier in Flask's user session.


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128)) # Hash of password, not actual password! Password will go through hash before added to db
  portfolios = db.relationship('Portfolio', backref='investor', lazy='dynamic')

  def __repr__(self):
    return 'Username: {}, email: {}'.format(self.username, self.email)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

class Portfolio(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  holdings = db.relationship('Holding', backref='portfolio', lazy='dynamic')

  def __repr__(self):
    return 'Investor: {}'.format(self.investor)


class Holding(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  ticker = db.Column(db.String(6))
  shares = db.Column(db.Integer)

  def __repr__(self):
    return 'Ticker: {}, Shares: {}'.format(self.ticker, self.shares)

