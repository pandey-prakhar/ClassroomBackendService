# core/apis/principal.py

from flask import Blueprint, jsonify
from core import db
from core.apis import decorators
from core.models.teachers import Teacher  # Import your Teacher model here
from .schema import TeacherSchema
from core.apis.responses import APIResponse

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

@principal_teachers_resources.route('/teachers', methods=['GET'])
@decorators.authenticate_principal
def get_teachers(principal):
    # Implement logic to retrieve and return all teachers
    # teachers = Teacher.query.all()
    teachers= Teacher.get_teachers_by_principal()
    teachers_dump= TeacherSchema().dump(teachers, many=True) 
    return APIResponse.respond(data=teachers_dump)
