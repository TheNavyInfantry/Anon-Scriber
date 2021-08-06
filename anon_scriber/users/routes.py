from anon_scriber import db
from anon_scriber.users.forms import RegisterForm, LoginForm
from anon_scriber.models import User, Post
from flask import render_template, redirect, url_for, flash, request, session, Blueprint
from flask_login import current_user, login_user, logout_user, login_required
from anon_scriber.main.routes import error_404

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register_page():

    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password.data)

        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)

        flash(f"Hey {user_to_create.username}! Your account has successfully created and logged into the website!", category='success')

        return redirect(url_for('posts.shared_posts'))

    if form.errors != {}: # To make sure that there aren't errors from validations
        for error_message in form.errors.values():
            flash(f'{error_message}', category='danger') # This category has a connection to base.html

    return render_template("register.html", form=form)



@users.route('/login', methods=['GET', 'POST'])
def login_page():

    form = LoginForm()

    if form.validate_on_submit():
        """
        1) Checks if the user is exists,
        2) Checks if the user and password are exists
        """
        attempted_user = User.query.filter_by(email_address=form.email_address.data).first()

        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):

            login_user(attempted_user)

            session.permanent = True

            session.modified = True

            flash(f"You have successfully logged in as {attempted_user.username}", category='success')

            return redirect(url_for('posts.shared_posts'))

        else:
            flash(f"Username and Password do NOT match! Please try again!",  category='danger')

    return render_template("login.html", form=form)


@users.route('/logout')
@login_required
def logout_page():
    logout_user()

    flash("You have successfully logged out!", category='warning')

    return redirect(url_for('main.index'))

@users.route('/user/<int:id>', methods=['GET', 'POST'])
@login_required
def user_posts(id):

    page = request.args.get('page', 1, type=int)

    user = User.query.filter_by(id=id).first_or_404()

    posts = Post.query.filter_by(user=user)\
        .order_by(Post.time_stamp.desc())\
        .paginate(page=page, per_page=6) #To get latest records from db

    return render_template("userposts.html", posts=posts, user=user)