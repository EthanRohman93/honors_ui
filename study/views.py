from django.shortcuts import render, redirect
from .models import Feedback, Interaction
from .utils import generate_goofy_name
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
import json


@csrf_exempt
@require_POST
def log_interaction(request):
    try:
        # Parse the JSON string from the request body
        data = json.loads(request.body)
        # Iterate through each interaction in the received data
        for interaction in data:
            # Parse the timestamp string to a datetime object
            timestamp = parse_datetime(interaction['timestamp'])
            # Create and save the Interaction instance
            Interaction.objects.create(
                type=interaction['type'],
                details=interaction['details'],
                timestamp=timestamp
            )

        return JsonResponse({"status": "success"}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except KeyError as e:
        # Catch missing keys errors and return a bad request response
        return JsonResponse({"error": f"Missing key: {e}"}, status=400)


def login_view(request):
    suggested_name = generate_goofy_name()  # Generate a goofy name for new users
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Attempt to authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User exists and is authenticated, so log them in
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # No user exists with the provided credentials, attempt to create a new user
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                # Log in the newly created user
                login(request, user)
                return redirect('home')  # Redirect to the home page after account creation and login
            except Exception as e:
                # If user creation fails, return to the login page with an error message
                context = {
                    'error': 'Account creation failed. The username may already be taken.',
                    'suggested_name': suggested_name
                }
                return render(request, 'study/login.html', context)

    # If it's a GET request or if the login/authentication failed, show the login page again
    return render(request, 'study/login.html', {'suggested_name': suggested_name})


def home_view(request):
    # The home.html is directly under templates, so it stays the same.
    return render(request, 'study/home.html')


def calculator_view(request):
    # Update the path to include the 'study' directory.
    return render(request, 'study/calculator.html')


def feedback_thank_you_view(request):
    return render(request, 'study/feedback_thank_you.html')


def form_view(request):
    if request.method == 'POST':
        # Assuming 'featuresUsed' is sent as a list of checkbox values
        features_used = request.POST.getlist('featuresUsed')  # Directly compatible with JSONField
        experience_issues = request.POST.get('experienceIssues', 'no') == 'yes'  # Convert to boolean
        feedback = Feedback(
            ease_of_use=request.POST.get('easeOfUse'),
            interface_satisfaction=int(request.POST.get('interfaceSatisfaction')),
            features_used=features_used,  # Direct assignment, Django handles serialization
            experience_issues=experience_issues,
            issue_description=request.POST.get('issueDescription', ''),
            performance_rating=request.POST.get('performanceRating'),
            recommendation_likelihood=int(request.POST.get('recommendationLikelihood')),
            additional_comments=request.POST.get('additionalComments', '')
        )
        feedback.save()

        return redirect('feedback_thank_you')
    else:
        return render(request, 'study/form.html')


def michael_jordan_view(request):
    # Update the path to include the 'study' directory.
    return render(request, 'study/michael_jordan.html')
