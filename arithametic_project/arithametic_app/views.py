from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name="india"
    return render(request,"index.html",{'obj':name})

def operations(request):
    x=int(request.GET['num1'])
    y =int(request.GET['num2'])
    res=x+y
    res1=x-y
    res2=x/y
    return render(request,"result.html",{'result':res,'result1':res1,'result2':res2})