"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from crypt import methods
from app import app
import os
from flask import flash, render_template, request, redirect, url_for, send_from_directory
from app.forms.properties_form import PropertiesForm
from werkzeug.utils import secure_filename
from app.models import Property
import locale
from . import db

def format_price(properties) :
    for property in properties :
        property.price = locale.format("%d", property.price, grouping=True)
    return properties


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/',methods=['GET'])
def properties():
    properties = db.session.query(Property).all()
    locale.setlocale(locale.LC_ALL, 'en_US')
    properties = format_price(properties);
    return render_template("properties.html",properties=properties)

@app.route('/property/<propertyid>',methods=['GET'])
def get_property(propertyid):
    property = Property.query.filter_by(id=propertyid).first()
    #locale.setlocale(locale.LC_ALL, 'en_US')
    #properties = format_price(properties);
    return render_template("property.html",property=property)

@app.route('/property/img/<filename>',methods=['GET'])
def get_property_img(filename):
    uploads = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])
    return send_from_directory(uploads,filename)


@app.route('/property/create/',methods=['GET','POST'])
def create_property() :
    propertiesForm = PropertiesForm()
    if request.method == "POST" : 
        form_valid_on_submit = True#propertiesForm.validate_on_submit();
        if (form_valid_on_submit) :
            propertyName = propertiesForm.title.data
            num_bathrooms = propertiesForm.num_bathrooms.data
            num_bedrooms = propertiesForm.num_bedrooms.data
            price = propertiesForm.price.data
            location = propertiesForm.location.data
            description = propertiesForm.description.data
            image = propertiesForm.image.data
            type = propertiesForm.type.data
            print(type)

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename))
            
            image.save(file_path)
            property = Property(propertyName,num_bedrooms,num_bathrooms,location,price,image.filename,description,type)
            db.session.add(property)
            db.session.commit()
            flash("The Property was successfully created")
            return redirect(url_for("properties"))
        else :
            flash("Please enter the correct fields")
    return render_template('create-property.html',form=propertiesForm)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
