from django.shortcuts import render
from core import facade


# Create your views here.
def homepage(request):
    return render(request, "index.html", context=facade.get_all_models())
