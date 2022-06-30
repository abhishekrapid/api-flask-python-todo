from config.flask_config import app
from flask import (
    jsonify,
    request
)
from model.todo import Note
from sqlalchemy import desc
from controller.todo import (
    add_note,
    complete_note,
    delete_note
)


# home route
@app.route('/')
def home():
    # making the data to render from a descending order according to the datetime
    incomplete = [{'ID': i.id, 'Name': i.text} for i in Note.query.filter_by(complete=False).order_by(desc(Note.date)).all()]
    complete = [{'ID': i.id, 'Name': i.text} for i in Note.query.filter_by(complete=True).order_by(desc(Note.date)).all()]
    return jsonify({'Incomplete': incomplete, 'Complete': complete})


# route for adding todos
@app.route('/add', methods=['POST'])
def add():
    response_data = {
        'status': 404,
        'message': 'Something went wrong.',
    }
    status = add_note(request.form['todoitem'])
    if status:
        response_data['status'] = '200'
        response_data['message'] = 'New note added successfully.'
    return jsonify(response_data)


# route to mark completed task
@app.route('/complete/<id>')
def complete(id):
    response_data = {
        'status': 404,
        'message': 'Something went wrong.',
    }
    status = complete_note(int(id))
    if status:
        response_data['status'] = '200'
        response_data['message'] = 'Task has been completed.'
    return jsonify(response_data)


@app.route("/delete/<todo_id>")
def delete(todo_id):
    response_data = {
        'status': 404,
        'message': 'Something went wrong.',
    }
    status = delete_note(int(todo_id))
    if status:
        response_data['status'] = '200'
        response_data['message'] = 'Task has been removed from the Todo list.'
    return jsonify(response_data)


# initiating the flask framework
if __name__ == "__main__":
    app.run(debug=True)