from flask import Flask, abort, redirect, render_template, request
from forms.user import LoginForm, RegisterForm
from forms.job import JobForm
from data import db_session
from data.users import User
from data.departments import Department
from data.jobs import Jobs
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "yandexlyceum_secret_key"


login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


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

@app.route("/jobs", methods=["GET", "POST"])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            is_finished=form.is_finished.data
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect("/")
    return render_template("jobs.html", title="Добавление работы", form=form)


@app.route('/edit_job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = JobForm()
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id).first()
    
    if request.method == "GET":
        if job:
            form.team_leader.data = job.team_leader
            form.job.data = job.job
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            form.start_date.data = job.start_date
            form.end_date.data = job.end_date
            form.is_finished.data = job.is_finished
        else:
            abort(404)
    
    if form.validate_on_submit():
        if job:
            job.team_leader = form.team_leader.data
            job.job = form.job.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            job.start_date = form.start_date.data
            job.end_date = form.end_date.data
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html', title='Редактирование работы', form=form)

@app.route('/delete_job/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_job(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id).first()
    
    if job and (current_user.id == job.team_leader or current_user.id == 1):
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/departments')
def departments():
    db_sess = db_session.create_session()
    deps = db_sess.query(Department).all()
    return render_template('departments.html', departments=deps)

@app.route('/add_department', methods=['GET', 'POST'])
def add_department():
    if request.method == 'POST':
        db_sess = db_session.create_session()
        
        department = Department(
            title=request.form['title'],
            chief=int(request.form['chief']),
            email=request.form['email']
        )
        
        members = request.form.getlist('members')
        for user_id in members:
            user = db_sess.query(User).get(user_id)
            if user:
                department.members.append(user)
        
        db_sess.add(department)
        db_sess.commit()
        return redirect('/departments')
    
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return render_template('edit_department.html', users=users, department=None)

@app.route('/edit_department/<int:id>', methods=['GET', 'POST'])
def edit_department(id):
    db_sess = db_session.create_session()
    department = db_sess.query(Department).get(id)
    
    if request.method == 'POST':
        department.title = request.form['title']
        department.chief = int(request.form['chief'])
        department.email = request.form['email']
        
        department.members = []
        for user_id in request.form.getlist('members'):
            user = db_sess.query(User).get(user_id)
            if user:
                department.members.append(user)
        
        db_sess.commit()
        return redirect('/departments')
    
    users = db_sess.query(User).all()
    return render_template('edit_department.html', department=department, users=users)

@app.route('/delete_department/<int:id>')
def delete_department(id):
    db_sess = db_session.create_session()
    department = db_sess.query(Department).get(id)
    
    if department:
        db_sess.delete(department)
        db_sess.commit()
    
    return redirect('/departments')


def main():
    db_session.global_init("db/mars_explorer.db")
    #add_captain()
    #add_colonist()
    #add_job()
    app.run()


if __name__ == "__main__":
    main()