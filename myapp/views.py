from tkinter.tix import INTEGER
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import Algorithms
import random

from Algorithms.unsortedData import unsortedData

# Create your views here.

#variable instantiation

def index(request):
    return render(request, 'index.html')

def getDataSize(request):
    try:
        global dataSize
        dataSize = int(request.POST['input'])
        unsortedList = random.sample(range(dataSize), dataSize)
        print(unsortedList)
        
    except:
        print("cannot convert into to int")
    return HttpResponse(status = 201)

def testBubbleSort(request):
    try:
        print("testbubbleSort worked")
    except:
        print("ERROR")
    return HttpResponse(status = 201)