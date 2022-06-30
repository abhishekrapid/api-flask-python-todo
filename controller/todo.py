from model.todo import db, Note


def add_note(todoitem):
    try:
        note = Note(text=todoitem, complete=False)
        db.session.add(note)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def complete_note(id):
    try:
        note = Note.query.filter_by(id=id).first()
        note.complete = True
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_note(id):
    try:
        note = Note.query.filter_by(id=id).first()
        # note.complete = True
        db.session.delete(note)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False