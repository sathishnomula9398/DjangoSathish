from django.http import HttpResponse
#create your views here
def welcome_view(request):
	print('This line added by view function names welcome_view...!!!')
	return HttpResponse('<h1>Custom Middleware Demo</h1> <hr />')

def home_page_view(request):
	return HttpResponse('<h1> Hello This is from home page view </h1><hr />')

def home_page_view2(request):
	print(10/0)
	return HttpResponse('<h1>Hello This is from home page view</h1><hr />')



class FirstMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		print('This line printed by FirstMiddleware at pre-processing of request');
		response = self.get_response(request)
		print('This line printed by FirstMiddleware at post-processing of request')
		return response;


class SecondMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		print('This line printed by SecondMiddleware at pre-processing of request')
		response = self.get_response(request)
		print('This line printed by SecondMiddleware at post-processing of request')
		return response


def home_page_view3(request):
	print('This line printed by home_page_view3 function...')
	return HttpResponse('<h1>Hello this is from home page view3 </h1><hr />')

