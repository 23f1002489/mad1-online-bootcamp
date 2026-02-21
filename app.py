from flask import Flask, render_template, request

from flask import Flask
from backend.models import db
# from backend.routes import *

app = None

def setup():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_database"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app) # connection between db and app
    app.app_context().push() # direct access to modules
    print("App is started !!")
    return app

app = setup()

from backend.routes import *
# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        admin = User.query.filter_by(email="admin@gmail.com").first()
        if not admin :
            admin = User(
                email = "admin@gmail.com",
                password = "1234",
                role = 0
            )
            db.session.add(admin)
            db.session.commit()
            print("Admin created successfully !!")
        else:
            print("Admin already exists !!")
    app.run(debug=True)
# app = Flask(__name__)
# @app.route("/", methods=["GET", "POST"])
# def index():
#     return "Hello, World!   This is a simple Flask application."


# if __name__ == "__main__":
#     app.run(debug=True)
