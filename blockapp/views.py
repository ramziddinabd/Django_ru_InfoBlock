from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    posts = Article.objects.all()
    return render(request, 'blockapp/home.html', {'posts':posts})
