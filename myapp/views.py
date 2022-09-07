from tkinter.tix import INTEGER
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
num = 0


def index(request):
    return render(request, 'index.html')

def testList(request):
    testVector = [1,2,3]
    return JsonResponse({'testVector': testVector})


def testPost(request):
    global num
    try:
        num = int(request.POST['input'])
    except:
        print("cannot convert into to string")
    print(num)
    return HttpResponse(status = 201)
