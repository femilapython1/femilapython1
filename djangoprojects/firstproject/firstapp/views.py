from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Place

# Create your views here.
# def demo(request):
#     name="india"
#     return render(request,"demo.html",{'obj':name})
# def addition(request):
#     a=int(request.GET['num1'])
#     b=int(request.GET['num2'])
#     res=a+b
def demo(request):
    obj = Place.objects.all()
    return render(request,"index.html")
# def contact(request):
#     return HttpResponse("hello im femila")