import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship


department_members = sqlalchemy.Table(
    'department_members',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('department_id', sqlalchemy.Integer, 
                     sqlalchemy.ForeignKey('departments.id')),
    sqlalchemy.Column('user_id', sqlalchemy.Integer,
                     sqlalchemy.ForeignKey('users.id'))
)


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    email = sqlalchemy.Column(sqlalchemy.String)
    
    members = orm.relationship("User",
                             secondary="department_members",
                             backref="departments")
    
    chief_user = orm.relationship("User", foreign_keys=[chief])
