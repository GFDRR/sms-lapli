from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def nbUser(request):
    nb_user = User.objects.count()
    return render(request, 'admin/index.html', {'date': datetime.now()})