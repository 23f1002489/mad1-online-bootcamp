from flask import Flask ,render_template , redirect , url_for,request
from .models import *
from app import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email = email , password = password).first()
        if user and user.role == 0:
            return redirect(url_for("admin", email = email))
        elif user and user.role == 1:
            return redirect(url_for("user", email= email))
        else:
            return render_template("Login.html", msg = "Invalid user")
        
    return render_template("Login.html")

@app.route("/register", methods=["GET", "POST"])
def Register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email = email , password = password).first()
        if user:
            return render_template("Register.html", msg= "User already exists !!")
        newuser = User(email = email, password = password)
        db.session.add(newuser)
        db.session.commit()
        return render_template("Login.html", msg = "You can login and continue")
    return render_template("Register.html")

@app.route("/admin/<email>")
def admin(email):
    return f"Hello Admin !! {email}"
    # # courses = get_courses()
    # return render_template("admin.html", email=email, courses=courses)

@app.route("/user/<email>")
def user(email):
    return f"Hello User !! {email}"
    # courses = get_courses()
    # return render_template("User.html", email=email, courses=courses)

 