from app import app, db
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user
from flask import redirect
from app.models import Student, Teacher, Subject, TypeOfPhone, Staff, SetOfPermission, Permission_SetOfPermission
from wtforms import StringField, validators

admin = Admin(app=app, name="STUDENT MANAGEMENT", template_mode='bootstrap4')


class BaseView(ModelView):
    create_template = 'admin/models/create.html'
    column_editable_list = ['phone', 'email']
    column_list = ['last_name', 'first_name', 'date_of_birth', 'email', 'phone', 'phone_type', 'username', 'password',
                   'active', 'setofpermission']
    column_searchable_list = ['first_name', 'first_name']
    column_filters = ['last_name', 'first_name', 'active', 'setofpermission']


class TypeOfPhoneView(ModelView):
    column_list = ['id', 'name', 'student']


class SetOfPermissionView(ModelView):
    column_list = ['name', 'student', 'teacher', 'permission_setofpermission']


admin.add_view(BaseView(Student, db.session, name="Manage Students"))
admin.add_view(ModelView(Teacher, db.session))
admin.add_view(ModelView(Staff, db.session))
admin.add_view(ModelView(Subject, db.session))
admin.add_view(TypeOfPhoneView(TypeOfPhone, db.session))
admin.add_view(SetOfPermissionView(SetOfPermission, db.session))
admin.add_view(ModelView(Permission_SetOfPermission, db.session))
