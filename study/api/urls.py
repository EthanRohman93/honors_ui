from django.urls import path
from .views import log_interaction, submit_form, api_login_or_register


urlpatterns = [
    path('log-interactions/', log_interaction, name='log_interactions'),
    path('submit-form/', submit_form, name='submit_form'),
    path('login/', api_login_or_register, name='api_login_or_register'),
]
