from django.shortcuts import render

def index(request):
    data = dict()
    data.update({'title': 'HomePage CRM'})
    return render(request, "home.html", data)