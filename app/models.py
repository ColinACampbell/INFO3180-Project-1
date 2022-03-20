from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(80))
    num_bedrooms = db.Column(db.Integer)
    num_bathrooms = db.Column(db.Integer)
    location =  db.Column(db.String(400))
    price = db.Column(db.Integer)
    imagePath = db.Column(db.String(200))
    description = db.Column(db.String(400))

    def __init__(self,title,bedrooms,bathrooms,location,price,imagePath,description) :
        self.title = title
        self.num_bedrooms = bedrooms
        self.num_bathrooms = bathrooms
        self.location = location
        self.price = price
        self.imagePath = imagePath
        self.description = description
        