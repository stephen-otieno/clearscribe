from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def contact_us(request):
    return render(request, 'contacts.html')

# Create your views here.
