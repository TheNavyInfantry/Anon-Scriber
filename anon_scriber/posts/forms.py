from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired
from anon_scriber import datetime

class PostForm(FlaskForm):
    title = StringField(label='Title: ', validators=[Length(min=1, max=60), DataRequired()])
    post_text = TextAreaField(label='Your Post: ', validators=[Length(min=1, max=1024), DataRequired()])
    time_stamp_of_post = StringField(label="Posted on: ", default=datetime.utcnow)
    submit = SubmitField(label='Share')