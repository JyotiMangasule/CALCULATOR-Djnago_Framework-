from django.shortcuts import render
from app.models import Calculator
# from django.http import JsonResponse
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def webHome(request):
    return render(request, 'web/index.html')


# def getCalcutaion(request):
#     if request.POST['action'] == "add":
#        Calculator.objects.create(
#             c_first=request.POST['first'],
#             c_second=request.POST['second'],
#             c_operator=request.POST['oper'],
#             c_result=request.POST['result']
#             # in_image = request.FILES['InputUploadFile']
#         )
#         return HttpResponse();


def getCalcutaion(request):
    if request.POST['action'] == "add":
        Calculator.objects.create(
            c_first=request.POST['first'],
            c_second=request.POST['second'],
            c_operator=request.POST['oper'],
            c_result=request.POST['result']
        )
        return HttpResponse(); 