# core/apis/assignments/principal.py

from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from .schema import AssignmentSchema, AssignmentGradeSchema

principal_assignments_resources = Blueprint("principal_assignments_resources", __name__)
# principal_assignments_bp = Blueprint("principal_assignments", __name__, url_prefix="/principal/assignments")

@principal_assignments_resources.route("/assignments", methods=["GET"])
@decorators.authenticate_principal
def list_assignments(p):
    # Implement logic to get all submitted and graded assignments
    principal_assignments = Assignment.get_assignments_by_principal(p.principal_id)
    principal_assignments_dump = AssignmentSchema().dump(principal_assignments, many=True)
    return APIResponse.respond(data=principal_assignments_dump)

@principal_assignments_resources.route("/assignments/grade", methods=["POST"] , strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    #logic to grade or re-grade an assignment
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    graded_assignment = Assignment.mark_re_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
