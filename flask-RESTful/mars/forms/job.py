from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = IntegerField("Лидер", validators=[DataRequired()])
    job = StringField("Работа", validators=[DataRequired()])
    work_size = IntegerField("Размер работы", validators=[DataRequired()])
    collaborators = StringField("Коллаборационисты", validators=[DataRequired()])
    start_date = DateField("Начало работ", validators=[DataRequired()])
    end_date = DateField("Окончание работ", validators=[DataRequired()])
    is_finished = BooleanField("Статус работы")
    submit = SubmitField("Добавить")