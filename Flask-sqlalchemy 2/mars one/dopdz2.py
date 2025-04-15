from sqlalchemy import func
from data.users import User
from data.departments import Department
from data.jobs import Jobs
from data.db_session import create_session, global_init


def main():
    db = input()
    global_init(db)
    session = create_session()

    result = session.query(User.surname, User.name)\
        .join(Department, User.id == Department.id)\
        .join(Jobs, User.id == Jobs.team_leader)\
        .filter(Department.id)\
        .group_by(User.id)\
        .all()
    
    output = [f"{surname} {name}" for surname, name in result]
    print(sorted(output))


if __name__ == "__main__":
    main()