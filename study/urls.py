from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Login view
    path('home/', views.home_view, name='home'),  # Home view
    path('form/feedback_thank_you/', views.feedback_thank_you_view, name='feedback_thank_you'),  # Feedback thank you view
    path('calculator/', views.calculator_view, name='calculator'),  # Calculator view
    path('michael_jordan/', views.michael_jordan_view, name='michael_jordan'),  # Michael Jordan view
]
