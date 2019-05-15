from .config import Config
import requests
import json
import urllib
from .fyersFormation import FyersFormation
from tornado import httpclient


formService = FyersFormation()

data_apis = ['/searchSymbols', '/getHistoricalOHLCV', '/level2data', '/getQuotes', '/getQuickQuote', '/symbolsinfo']

class FyersService:

    def __init__(self):
        self.content = 'application/json'    

    def postCall(self,api,header,data = None):
        try:
            response = requests.post(Config.Api+api,headers={"Authorization":header, 'Content-Type': self.content}, json = data)
            response = formService.responseFormation(response.status_code,response.json())
        except Exception as e:
            response = formService.exceptionRaised(e)
        return response   
    
    def getCall(self,api,header,data = None):
        try:
            if data is not None:
                #args = ['{}={}'.format(k, v) for k,v in data.items()]
                #args_in_one_string = "&".join(args)
                try:
                    url_params = urllib.urlencode(data)
                except Exception as e:
                    url_params = urllib.parse.urlencode(data)
                if api in data_apis:
                    url = Config.DataApi+api+ "?" + url_params
                else:
                    url = Config.Api+api+ "?" + url_params
                response = requests.get(url = url,headers={"Authorization":header, 'Content-Type': self.content})
            else:
                if api in data_apis:
                    URL =  Config.DataApi+api
                else:
                    URL = Config.Api+api
                response = requests.get(url = URL,headers={"Authorization":header, 'Content-Type': self.content}, params = data)
            response = formService.responseFormation(response.status_code,response.json())
        except Exception as e:
            response = formService.exceptionRaised(e)
        return response

    def deleteCall(self,api, header, data):
        try:
            response =  requests.delete(url = Config.Api+api, headers={"Authorization":header, 'Content-Type': self.content}, json = data)
            response = formService.responseFormation(response.status_code,response.json())
        except Exception as e:
            response = formService.exceptionRaised(e)
        return response

    def putCall(self,api,header,data):
        try:
            response = requests.put(url = Config.Api+api, headers={"Authorization":header, 'Content-Type': self.content}, json = data)
            response = formService.responseFormation(response.status_code,response.json())
        except Exception as e:
            response = formService.exceptionRaised(e)       
        return response

class FyersAsyncService:

    def __init__(self):
        self.content = 'application/json'    

    def postCall(self,api,header,data = None):
        try:
            reqClient = httpclient.AsyncHTTPClient()
            request = httpclient.HTTPRequest(Config.Api+api, method="POST", body=json.dumps(data), headers={"Authorization":header, 'Content-Type': self.content})
            response = reqClient.fetch(request,raise_error=False)
        except Exception as e:
            response = formService.exceptionRaised(e)
        return response   
    
    def getCall(self,api,header,data = None):
        try:
            reqClient = httpclient.AsyncHTTPClient()
            if data is not None:
                try:
                    url_params = urllib.urlencode(data)
                except Exception as e:
                    url_params = urllib.parse.urlencode(data)
                if api in data_apis:
                    url = Config.DataApi+api+ "?" + url_params
                else:
                    url = Config.Api+api+ "?" + url_params
                request = httpclient.HTTPRequest(url, method="GET", headers={"Authorization":header, 'Content-Type': self.content})
            else:
                if api in data_apis:
                    URL =  Config.DataApi+api
                else:
                    URL = Config.Api+api
                request = httpclient.HTTPRequest(URL, method="GET", headers={"Authorization":header, 'Content-Type': self.content})

            response = reqClient.fetch(request,raise_error=False)
        except Exception as e:
            response = formService.exceptionRaised(e)
        return response

    def deleteCall(self,api, header, data):
        try:
            reqClient = httpclient.AsyncHTTPClient()
            request = httpclient.HTTPRequest(Config.Api+api, method="DELETE", body=json.dumps(data), headers={"Authorization":header, 'Content-Type': self.content},allow_nonstandard_methods=True)
            response = reqClient.fetch(request,raise_error=False)
        except Exception as e:
            response = formService.exceptionRaised(e)
        return response

    def putCall(self,api,header,data):
        try:
            reqClient = httpclient.AsyncHTTPClient()
            request = httpclient.HTTPRequest(Config.Api+api, method="PUT", body=json.dumps(data), headers={"Authorization":header, 'Content-Type': self.content})
            response = reqClient.fetch(request,raise_error=False)
        except Exception as e:
            response = formService.exceptionRaised(e)       
        return response