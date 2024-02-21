from django.shortcuts import render
from django.http import HttpResponse

def taskList(request):
    ctx = {
        "name": "TASKS FOR THE DAY",
        "lists": [
            {
                'name': 'CSCI 40',
                'list': [
                    'Create Python Environment',
                    'Install Django and Dotenv',
                    'Create Django Project',
                    'Configuro Django Project',
                    'Create App under project'
                ]
            }
        ],
        "image path": "taskApp/tasks/images/download.jpeg"
    }

    return render(request, "tasks.html", ctx)
