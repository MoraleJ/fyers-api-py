import json

class FyersFormation:

    def __init__(self):
        pass

    def headerFormation(self,header,content):
        ret = {"Authorization":header, 'Content-Type': content}
        return ret   

    def exceptionRaised(self,e):
        response = {"code":"500","data":e}
        return response    

    def responseFormation(self,statusCode,data):
        try:
            data = json.loads(data)
        except Exception as e:
            data = data
        if statusCode != 200:
            message = ''
            if 'message' in data:
                message = data['message']
            if 'errmsg' in data:
                message = data['errmsg']
            ret = {"code": statusCode, "data" : [],"message":message}
        else:
            message = ""
            if 'message' in data:
                message = data.pop('message',None)
            if 's' in data:
                data.pop('s',None)
            ret = {"code": statusCode, "data" : data,"message":message}
        return ret        