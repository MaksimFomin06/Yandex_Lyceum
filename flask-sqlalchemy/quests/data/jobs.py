import sqlalchemy
from sqlalchemy import orm
from datetime import datetime
from data.db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(
        sqlalchemy.Integer, 
        sqlalchemy.ForeignKey('users.id')
    )
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    
    user = orm.relationship('User')

    def __repr__(self):
        return (f"{self.team_leader} {self.job} {self.work_size} "
                f"{self.collaborators} {self.is_finished}")