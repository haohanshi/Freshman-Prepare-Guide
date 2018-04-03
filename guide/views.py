from django.shortcuts import render
from django.conf.urls import url

# Create your views here.
def redirect(request):
    return redirect('/guide')

def main(request):
    return render(request, 'guide/index.html')

def preface(request):
    return render(request, 'guide/preface.html')

def faq(request):
    return render(request, 'guide/faqs.html')