from app.models import Teacher,Student, SetOfPermission, Permission_SetOfPermission, Permission
from app import app, db
import hashlib


def get_user_by_id(user_id):
    return Teacher.query.get(user_id)


def load_permission(permission_id):
    permission = db.session.query(Permission, SetOfPermission, Permission_SetOfPermission).filter(
        Permission.id == Permission_SetOfPermission.permission_id,
        SetOfPermission.id == Permission_SetOfPermission.set_of_permission_id, SetOfPermission.id == permission_id
    ).all()
    return permission


def load_setofpermission():
    return SetOfPermission.query.all()


def auth_user(username, password, permission):
    # password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    with app.app_context():
        if permission == '1':
            return Teacher.query.filter(Teacher.username.__eq__(username),
                                        Teacher.password.__eq__(password)).first()
        if permission == '2':
            return Student.query.filter(Student.username.__eq__(username),
                                        Student.password.__eq__(password)).first()
        if permission == '3':
            return Teacher.query.filter(Teacher.username.__eq__(username),
                                        Teacher.password.__eq__(password)).first()



