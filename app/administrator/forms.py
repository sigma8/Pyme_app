from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, DateTimeField, IntegerField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Email
from app.models import User, Teacher, Subject



class AddSubjectForm(FlaskForm):
    name = StringField('Materia', validators=[DataRequired()])
    description = StringField('Descripcion', validators=[DataRequired()])
    start = DateTimeField('Inicio', format='%Y/%m/%d', validators=[DataRequired()], description="YYYY/MM/DD")
    end = DateTimeField('Fin', format='%Y/%m/%d', validators=[DataRequired()], description="YYYY/MM/DD")
    day = SelectField('Dia', choices=["Lun", "Mar", "Mie", "Jue", "Vie", "Sab"])
    capacity = IntegerField('Capacidad', validators=[DataRequired()])
    #teacher = IntegerField('Profesor id', validators=[DataRequired()])
    enter = SubmitField('Agregar')


class AddTeacherForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    last_name = StringField('Apellido', validators=[DataRequired()])
    dni = StringField('DNI', validators=[DataRequired()])
    status = SelectField('Estado',
                        choices=["No activo", "Activo"])
    enter = SubmitField('Agregar')
