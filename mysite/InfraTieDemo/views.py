from dataclasses import field
from django.shortcuts import render
from django.http import HttpResponse
from .models import Table1, Table2
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    model = Table1
    fields = ['InspectionID', 'PipeID', 'Length', 'Width', 'Rating']
    context = {}
    context["dataset"] = Table1.objects.all()
    return render(request, "table1_list_view.html", context)

def home(request):
    model = Table1
    fields = ['InspectionID', 'PipeID', 'Length', 'Width', 'Rating']
    context = {}
    context["dataset"] = Table1.objects.all()
    return render(request, "home.html", context)
    


def detail(request, InspectionID):
    model = Table2
    fields = ['ConditionID', 'InspectionID', 'Distance', 'Code']
    context = {}
    context["dataset"] = Table2.objects.filter(InspectionID=InspectionID)
    return render(request, "table2_list_view.html", context)


def login(request):
    return render(request, 'login.html')

# def login(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(request, username=username, password=password)
#    if user is not None:
#        login(request, user)
#        # Redirect to a success page.
#        index(request)
#        ...
#    else:
#        # Return an 'invalid login' error message.
#
#        ...
