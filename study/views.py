from django.shortcuts import render
from .utils import generate_goofy_name


def login_view(request):
    if request.method == 'POST':
        return render(request, 'study/login.html')  # Redirect to the login API usage in your Next.js frontend
    else:
        suggested_name = generate_goofy_name()
        return render(request, 'study/login.html', {'suggested_name': suggested_name})


def home_view(request):
    return render(request, 'study/home.html')


def calculator_view(request):
    return render(request, 'study/calculator.html')


def feedback_thank_you_view(request):
    return render(request, 'study/feedback_thank_you.html')


def michael_jordan_view(request):
    return render(request, 'study/michael_jordan.html')
