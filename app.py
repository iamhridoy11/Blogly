"""Blogly application."""
from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, User

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogy_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

"""Home page"""


@app.route('/')
def home_page():
    """Show list of all users from the database"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('list.html', users=users)


"""New user add"""


@app.route('/add_new')
def new_user():
    """New user page"""

    return render_template('newuser.html')


"""Posting new user to the psql database"""


@app.route('/add_new', methods=["POST"])
def create_users():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    image_url = image_url if image_url else None

    new_user = User(first_name=first_name,
                    last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/')


"""Show user details"""


@app.route('/user_details/<int:user_id>')
def show_user(user_id):
    """Show details about a single user"""
    found_user = User.query.get_or_404(user_id)

    return render_template('details.html', user=found_user)


"""Edit an existing user"""


@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    """Edit user details"""

    found_user = User.query.get_or_404(user_id)

    return render_template('edit.html', user=found_user)


"""Post updated user"""


@app.route('/edit/<int:user_id>', methods=["POST"])
def post_edit_user(user_id):
    """Post user details information (Edited) to the psql database"""

    found_user = User.query.get_or_404(user_id)

    found_user.first_name = request.form["first_name"]
    found_user.last_name = request.form["last_name"]
    found_user.image_url = request.form["image_url"]

    db.session.add(found_user)
    db.session.commit()

    return redirect('/')


"""Delete an user"""


@app.route('/delete/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    found_user = User.query.get_or_404(user_id)
    db.session.delete(found_user)
    db.session.commit()

    return redirect('/')
