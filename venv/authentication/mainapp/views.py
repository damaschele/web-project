from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request, 'registration/index.html', {'section':'index'})

@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html', {'section':'dashboard'})