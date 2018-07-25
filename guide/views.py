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

def vpn(request):
    return render(request, 'guide/vpn.html')

def checklist_1(request):
    return render(request, 'guide/checklist_1.html')

def checklist_2(request):
    return render(request, 'guide/checklist_2.html')

def at_school_1(request):
    return render(request, 'guide/at_school_1.html')