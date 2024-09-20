from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.teachers import Teacher
from core.libs import assertions

from .schema import AssignmentSchema,AssignmentGradeSchema,TeacherSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments',methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def list_assigments(p):
    principal_assignments=Assignment.get_assignments_by_principal()
    principal_assignments_dump = AssignmentSchema().dump(principal_assignments, many=True)
    return APIResponse.respond(data=principal_assignments_dump)

@principal_assignments_resources.route('/assignments/grade',methods=['POST'],strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def mark_assignment(p,incoming_payload):
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    graded_assignment = Assignment.mark_grade(
    _id=grade_assignment_payload.id,
    grade=grade_assignment_payload.grade,
    auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)

@principal_assignments_resources.route('/teachers',methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def get_teachers(p):
    assertions.assert_auth(p.principal_id,'Not authorized')
    principal_teachers=Teacher.filter()
    principal__teachers_dump = TeacherSchema().dump(principal_teachers, many=True)
    return APIResponse.respond(data=principal__teachers_dump)




