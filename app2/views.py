from django.shortcuts import render

# Create your views here.
def generic(request):
    return render(request,'generic.html')
def generic2(request):
    return render(request,'generic2.html')
