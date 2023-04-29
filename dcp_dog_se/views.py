from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def quiz_dog_3(request):
    return render(request, 'quiz_dog_3.html')

def quiz_dog_4(request):
    return render(request, 'quiz_dog_4.html')

def quiz_dog_5(request):
    return render(request, 'quiz_dog_5.html')

def test_result_dog(request):
    return render(request, 'test_result_dog.html')
