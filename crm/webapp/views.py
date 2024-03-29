from django.shortcuts import render


# - Homepage
def home(request):
    return render(request, "webapp/index.html")
