import math
from flask import render_template, request, redirect, jsonify, url_for
import dao
from app import app, login
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user_login", methods=['post', 'get'])
def user_login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user)
            return redirect(url_for("index"))
    return render_template("user_login.html")


@app.route("/user_register", methods=['post', 'get'])
def user_register():
    return render_template("user_register.html")


@app.route("/user_logout")
def user_logout():
    logout_user()
    return redirect(url_for("user_login"))

@app.route("/ministry/create_student_profile")
def create_student():
    return render_template("ministry/create_student.html")

@app.route("/teacher/make_scoreboard")
def make_scoreboard():
    return render_template("/teacher/make_scoreboard.html")

@app.route("/ministry/make_class")
def make_class():
    return render_template("ministry/make_class.html")


@app.route("/admin/login", methods=['post'])
def admin_login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user)
    return redirect("/admin")


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
