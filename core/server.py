import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import jsonify
from marshmallow.exceptions import ValidationError
from core import app
from core.apis.assignments import (
    student_assignments_resources,
    teacher_assignments_resources,
    principal_assignments_resources,
)
from core.libs import helpers
from core.libs.exceptions import FyleError
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError

# Register blueprints
for resource, prefix in zip(
    [student_assignments_resources, teacher_assignments_resources, principal_assignments_resources],
    ['/student', '/teacher', '/principal']
):
    app.register_blueprint(resource, url_prefix=prefix)

@app.route('/')
def ready():
    return jsonify({'status': 'ready', 'time': helpers.get_utc_now()})

@app.errorhandler(Exception)
def handle_error(err):
    error_response = {
        FyleError: lambda: (jsonify(error=err.__class__.__name__, message=err.message), err.status_code),
        ValidationError: lambda: (jsonify(error=err.__class__.__name__, message=err.messages), 400),
        IntegrityError: lambda: (jsonify(error=err.__class__.__name__, message=str(err.orig)), 400),
        HTTPException: lambda: (jsonify(error=err.__class__.__name__, message=str(err)), err.code)
    }
    
    response = error_response.get(type(err), lambda: None)()
    if response:
        return response

    raise err

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
