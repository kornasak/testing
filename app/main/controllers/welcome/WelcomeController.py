from flask_restplus import Namespace, Resource, fields
from flask import Flask, jsonify, request


api = Namespace('welcome', description='Welcome')

@api.route('/print')
@api.doc(responses={
        0: 'success'
    })
class WelcomeText(Resource):
    resource_fields = api.model('PRINT_WELCOME_TEXT', {
        'text' : fields.String(required=False, description='test', example='test')
    })

    @api.expect(resource_fields, validate=True)
    def post(self):
        data = request.json
        return data