from django.shortcuts import render
from .models import Table1, Table2

# Create your views here.

# Home View
def home(request):
    model = Table1 # Use Table1 for model
    fields = ['InspectionID', 'PipeID', 'Length', 'Width', 'Rating'] # Use these fields from model
    context = {} # Init context
    context["dataset"] = Table1.objects.all() # Fill context dict with all objects in Table1
    return render(request, "home.html", context) # Render with request, source, and context dict
    
# Detail View
def detail(request, InspectionID):
    model = Table2 # Use Table2 for model
    fields = ['ConditionID', 'InspectionID', 'Distance', 'Code'] # Use these fields from model
    context = {} # Init context
    context["dataset"] = Table2.objects.filter(InspectionID=InspectionID) # Fill context dict with all objects in Table2
    context["InspectionID"] = InspectionID # Get InspectionID
    return render(request, "table2_list_view.html", context) # Render with request, source, and context dict

# Login View
def login(request):
    return render(request, 'login.html') # Render with request and source
