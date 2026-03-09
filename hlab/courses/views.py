from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from datetime import datetime
# Create your views here.
def courses(request):
    return HttpResponse("Courses")

def show_current_date(request):
    current_date = datetime.today()
    
    return HttpResponse(current_date, request)

def get_path(request):
    path = request.path
    return HttpResponse(path)

def get_http_params(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META.get("REMOTE_ADDR", "unknown")
    user_agent = request.META.get("HTTP_USER_AGENT", "unknown")
    path_info = request.path_info

    message = (
            f"path: {path}\n"
            f"scheme: {scheme}\n"
            f"method: {method}\n"
            f"address: {address}\n"
            f"user_agent: {user_agent}\n"
            f"path_info: {path_info}"
        )
    return HttpResponse(message,content_type="text/plain")

def get_course(request, name):
    courses = {
        "python":"Cool course, covers everything",
        "ml":"All about machine learning",
        "dl":"All about deep learning"
    }
    info = courses[name]
    message = f"<h1>{name}: </h1><br> <h2>{info}</h2>"
    return HttpResponse(message)

# Adding class based views to avoid adding so much functions
class CourseListViews(View):
    def get(self, request):
        return HttpResponse("All courses")
    
    def post(self, request):
        return HttpResponse("Form submitted")
