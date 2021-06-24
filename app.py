from datetime import date
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.fields.html5 import DateTimeField
from wtforms.validators import DataRequired, Length

from debugger import initialize_flask_server_debugger_if_needed


initialize_flask_server_debugger_if_needed()

#Create the object of Flask
app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'thisisverysecret'

@app.route("/")
def index():
    return render_template('index.html')
class NotificationForm(FlaskForm):
    """ Form to create a maintenance notification"""
    owner = StringField('Name', [DataRequired()])
    reason = TextField('Grund', [DataRequired(), Length(max=200)])
    since = DateTimeField('Von', [DataRequired()], default=date.today)
    until = DateTimeField('Bis', [DataRequired()], default=date.today)
    submit = SubmitField('Erfassen')

if __name__ == "__main__":
    app.run(debug=True)
