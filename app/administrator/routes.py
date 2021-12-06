from flask import render_template, redirect, flash, url_for, request
from app import db
from app.administrator import bp
from app.administrator.forms import AddSubjectForm, AddTeacherForm
from flask_login import login_required
from app.models import Subject, Teacher, User


@bp.route('/registros')
@login_required
def registros():
    usuarios = User.query
    return render_template('administrator/registros.html', title='Listado de Usuarios', usuarios=usuarios)

@bp.route('/listaprofesores')
@login_required
def teachersadded():
    teachers = Teacher.query
    return render_template('administrator/teachersadded.html', title='Listado de Profesores', teachers=teachers)

@bp.route('/listamaterias')
@login_required
def subjectsadded():
    subjects = Subject.query
    return render_template('administrator/subjectsadded.html', title='Listado de Materias', subjects=subjects)


@bp.route('/materias', methods=['GET', 'POST'])
@login_required
def subject():
    form = AddSubjectForm()
    if form.validate_on_submit():
        materia = Subject(name=form.subject_name.data,
                        description=form.description.data,
                        )
        periodo = Period(name=form.subject_name.data,
                        start=form.start.data,
                        end=form.end.data
                        )
        dia = WeekDay(name=form.name.data)
        horario = ClassSchedule(capacity=form.capacity.data
                                #id_teacher=
                                #id_materia=
                                #id_periodo=
                                )
        hours = Hours(start=form.start.data,
                    end=form.start.data
                    #id_class
                    )

        db.session.add(materia, periodo, dia, horario, hours)
        db.session.commit()
        flash('Clase Agregada')
        return redirect(url_for('administrator.subjectsadded'))
    return render_template('administrator/materias.html', title='Materias', form=form)

@bp.route('/profesores', methods=['GET', 'POST'])
@login_required
def teacher():
    form = AddTeacherForm()
    if form.validate_on_submit():
        profesor = Teacher(name=form.name.data,
                        last_name=form.last_name.data,
                        dni=form.dni.data,
                        status=form.status.data
                            )
        db.session.add(profesor)
        db.session.commit()
        flash('Profesor Agregado')
        return redirect(url_for('administrator.teachersadded'))
    return render_template('administrator/teachers.html', title='Profesores', form=form)
