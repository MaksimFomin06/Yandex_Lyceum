from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = "yandexlyceum_secret_key"


def add_captain():
    db_sess = db_session.create_session()
    captain = User(
        surname = "Scott",
        name = "Ridley",
        age = 21,
        position = "captain",
        speciality = "research engineer",
        address = "module_1",
        email = "scott_chief@mars.org",
    )
    captain.set_password("123456789")
    db_sess.add(captain)
    db_sess.commit()


def add_colonist():
    for i in range(1, 4):
        db_sess = db_session.create_session()
        colonist = User(
            surname = f"Surname{i}",
            name = f"Colonist{i}",
            age = 18 + i,
            position = "colonist",
            speciality = "None",
            address = f"module_{i}",
            email = f"colonist{i}@mars.org",
        )
        colonist.set_password(f"123456789_{i}")
        db_sess.add(colonist)
        db_sess.commit()


def add_job():
    db_sess = db_session.create_session()
    job = Jobs(
        team_leader = 1,
        job = "deployment of residential modules 1 and 2",
        work_size = 15,
        collaborators = "2, 3",
        start_date = None,
        is_finished = False
    )
    db_sess.add(job)
    db_sess.commit()


def main():
    db_session.global_init("db/mars_explorer.db")
    #add_captain()
    #add_colonist()
    add_job()
    app.run()


if __name__ == "__main__":
    main()