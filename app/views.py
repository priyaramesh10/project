from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.models import User
from .models import Product
from django.http import JsonResponse
from django.db.models import Q


@csrf_exempt
def student_details(request):
    if request.method =='GET':
        try:
            students = Product.objects.all().values('product_name','title','brand','price')
            return JsonResponse({'students': list(students)},safe=False)
        except Exception as e:
            return JsonResponse({"error":"Ivaild Method!!"})
    else:
        return JsonResponse({"sucess":False,"response": "Method not allowed!!"})






