from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionRequest(FlaskForm):
    query = StringField("query", validators=[
        DataRequired(message="Query is required"),
        Length(max=2000, message="Query Maximum length is 2000 characters")
    ])
