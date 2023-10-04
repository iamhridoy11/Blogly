"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


def connect_db(app):

    db.app = app
    db.init_app(app)


# Models go below!

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False, )
    last_name = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    def __repr__(self):
        p = self
        return f"<User_id={p.id} full_name={p.full_name()} image_url={p.image_url}>"

    def full_name(self):
        """Full name of a user"""

        return f"{self.first_name} {self.last_name}"
