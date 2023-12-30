#
# from app import app, db
# from flask_admin import Admin, BaseView, expose
# from flask_admin.contrib.sqla import ModelView
# from flask_login import logout_user, current_user
# from flask import redirect
#
# admin = Admin(app=app, name='Student Management', template_mode='bootstrap4')
#
#
# class AuthenticatedAdmin(ModelView):
#     def is_accessible(self):
#         return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN
#
#
# class AuthenticatedUser(BaseView):
#     def is_accessible(self):
#         return current_user.is_authenticated
#
#
# class MyStatsView(AuthenticatedUser):
#     @expose("/")
#     def index(self):
#         return self.render('admin/stats.html')
#
#
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
#
#
# admin.add_view(MyStudentsView(name='Student'))
# admin.add_view(MyClassesView(name='Classes'))
# admin.add_view(MySubjectsView(name='Subjects'))
# admin.add_view(MyStatsView(name='Statistics'))
# admin.add_view(LogoutView(name='Logout'))