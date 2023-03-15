from django.shortcuts import render

# Create your views here.
def hardik(request):
    return render(request,'operations.html',context={'name':'Banglore','loc':'marthalli'})


def rohit(request):
    return render(request,'operations1.html',context={'a':10,'b':80,'c':3,'d':3})