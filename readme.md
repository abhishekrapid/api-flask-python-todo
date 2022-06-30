<p align="center">
  <a href="https://www.rapidinnovation.io/" target="blank"><img src="static/images/ri_logo.jpeg" width="320" alt="RapidInnovation Logo" /></a>
</p>

## TODO List using flask api


Checkout *requirements.txt* for libraries used.

**Versions**
Python: 3.7

### Activate Virtual env
python -m venv venv
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Postgresql must have in your system.


### Add Envioroment variables
Please refer .env_example for the env variables that is needed


### Run the application
python run.py

### Test the application
[Click Here](http://127.0.0.1:5000/)


### How to run the application

I created four endpoint for testing/running the application.

1. For Fetching all the TODO task.
        
   http://127.0.0.1:5000/
2. For adding new TODO task.
    http://127.0.0.1:5000/add + send Task name in form data with "todoitem" key.

3. For changing the status from incomplete to complete by task id.
    http://127.0.0.1:5000/complte/<id>    , where id is task id

4. For delete the task by task id.
    http://127.0.0.1:5000/delete/<todo_id> , where todo_id is task id.
