"""Simple script to show how marshmallow marshals json through a schema"""

import json

from marshmallow import pprint
from schemata.employee import EmployeeSchema

# Raw json to be serialized
json_data = '{"firstName": "Brian", "lastName": "Rose", "jobTitle": "Engineer","company": "Company"}'

# Converted raw json to Python dictionary
json_dict = json.loads(json_data)

# Initialize schema
schema = EmployeeSchema()

# Serialize the json by dumping through schema 
serialized_json = schema.dumps(json_dict)

# Result of serialization
pprint(serialized_json.data)
