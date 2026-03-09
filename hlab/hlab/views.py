from django.http import HttpResponse


def handler404(request, exception):
    return HttpResponse("PAGE NOT FOUND")