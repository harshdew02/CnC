
# import imp
from os import remove
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    remline = request.POST.get('newlinerem', 'off')

    if (removepunc == "on"):
     punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
     analyzed = ""
     for char in djtext:
        if char not in punctuations:
            analyzed += char

     params = {'purpose': 'Remove Puntuations', 'analyzed_text': analyzed}
     djtext = analyzed

    if (fullcaps == "on"):
     analyzed = ""
     for char in djtext:
        analyzed += char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
     djtext = analyzed

    if (remline == 'on'):
     analyzed = ""
     for char in djtext:
        if char !="\n" and char != "\r":
            analyzed += char.upper()

        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
     return render(request, 'analyze.html', params)

    else:
     return HttpResponse('Error')

