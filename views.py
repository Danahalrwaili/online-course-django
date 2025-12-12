from django.http import HttpResponse
def index(request):
    return HttpResponse("Courses Page")
def exam(request):
    return HttpResponse("Exam Page")
def result(request):
    return HttpResponse("Result Page: Score = 100%")
