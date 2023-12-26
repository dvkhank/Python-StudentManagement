import enum
import hashlib

from sqlalchemy import Column, Integer, String, Float,ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin



class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar =  Column(String(100),
                     default='https://cdn.tgdd.vn/Files/2016/05/04/824270/tim-hieu-cac-cong-nghe-man-hinh-dien-thoai-5.jpg')

    user_role = Column(Enum(UserRoleEnum), default= UserRoleEnum.USER)
    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()


        # u = User(name='Admin', username='admin',
        #          password= str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role = UserRoleEnum.ADMIN)
        u = User(name='Duong Van Khanh', username = 'khanh',
                 password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 )

        db.session.add(u)
        db.session.commit()










