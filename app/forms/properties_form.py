from flask_wtf import FlaskForm
from wtforms import StringField 
from wtforms import DecimalField 
from wtforms.validators import DataRequired
from wtforms import FileField
from wtforms import TextAreaField
from wtforms import IntegerField
from wtforms import SelectField



class PropertiesForm(FlaskForm) :
    title = StringField("Property Title",validators=[DataRequired()])
    num_bedrooms = IntegerField("Number of Bedrooms",validators=[DataRequired()])
    num_bathrooms = IntegerField("Number of Bathrooms",validators=[DataRequired()])
    location = TextAreaField("Location",validators=[DataRequired()])
    price = DecimalField("Price of The Property",validators=[DataRequired()])
    image = FileField("Image of Property",validators=[])
    description = TextAreaField("The Property Description",validators=[DataRequired()])
    type = SelectField('Type', choices=[('1','House'),('2','Apartment')])

    class Meta :
        csrf = True