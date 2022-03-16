from flask_wtf import FlaskForm
from wtforms import StringField 
from wtforms.validators import DataRequired


class PropertiesForm(FlaskForm) :
    title = StringField("Property Title",validators=[DataRequired()])
    num_bedrooms = StringField("Number of BedRooms",validators=[DataRequired()])
    num_bathrooms = StringField("Number of Bathrooms",validators=[DataRequired()])
    location = StringField("Location",validators=[DataRequired()])
    price  = StringField("Price",validators=[DataRequired()])