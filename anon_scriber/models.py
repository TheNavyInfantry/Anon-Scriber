from anon_scriber import db, datetime, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=50), unique=True, nullable=False)
    email_address = db.Column(db.String(length=60), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter # hashes password
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password): # checks whether hashed passwords are matched or not
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f"{self.username} - {self.email_address} - {self.password_hash}\n{self.posts}"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=60), nullable=False, unique=True)
    post = db.Column(db.String(length=1024), nullable=False, unique=True)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.user_id} - {self.title}\n{self.post} - {self.time_stamp}"
