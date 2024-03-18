from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Feedback(models.Model):
    ease_of_use = models.CharField(max_length=20, choices=[
        ('very_easy', 'Very easy'),
        ('easy', 'Easy'),
        ('neutral', 'Neutral'),
        ('difficult', 'Difficult'),
        ('very_difficult', 'Very difficult')
    ])
    interface_satisfaction = models.IntegerField()
    features_used = models.JSONField()  # Stores selected features as a list
    experience_issues = models.BooleanField()
    issue_description = models.TextField(blank=True, null=True)
    performance_rating = models.CharField(max_length=20, choices=[
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('average', 'Average'),
        ('poor', 'Poor'),
        ('terrible', 'Terrible')
    ])
    recommendation_likelihood = models.IntegerField()
    additional_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Feedback {self.id}"


class Interaction(models.Model):
    type = models.CharField(max_length=50)
    details = models.JSONField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.type} - {self.timestamp}"
