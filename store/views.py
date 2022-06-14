from django.shortcuts import render
from django.http import JsonResponse



def index(request):
    return render(request, 'store/index.html')



def about(request):
    return render(request, 'store/about.html')



def contact(request):
    return render(request, 'store/contact.html')



def services(request):
    return render(request, 'store/services.html')



def testimonial(request):
    return render(request, 'store/testimonial.html')