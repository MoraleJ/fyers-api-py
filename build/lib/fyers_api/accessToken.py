from .fyersService import FyersService
import json
from .config import Config

class SessionModel:

	def __init__(self,id,key):
		self.appId = id 
		self.secretKey = key 

	def auth(self):
		data = {"app_id":self.appId, "secret_key":self.secretKey}
		token = ''
		service = FyersService()
		response = service.postCall(Config.auth,token,data)
		return response

	def set_token(self,token):
		self.auth_token = token
		return True

	def generate_token(self,user_id=None):
		if user_id is None:
			api = Config.Api+Config.genrateToken+'?authorization_code='+self.auth_token+'&appId='+self.appId
		else:
			api = Config.Api+Config.genrateToken+'?authorization_code='+self.auth_token+'&appId='+self.appId+'&user_id='+user_id
		return api
