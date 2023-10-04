"""Seed file to make sample data for User for blogy_db"""

from models import User, db
from app import app

# Create all tables

db.drop_all()
db.create_all()

# If table isn't empty, empty the table
User.query.delete()

# Adding users

john = User(first_name="John", last_name="Cena",
            image_url="https://e00-marca.uecdn.es/assets/multimedia/imagenes/2023/02/05/16755519728234.jpg")
rock = User(first_name="Dwayne", last_name="Johnson",
            image_url="https://www.etonline.com/sites/default/files/styles/1280x720/public/images/2020-02/the-rock-under-armour-1280.jpg?h=3d14d278")
undertaker = User(first_name="Mark", last_name="Calaway",
                  image_url="https://pbs.twimg.com/media/Eyn127pW8AQb66W.jpg:large")

moxly = User(first_name="Steve", last_name="Moxly")

db.session.add_all([john, rock, undertaker, moxly])
db.session.commit()
