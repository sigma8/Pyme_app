from app import db, login, admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from flask_admin.contrib.sqla import ModelView


#tabla usuario para el registro
class User(UserMixin, db.Model):
    __tablename__= "User"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    user_type = db.Column(db.String(24), db.ForeignKey('UserType.name'))
    password_hash = db.Column(db.String(128))
    usertype = db.relationship("UserType")
    #user_sch = db.relationship("UserSchedule")

    def __repr__(self):
        return f'{self.name}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#tabla tipo usuario, admin o alumno
class UserType(db.Model):
    __tablename__="UserType"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    #user = db.relationship("User", backref="User Type")

    def __repr__(self):
        return f'{self.name}'

#tabla para profesores
class Teacher(db.Model):
    __tablename__= "Teacher"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    dni = db.Column(db.String(12), unique=True)
    status_teacher = db.Column(db.String(24), db.ForeignKey('Status.name'))
    status = db.relationship("Status")
    #class_sch = db.relationship("ClassSchedule")

    def __repr__(self):
        return f'{self.name}'

#
class Status(db.Model):
    __tablename__="Status"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    #teacher = db.relationship("Teacher")

    def __repr__(self):
        return f'{self.name}'

#tabla para el nombre de la materia y su descripcion
class Subject(db.Model):
    __tablename__= "Subject"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(240))
    #class_sch = db.relationship("ClassSchedule")


    def __rep__(self):
        return f'{self.name}'

#tabla horario de clases donde hereda los datos de todos lo anterior
#adicion la capacidad de la clase
class ClassSchedule(db.Model):
    __tablename__= "ClassSchedule"
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.String(24), db.ForeignKey('Teacher.name'))
    subject = db.Column(db.String(24), db.ForeignKey('Subject.name'))
    calender_sch = db.Column(db.String(24), db.ForeignKey('Calender.name'))
    capacity = db.Column(db.Integer)
    teacher_name = db.relationship("Teacher")
    subject_name = db.relationship("Subject")
    calender = db.relationship("Calender")

    def __repr__(self):
        return f'<ClassSchedule {self.name}>'

class Calender(db.Model):
    __tablename__= "Calender"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))
    day_begin = db.Column(db.DateTime, default=datetime.utcnow)
    day_end = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    #class_sch = db.relationship("ClassSchedule")


    def __repr__(self):
        return f'{self.name}'

class UserView(ModelView):
    can_delete = False
    column_exclude_list = ['password_hash']
    column_labels = dict(name='Nombre', last_name='Apellido', usertype='Tipo de Usuario')
    form_colums = ("Nombres", "Apellidos", "Username", "Email")
    form_excluded_columns = ("password_hash")


class TeacherView(ModelView):
    can_delete = False
    column_labels = dict(name='Nombre', last_name='Apellido', dni='DNI', status='Estado')

admin.add_view(UserView(User, db.session))
admin.add_view(ModelView(UserType, db.session))
admin.add_view(TeacherView(Teacher, db.session))
admin.add_view(ModelView(Status, db.session))
admin.add_view(ModelView(Subject, db.session))
admin.add_view(ModelView(Calender, db.session))
admin.add_view(ModelView(ClassSchedule, db.session))
