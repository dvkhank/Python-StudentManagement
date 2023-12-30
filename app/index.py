import math
from flask import render_template, request, redirect, jsonify, url_for, session
import dao
from app import app, login
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('user_login'))
    permission_id = session['permission_id']
    permission = dao.load_permission(permission_id=permission_id)
    return render_template("index.html", permission=permission)


@app.route("/user_login", methods=['post', 'get'])
def user_login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        permission = request.form.get('permission')
        user = dao.auth_user(username=username, password=password, permission=permission)

        if user:
            login_user(user)
            session['permission_id'] = user.permission
            return redirect(url_for("index"))
    set_of_permission = dao.load_setofpermission()
    return render_template("user_login.html", setofpermission=set_of_permission)


@app.route("/user_register", methods=['post', 'get'])
def user_register():
    return render_template("user_register.html")


@app.route("/user_logout")
def user_logout():
    logout_user()
    return redirect(url_for("user_login"))


@app.route("/admin/login", methods=['post'])
def admin_login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user)
    return redirect("/admin")


@app.route("/profile")
def profile_user():
    if current_user.is_authenticated:
        user = dao.get_user_by_id(current_user.id)
    return render_template('profile.html', user=user)


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin

    app.run(debug=True)
