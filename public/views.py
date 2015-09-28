from django.shortcuts import render

# Create your views here.


def rpluie(request):
    return render(request, "public/temp_rapport.html", {})