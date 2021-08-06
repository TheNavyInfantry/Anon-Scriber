from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
@main.route("/home")
def index():
    return render_template("index.html")

@main.errorhandler(404)
def error_404(e):
    return render_template('404_error.html'), 404