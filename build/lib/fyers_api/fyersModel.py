from .fyersService import FyersService
from .fyersService import FyersAsyncService
import json
from .config import Config

#service = FyersService()

class FyersModel:
	def __init__(self,is_async=False):
		if is_async is False:
			self.service = FyersService()
		else:
			self.service = FyersAsyncService()

	def tradebook(self,token):
		response = self.service.getCall(Config.tradebook,token)		
		return response

	def positions(self,token):
		response = self.service.getCall(Config.positions,token)
		return response

	def holdings(self,token):
		response = self.service.getCall(Config.holdings,token)
		return response

	def convert_position(self,token,data):
		response = self.service.postCall(Config.convertPosition,token,data)
		return response

	def funds(self,token):
		response = self.service.getCall(Config.funds,token)
		return response

	def orders(self,token):
		response = self.service.getCall(Config.orders,token)
		return response		

	def delete_orders(self,token,data):
		response = self.service.deleteCall(Config.orders,token,data)
		return response		

	def place_orders(self,token,data):
		response = self.service.postCall(Config.orders,token,data)
		return response

	def update_orders(self,token,data):
		response = self.service.putCall(Config.orders,token,data)
		return response

	def order_id(self,token,data):
		response = self.service.getCall(Config.orderId,token,data)
		return response	

	def minquantity(self,token):
		response = self.service.getCall(Config.minquantity,token)
		return response

	def order_status(self,token,data):
		response = self.service.getCall(Config.orderStatus,token,data)
		return response

	def market_status(self,token):
		response = self.service.getCall(Config.marketStatus,token)
		return response	


	def level2data(self,token,data):
		response = self.service.getCall(Config.level2data,token,data)
		return response 

	def symbolsinfo(self,token,data):
		response = self.service.getCall(Config.symbolsinfo,token,data)
		return response

	def get_quotes(self,token,data):
		response = self.service.getCall(Config.getQuotes,token,data)
		return response        

	def get_quickquote(self,token,data):
		response = self.service.getCall(Config.getQuickQuote,token,data)
		return response    

	def get_historical_OHLCV(self,token,data):
		response = self.service.getCall(Config.getHistoricalOHLCV,token,data)
		return response

	def search_symbols(self,token,data):
		response = self.service.getCall(Config.searchSymbols,token,data)
		return response