import enum
import hashlib

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Enum, DateTime, Double
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


class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


# class Phone(Base):
#     phone_number = Column(String(10), unique=True)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
#     phone_type = Column(String(50))


class User(Base1, UserMixin):
    __abstract__ = True
    last_name = Column(String(50), nullable=False)
    frist_name = Column(String(50), nullable=False)

    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100),
                    default='https://cdn.tgdd.vn/Files/2016/05/04/824270/tim-hieu-cac-cong-nghe-man-hinh-dien-thoai-5.jpg')
    # phones = relationship(Phone, backref='user', lazy=True)
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    active = Column(Boolean, default=True)

    def __str__(self):
        return self.name


class Student(User):
    student_class = relationship('student_class', backref='student', lazy=True)


class Class(Base2):
    size = Column(Integer, nullable=False)
    grade_id = Column(Integer, ForeignKey('grade.id'), nullable=False)
    student_class = relationship('student_class', backref='class', lazy=True)
    subject_teacher_class = relationship('subject_teacher_class', backref='class', lazy=False)
    homeroom_teacher_id = Column(Integer, ForeignKey('teacher.id'), unique=True, nullable=False)

        # u = User(name='Admin', username='admin',
        #          password= str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role = UserRoleEnum.ADMIN)
        # u = User(name='Duong Van Khanh', username = 'khanh',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        # )

        # u = User(name='Cao Ngoc Son', username='Son',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        # )


class Grade(Base2):
    classes = relationship('class', backref='grade', lazy=True)


class Student_Class(Base1):
    student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
    class_id = Column(Integer, ForeignKey(Class.id), nullable=False)
    semester_id = Column(Integer, ForeignKey('semester.id'), nullable=False)
    score = relationship('score', backref='student_class',
                         lazy=True)


class Teacher(User):
    degree = Column(String(50), nullable=False)
    homeroom_class = relationship('class', back_populates='homeroom_teacher', uselist=False)
    subject_teacher = relationship('subject_teacher', backref='teacher', lazy=True)
    head_subject = relationship('subject', backref='teacher', lazy=True)


class Semester(Base2):
    year_id = Column(Integer, ForeignKey('year.id'), nullable=False)
    students_classes = relationship(Student_Class, backref='semester', lazy=True)


class Year(Base1):
    year = Column(Integer, nullable=False)
    semesters = relationship(Semester, backref='year', lazy=True)


class Subject(Base2):
    subject_teacher = relationship('subject_teacher', backref='subject', lazy=True)
    head_teacher = Column(Integer, ForeignKey(Teacher.id), nullable=False, unique=True)


class Subject_Teacher(Base1):
    subject_id = Column(Integer, ForeignKey(Subject.id), nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teacher.id), nullable=False)
    date_joined = Column(DateTime, default=datetime.now())
    subject_teacher_class = relationship('subject_teacher_class', backref='subject_teacher', lazy=False)


class Subject_Teacher_Class(Base1):
    subject_teacher_id = Column(Integer, ForeignKey(Subject_Teacher.id), nullable=False)
    class_id = Column(Integer, ForeignKey(Class.id), nullable=False)
    score = relationship('score', backref='subject_teacher_class', lazy=True)


class Score(Base1):
    student_class_id = Column(Integer, ForeignKey(Student_Class.id), nullable=False)
    subject_teacher_class_id = Column(Integer, ForeignKey(Subject_Teacher_Class.id), nullable=False)
    score = Column(Double)
    typeofscore_id = Column(Integer, ForeignKey('typeofscore.id'), nullable=False)


class TypeOfScore(Base2):
    __tablename__ = 'typeofscore'
    factor = Column(Double, nullable=False)
    scores = relationship(Score, backref='typeofscore', lazy=True)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        g1 = Grade(id=1, name='10')
        g2 = Grade(id=2, name='11')
        g3 = Grade(id=3, name='12')
        db.session.add_all([g1, g2, g3])

        # st1 = Student(id=1, last_name='Duong', first_name='Van Khanh', username='khanh', password='khanh')
        # st2 = Student(id=2, last_name='Dang', first_name='Trung Thang', username='thang', password='thang')
        # st3 = Student(id=3, last_name='Cao', first_name='Ngoc Son', username='son', password='son')
        # db.session.add_all([st1, st2, st3])
        #
        # s1 = Semester(id=1, name='Hocki 1')
        #
        # t1 = Teacher(id=1, degree='ThacSi', last_name='Duong', first_name='Huu Thanh', username='thanh',
        #              password='thanh')
        # t2 = Teacher(id=2, degree='ThacSi', last_name='Ho', first_name='Huong Thien', username='thien',
        #              password='thien')
        # t3 = Teacher(id=3, degree='ThacSi', last_name='Ho', first_name='Van Thanh', username='thanhh',
        #              password='thanhh')
        # db.session.add_all([t1, t2, t3, s1])
        #
        # c1 = Class(id=1, grade_id=1, homeroom_teacher_id=1, name='A1')
        #
        # sc1 = Student_Class(id=1, student_id=1, class_id=1, semester_id=1)
        # db.session.add_all([c1, sc1])
        db.session.commit()
