from django.shortcuts import render

# Create your views here.
def secondpage(request):
    return render(request,'secondpage.html')