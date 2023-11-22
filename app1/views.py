from django.shortcuts import render

# Create your views here.
def specific(request):
    return render(request,'specific.html')
def specific2(request):
    return render(request,'specific2.html')
