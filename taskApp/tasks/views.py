from django.shortcuts import render
from django.http import HttpResponse

def taskList(request):
    ctx = {
        "Hello WOrld"
        }

    return render(request, "recipeList.html", ctx)
