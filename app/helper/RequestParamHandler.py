from flask import request
from flask_restplus import fields
from app.helper.CustomField import CustomField
# from app.main.models.RequestLogModel import RequestLogModel


class RequestParamHandler:
    def __init__(self, **kwargs):
        self.data = kwargs.get('data')

    def getRoute(self):
        return request.environ['PATH_INFO']

    def getIpaddress(self):
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ipaddress = request.environ['REMOTE_ADDR']
        else:
            ipaddress = request.environ['HTTP_X_FORWARDED_FOR']
        return ipaddress

    def getUserAgent(self):
        return request.environ['HTTP_USER_AGENT']

    def validatePayload(self, api_model):
        for key in api_model:
            if api_model[key].required and key not in self.data:
                return {
                    'responsecode' : 99,
                    'status' : 'failed',
                    'messages' : 'required field \'{}\' missing'.format(key)
                }
        for key in self.data:
            field = api_model[key]
            if isinstance(field, fields.List):
                field = field.container
                data = self.data[key]
            else:
                data = [self.data[key]]
            if isinstance(field, CustomField) and hasattr(field, 'validate'):
                for i in data:
                    if not field.validate(i):
                        return {
                            'responsecode' : 99,
                            'status' : 'failed',
                            'messages' : 'validation of \'{}\' field failed'.format(key)
                        }
        # for key in self.data:
        #     if not self.data[key]:
        #         return {
        #             'responsecode' : 99,
        #             'status' : 'failed',
        #             'messages' : 'empty validation of \'{}\' field failed'.format(key)
        #         }

    # def requestLog(self):
    #     return RequestLogModel().create(self.data)