from django.shortcuts import render
from .models import Proprety

def index(request):
    propretys = Proprety.objects.all()
    user = request.user
    return render(request, "index.html", locals())

def login(request):
    return render(request, 'login.html', locals())
# Create your views here.
