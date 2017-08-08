from marshmallow import fields, Schema

class EmployeeSchema(Schema):
    first_name = fields.String(required=True, attribute='firstName')
    last_name = fields.String(required=True, attribute='lastName')
    job_title = fields.String(attribute='jobTitle')
    company = fields.String(required=True)
