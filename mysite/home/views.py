from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse("<h1>Polls questions: <a href='http://127.0.0.1:8000/polls/'>polls/<a></h1>")
