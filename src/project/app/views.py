from django.shortcuts import render

# Create your views here.


from django.shortcuts import render


def index(request):
    context = {"key": "value"}
    return render(request, "index.html", context)
