from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from ..models import Interaction, Feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.dateparse import parse_datetime
import json


@api_view(['POST'])
@permission_classes([AllowAny])  # Adjust permissions as appropriate
def log_interaction(request):
    try:
        data = request.data  # DRF automatically parses JSON data
        for interaction in data:
            timestamp = parse_datetime(interaction['timestamp'])
            Interaction.objects.create(
                type=interaction['type'],
                details=interaction['details'],
                timestamp=timestamp
            )
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)
    except KeyError as e:
        return Response({"error": f"Missing key: {e}"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def submit_form(request):
    try:
        feedback = Feedback(
            ease_of_use=request.data.get('easeOfUse'),
            interface_satisfaction=int(request.data.get('interfaceSatisfaction')),
            features_used=request.data.get('featuresUsed', []),  # Directly get the list without getlist
            experience_issues=request.data.get('experienceIssues', 'no') == 'yes',
            issue_description=request.data.get('issueDescription', ''),
            performance_rating=request.data.get('performanceRating'),
            recommendation_likelihood=int(request.data.get('recommendationLikelihood')),
            additional_comments=request.data.get('additionalComments', '')
        )
        feedback.save()
        return Response({"status": "success", "message": "Feedback submitted successfully."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": "Failed to submit feedback", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login_or_register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return Response({'status': 'success', 'message': 'Login successful.'}, status=status.HTTP_200_OK)
    else:
        # Try to create a new user if one does not exist
        if User.objects.filter(username=username).exists():
            return Response({'status': 'error', 'message': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Create new user
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)  # Log the new user in
            return Response({'status': 'success', 'message': 'User registered and logged in.'}, status=status.HTTP_201_CREATED)

