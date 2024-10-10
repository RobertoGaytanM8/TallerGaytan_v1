from django.shortcuts import render

# Create your views here.

def VerLista(request):
    return render(request,'index.html')
