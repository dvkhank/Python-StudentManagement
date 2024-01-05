
from app import app, db
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user
from flask import redirect
from app.models import Student
admin = Admin(app=app, name='Student Management', template_mode='bootstrap4')
admin.add_view(ModelView(Student, db.session))

class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.setofpermission == 4



# class MyStudentsView(AuthenticatedUser):
#     @expose("/")
#     def index(self):
#         return self.render('admin/student.html')
#
#
# class MyClassesView(AuthenticatedUser):
#     @expose("/")
#     def index(self):
#         return self.render('admin/class.html')
#
#
# class MySubjectsView(AuthenticatedUser):
#     @expose("/")
#     def index(self):
#         return self.render('admin/subject.html')
#
#
# class LogoutView(AuthenticatedUser):
#     @expose("/")
#     def index(self):
#         logout_user()
#         return redirect("/admin")

