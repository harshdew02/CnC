from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'main/index.html')

def blogpost(request):
    return render(request , 'main/blogpost.html')

def contact(request):
    return render(request , 'main/contact.html') 