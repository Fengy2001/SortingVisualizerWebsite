from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def testList(request):
    testVector = [1,2,3]
    return JsonResponse({'testVector': testVector})