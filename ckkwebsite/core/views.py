from django.shortcuts import render
from core import facade


def homepage(request):
    return render(request, "index.html", context=facade.get_all_models())
