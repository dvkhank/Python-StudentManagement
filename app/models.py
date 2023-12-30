import enum
import hashlib

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Double
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin
from datetime import datetime


class Base1(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Base2(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)


class TypeOfPhone(Base2):
    student = relationship('Student', backref='typeofphone', lazy=True)
    teacher = relationship('Teacher', backref='typeofphone', lazy=True)


class User(Base1, UserMixin):
    __tablename__ = 'user'
    __abstract__ = True
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    date_of_birth = Column(DateTime, default=datetime.now())
    email = Column(String(100), nullable=False)
    phone = Column(String(10), nullable=False, unique=True)
    phone_type = Column(Integer, ForeignKey(TypeOfPhone.id), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100),
                    default='https://cdn.tgdd.vn/Files/2016/05/04/824270/tim-hieu-cac-cong-nghe-man-hinh-dien-thoai-5.jpg')
    # phones = relationship(Phone, backref='user', lazy=True)
    active = Column(Boolean, default=True)
    permission = Column(Integer, ForeignKey('setofpermission.id'), nullable=False)

    # phones = relationship('Phone', backref='user')


class Student(User):
    __tablename__ = 'student'

    student_class = relationship('Student_Class', backref='student', lazy=True)


class Class(Base2):
    __tablename__ = 'class'

    size = Column(Integer, nullable=False)
    grade_id = Column(Integer, ForeignKey('grade.id'), nullable=False)
    student_class = relationship('Student_Class', backref='class', lazy=True)
    subject_teacher_class = relationship('Subject_Teacher_Class', backref='class', lazy=False)
    homeroom_teacher_id = Column(Integer, ForeignKey('teacher.id'), unique=True, nullable=False)


class Grade(Base2):
    __tablename__ = 'grade'

    classes = relationship(Class, backref='grade', lazy=True)


class Student_Class(Base1):
    __tablename__ = 'student_class'
    student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
    class_id = Column(Integer, ForeignKey(Class.id), nullable=False)
    semester_id = Column(Integer, ForeignKey('semester.id'), nullable=False)
    score = relationship('Score', backref='student_class',
                         lazy=True)


class Teacher(User):
    __tablename__ = 'teacher'
    degree = Column(String(50), nullable=False)
    homeroom_class = relationship('Class', backref='homeroom_teacher', uselist=False)
    subject_teacher = relationship('Subject_Teacher', backref='teacher', lazy=True)
    head_subject = relationship('Subject', backref='teacher', lazy=True)


class Semester(Base2):
    __tablename__ = 'semester'

    year_id = Column(Integer, ForeignKey('year.id'), nullable=False)
    students_classes = relationship(Student_Class, backref='semester', lazy=True)


class Year(Base1):
    __tablename__ = 'year'

    year = Column(Integer, nullable=False)
    semesters = relationship(Semester, backref='year', lazy=True)


class Subject(Base2):
    __tablename__ = 'subject'

    subject_teacher = relationship('Subject_Teacher', backref='subject', lazy=True)
    head_teacher = Column(Integer, ForeignKey(Teacher.id), nullable=False, unique=True)


class Subject_Teacher(Base1):
    __tablename__ = 'subject_teacher'
    subject_id = Column(Integer, ForeignKey(Subject.id), nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teacher.id), nullable=False)
    date_joined = Column(DateTime, default=datetime.now())
    subject_teacher_class = relationship('Subject_Teacher_Class', backref='subject_teacher', lazy=False)


class Subject_Teacher_Class(Base1):
    __tablename__ = 'subject_teacher_class'

    subject_teacher_id = Column(Integer, ForeignKey(Subject_Teacher.id), nullable=False)
    class_id = Column(Integer, ForeignKey(Class.id), nullable=False)
    score = relationship('Score', backref='subject_teacher_class', lazy=True)


class Score(Base1):
    __tablename__ = 'score'
    student_class_id = Column(Integer, ForeignKey(Student_Class.id), nullable=False)
    subject_teacher_class_id = Column(Integer, ForeignKey(Subject_Teacher_Class.id), nullable=False)
    score = Column(Double)
    typeofscore_id = Column(Integer, ForeignKey('typeofscore.id'), nullable=False)


class TypeOfScore(Base2):
    __tablename__ = 'typeofscore'
    factor = Column(Double, nullable=False)
    scores = relationship(Score, backref='typeofscore', lazy=True)


class Permission(Base2):
    __tablename__ = 'permission'

    permission_setofpermission = relationship('Permission_SetOfPermission', backref='permission', lazy=True)


class SetOfPermission(Base2):
    __tablename__ = 'setofpermission'
    student = relationship(Student, backref='set_of_permission', lazy=True)
    teacher = relationship(Teacher, backref='set_of_permission', lazy=True)
    permission_setofpermission = relationship('Permission_SetOfPermission', backref='setofpermission', lazy=True)


class Permission_SetOfPermission(Base1):
    __tablename__ = 'permission_setofpermission'
    permission_id = Column(Integer, ForeignKey(Permission.id), nullable=False)
    set_of_permission_id = Column(Integer, ForeignKey(SetOfPermission.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()

        per1 = Permission(name = 'Export a scoresheet')
        per2 = Permission(name = 'Create a scoresheet')
        per3 = Permission(name = 'Create a class')
        per4 = Permission(name = 'Create a student')
        per5 = Permission(name = 'Check Result')
        db.session.add_all([per1, per2, per3, per4, per5])
        # db.session.commit()

        setper1 = SetOfPermission(name = 'Teacher')
        setper2 = SetOfPermission(name = 'Student')
        setper3 = SetOfPermission(name = 'Staff')
        db.session.add_all([setper1, setper2, setper3])
        # db.session.commit()


        setper_per1 = Permission_SetOfPermission(permission_id = 1, set_of_permission_id = 1)
        setper_per2 = Permission_SetOfPermission(permission_id = 2, set_of_permission_id = 1)
        setper_per3 = Permission_SetOfPermission(permission_id = 3, set_of_permission_id = 3)
        setper_per4 = Permission_SetOfPermission(permission_id = 4, set_of_permission_id = 3)
        setper_per5 = Permission_SetOfPermission(permission_id = 5, set_of_permission_id = 2)
        db.session.add_all([setper_per1, setper_per2, setper_per3, setper_per4, setper_per5 ])
        # db.session.commit()

        phone1 = TypeOfPhone(name='Mobile')
        phone2 = TypeOfPhone(name='Telephone')
        db.session.add_all([phone2, phone1])
        # db.session.commit()

        t1 = Teacher(last_name='Duong', first_name='Huu Thanh', date_of_birth='2000/12/06', email='thanhdt@gmail.com',
                     phone='013525432', phone_type=1, username='thanh', password='thanh', degree = 'Master', permission = 1)
        db.session.add(t1)
        db.session.commit()
