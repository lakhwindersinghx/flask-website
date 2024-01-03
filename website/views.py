from flask import Blueprint,render_template,request,flash
from flask_login import current_user,login_required
from .models import Note
from . import db



views=Blueprint('views', __name__)


@views.route('/',methods=['POST','GET'])
@login_required
def home():
    if request.method=="POST":
        note=request.form.get('note')

        if len(note)<1:
            flash('Note is too short',category='error')
        else:
            new_note=Note(data=note)
            db.session.add(new_note)
            db.session.commit()
            flash('NOTE ADDED!',category='success')
    return render_template('home.html',user=current_user)