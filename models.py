from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet Model"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, unique=True,
                   primary_key=True, autoincrement=True)

    name = db.Column(db.String, nullable=False)

    species = db.Column(db.String, nullable=False)

    photo_url = db.Column(
        db.Text, default='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/dog-face_1f436.png')

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, nullable=False, default=True)
