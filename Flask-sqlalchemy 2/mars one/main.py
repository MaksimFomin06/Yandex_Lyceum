from flask import Flask, redirect, render_template
from forms.user import LoginForm, RegisterForm
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask_login import LoginManager, login_required, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "yandexlyceum_secret_key"


login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template("login.html",
                               message = "Неправильный логин или пароль",
                               form=form)
    return render_template("login.html", title = "Авторизация", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template("register.html", title="Регистрация",
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template("register.html", title="Регистрация",
                                   form=form,
                                   message="Такой пользователь уже существует")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/login")
    return render_template("register.html", title="Регистрация", form=form)


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
    #add_job()
    app.run()


if __name__ == "__main__":
    main()