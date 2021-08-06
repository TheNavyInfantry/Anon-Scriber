from anon_scriber import db
from anon_scriber.posts.forms import PostForm
from anon_scriber.models import User, Post
from flask import render_template, redirect, url_for, flash, request, abort, Blueprint
from flask_login import current_user, login_user, logout_user, login_required

posts = Blueprint('posts', __name__)

@posts.route('/share', methods=['GET', 'POST'])
@login_required # Blocks unauthorized accesses
def post_page():

    form = PostForm()

    if form.validate_on_submit():
        post_to_create = Post(title=form.title.data,
                              post=form.post_text.data,
                              user_id=current_user.id)

        db.session.add(post_to_create)

        try:
            db.session.commit()
            flash(f"Hey! Your post has successfully shared!", category='success')

            return redirect(url_for('posts.shared_posts'))

        except:
            return redirect(url_for('main.error_404'))

    else:
        return render_template("sharepost.html", form=form)


@posts.route('/posts', methods=['GET', 'POST'])
@login_required
def shared_posts():

    user_sum = db.session.query(User).count()

    page = request.args.get('page', 1, type=int)

    posts = Post.query.order_by(Post.time_stamp.desc()).paginate(page=page, per_page=6) #To get latest records from db

    return render_template("posts.html", posts=posts, user_sum=user_sum)



@posts.route('/user/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):

    post = Post.query.get_or_404(post_id)

    if post.user != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    flash(f"Your post has been deleted!", category='success')

    return redirect(url_for('posts.shared_posts'))