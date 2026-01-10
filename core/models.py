

# Create your models here.
from django.conf import settings
from django.db import models

class LocationCity(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    is_coastal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.state}"

class HouseholdProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.ForeignKey(LocationCity, on_delete=models.SET_NULL, null=True, blank=True)
    members_count = models.PositiveIntegerField(default=1)
    income_bracket = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('mid', 'Middle'),
        ('high', 'High'),
    ])
    diet_type = models.CharField(max_length=20, choices=[
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non Vegetarian'),
        ('fish', 'Fish-heavy'),
    ], default='nonveg')

    def __str__(self):
        return f"{self.user.username} household"

class ActivityType(models.Model):
    category = models.CharField(max_length=20, choices=[
        ('plastic', 'Plastic'),
        ('fashion', 'Fashion'),
        ('transport', 'Transport'),
    ])
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category} - {self.name}"

class HouseholdActivityLog(models.Model):
    household = models.ForeignKey(HouseholdProfile, on_delete=models.CASCADE)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    value = models.FloatField()
    period_start = models.DateField()
    period_end = models.DateField()

    def __str__(self):
        return f"{self.household} - {self.activity_type} - {self.value}"
class SustainabilityScore(models.Model):
    household = models.ForeignKey(HouseholdProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    plastic_score = models.FloatField(default=50)
    fashion_score = models.FloatField(default=50)
    transport_score = models.FloatField(default=50)
    overall_score = models.FloatField(default=50)
