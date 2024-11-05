class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        print("init() is executed only once..!!")
        self.get_response = get_response
    def __call__(self, request):
        print('This line added at pre-processing of request')
        response = self.get_response(request)
        print('This line added at post-processing of request')
        return response


from django.http import HttpResponse


class AppMaintananceMiddleware(object):
    def __init__(self, get_response):
        print("init() method is called...");
        self.get_response = get_response
    def __call__(self, request):
        return HttpResponse('<h1>Currently Application under maintenance...Plz try after 8am..!!</h1><hr />')


from django.http import HttpResponse


class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        print("init() is called for error-app");
        self.get_response = get_response
    def __call__(self, request):
        return self.get_response(request)
    def process_exception(self, request, exception):
        print("Server is printing exception")
        return HttpResponse(
            '<h1> Currently we are facing some technical problems..(Exception) Plz try after some time !!!</h1><hr />')

