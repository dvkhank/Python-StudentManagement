import math
from functools import wraps

from flask import render_template, request, redirect, jsonify, url_for, session
import dao
from app import app, login
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("user_login"))
    else:
        set_of_permission_id = session['set_of_permission_id']
        list_of_permission = dao.load_permission(set_of_permission_id=set_of_permission_id)
    return render_template("index.html", list_of_permission=list_of_permission)


@app.route("/user_login", methods=['post', 'get'])
def user_login():
    error_message = None
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        set_of_permission = request.form.get('set_of_permission')
        print(set_of_permission)
        user = dao.auth_user(username=username, password=password, set_of_permission=set_of_permission)
        if user:
            login_user(user)
            print(user.username)
            session['set_of_permission_id'] = user.setofpermission
            return redirect(url_for("index"))
        else:
            error_message = 'There is no user like that'
    set_of_permission = dao.load_setofpermission()
    return render_template("user_login.html", set_of_permission=set_of_permission, error_message=error_message)


@app.route("/user_register", methods=['post', 'get'])
def user_register():
    return render_template("user_register.html")


@app.route("/user_logout")
def user_logout():
    logout_user()
    if 'set_of_permission_id' in session:
        del session['set_of_permission_id']
    return redirect(url_for("user_login"))







# @app.route("/admin/login", methods=['post'])
# def admin_login():
#     username = request.form.get("username")
#     password = request.form.get("password")
#     user = dao.auth_user(username=username, password=password, set_of_permission_id = 4)
#     if admin:
#         login_user(user)
#     return redirect("/admin")


@app.route("/manage_users", methods=['post', 'get'])
def manage_users():
    set_of_permission = dao.load_setofpermission()
    type_of_phone = dao.load_phonetype()
    if request.method.__eq__('POST'):

        last_name = request.form.get("last_name")
        first_name = request.form.get("first_name")
        date_of_birth = request.form.get("date_of_birth")
        email = request.form.get("email")
        phone = request.form.get('phone')
        phone_type = request.form.get('phone_type')
        degree = request.form.get('degree')
        username = request.form.get('username')
        password = request.form.get("password")
        set_of_permission_id = request.form.get('permission')
        if (set_of_permission_id == 1):
            degree = request.form.get('degree')
            dao.add_user(last_name=last_name, first_name=first_name, date_of_birth=date_of_birth, email=email,
                         phone=phone,
                         phone_type=phone_type, degree=degree, username=username, password=password,
                         set_of_permission_id=set_of_permission_id)
        if (set_of_permission_id == 2):
            dao.add_user(last_name=last_name, first_name=first_name, date_of_birth=date_of_birth, email=email,
                         phone=phone,
                         phone_type=phone_type, degree=degree, username=username, password=password,
                         set_of_permission_id=set_of_permission_id)
    return render_template('add_users.html', set_of_permission=set_of_permission, type_of_phone=type_of_phone)


@app.route("/profile")
def profile_user():
    set_of_permission_id = session['set_of_permission_id']
    if current_user.is_authenticated:
        user = dao.get_user_by_id(current_user.id, set_of_permission_id)
    return render_template('profile.html', user=user)


@login.user_loader
def load_user(user_id):
    set_of_permission_id = session['set_of_permission_id']
    user = dao.get_user_by_id(user_id, set_of_permission_id)
    return user


# @app.context_processor
# def common_response():
#     permission_id = None
#     if permission_id:
#         permission = dao.load_permission(permission_id)
#         return {"permission": permission}


if __name__ == '__main__':
    from app import admin

    app.run(debug=True)
