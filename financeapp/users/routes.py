from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from financeapp.users.forms import RegistrationForm, LoginForm
from financeapp.models import User
from financeapp import db



users = Blueprint('users', __name__)


@users.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('chart'))
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u and u.check_password(form.password.data):
            login_user(u, remember=form.remember.data)
            flash("You have logged in successfully!", "success")
            return redirect(url_for('chart_blueprint.chart'))
        else:
            flash('Invalid email or password', 'danger')
            #return redirect(url_for('login'))
    return render_template('login.html', form=form)

@users.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('chart_blueprint.chart'))
    form = RegistrationForm()
    if form.validate_on_submit():
        u = User(username=form.username.data, email=form.email.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash('You registered successfully!', 'success')
        return redirect(url_for('users.login'))
    else:
        return render_template('register.html', form=form)

@users.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash('You have logged out!', 'success')
    return redirect(url_for('chart_blueprint.chart'))