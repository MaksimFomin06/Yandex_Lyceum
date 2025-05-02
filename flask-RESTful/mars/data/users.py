import datetime
from flask_login import UserMixin
import sqlalchemy
from data.db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String)
    speciality = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    city_from = sqlalchemy.Column(sqlalchemy.String)
    
    jobs = sqlalchemy.orm.relationship("Jobs", back_populates="user")

    def to_dict(self, only=()):
        user_dict = {
            'id': self.id,
            'surname': self.surname,
            'name': self.name,
            'age': self.age,
            'position': self.position,
            'speciality': self.speciality,
            'address': self.address,
            'email': self.email,
            'city_from': self.city_from,
            'modified_date': self.modified_date.isoformat() if self.modified_date else None
        }

        if only:
            return {key: user_dict[key] for key in only if key in user_dict}
            
        return user_dict

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return (f"{self.surname} {self.name} {self.age} {self.position} {self.speciality}\n"
                f"{self.address} {self.email} {self.hashed_password}")