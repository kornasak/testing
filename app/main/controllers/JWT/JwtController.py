import json, jwt, app.helper.CustomField as fields
from flask import request
from flask_restplus import Namespace, Resource
from app.helper.ErrException import ErrException
from app.helper.RequestParamHandler import RequestParamHandler


api = Namespace('jwt', description='Testing jwt library')

ENCODE_DATA = api.model('ENCODE_DATA', {
    'test' : fields.String(required=True)
})

DECODE_DATA = api.model('DECODE_DATA', {
    'token' : fields.String(required=True)
})

@api.route('/encode')
class EncodeData(Resource):
    @api.expect(ENCODE_DATA)
    def post(self):
        data = request.json
        functionName = RequestParamHandler().getRoute()
        ipAddress = RequestParamHandler().getIpaddress()
        userAgent = RequestParamHandler().getUserAgent()
        validatePayload = RequestParamHandler(data=data).validatePayload(ENCODE_DATA)
        if (validatePayload):
            params = {
                'route' : functionName,
                'params' : json.dumps(data),
                'response' : json.dumps(validatePayload),
                'request_ip' : ipAddress,
                'user_agent' : userAgent
            }
            # RequestParamHandler(
            #     data=params
            # ).requestLog()
            return validatePayload
        try:
            encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
            # print(encoded_jwt)
            result = {
                'responsecode' : 0,
                'status' : 'success',
                'token' : encoded_jwt
            }
        except ErrException as error:
            result = {
                'responsecode' : int(error.code),
                'status' : 'failed',
                'messages' : error.msg
            }
        # finally:
        #     params = {
        #         'route' : functionName,
        #         'params' : json.dumps(data),
        #         'response' : json.dumps(result),
        #         'request_ip' : ipAddress,
        #         'user_agent' : userAgent
        #     }
        #     RequestParamHandler(
        #         data=params
        #     ).requestLog()
        return result
        #     result = GBPPaymentService().generate(
        #         data['amount'],
        #         data['transactionid'],
        #         data['callbackurl']
        #     )
        # except ErrException as error:
        #     result = {
        #         'responsecode' : int(error.code),
        #         'status' : 'failed',
        #         'messages' : error.msg
        #     }
        # finally:
        #     params = {
        #         'route' : functionName,
        #         'params' : json.dumps(data),
        #         'response' : json.dumps(result),
        #         'request_ip' : ipAddress,
        #         'user_agent' : userAgent
        #     }
        #     RequestParamHandler(
        #         data=params
        #     ).requestLog()
        # return result