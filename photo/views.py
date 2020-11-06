from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'photo/index.html')


def wedding(request):
    return render(request, 'photo/wedding.html')


def birthday(request):
    return render(request, 'photo/birthday.html')

def preWedding(request):
    return render(request, 'photo/prewedding.html')
