"""Module that handles methods for the employee schema"""

from marshmallow import fields, Schema

class EmployeeSchema(Schema):
    """Schema for employee data"""
    first_name = fields.String(required=True, attribute='firstName')
    last_name = fields.String(required=True, attribute='lastName')
    job_title = fields.String(attribute='jobTitle')
    company = fields.String(required=True)
    interest = fields.String(require=False)
    hobbies = fields.String(required=False)
