from django.shortcuts import render

def home(request):
    if request.method == 'GET':
        template = 'home.html'
        context = {
            "request": request
        }

        return render(request, template, context)