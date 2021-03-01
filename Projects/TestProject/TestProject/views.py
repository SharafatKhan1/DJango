from django.http import HttpResponse
from . import views
from django.shortcuts import render

def home(request):
    print("Hello Django")
    
    return render(request, 'Home.html')

def result(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    fullName = fname+' '+lname


    return render(request, "Index.html", {'fullName': fullName})


def calculator(request):
    val1 = request.GET.get('num1')
    val2 = request.GET.get('num2')
    operator = request.GET.get('operator')

    answer = None
    # if(len(val1) == 0 | len(val2) == 0):
    #     answer = "Please Enter Number(s)"
    # else:
    if operator == "+":
        answer = int(val1) + int(val2)
    elif operator == "-":
        answer = int(val1) - int(val2)
    elif operator == "*":
        answer = int(val1) * int(val2)
    elif operator == "/":
        answer = int(val1) / int(val2)
    else:
        answer = ""

    res = {'answer': answer}
    return render(request, 'Calculator.html', res)