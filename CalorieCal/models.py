from django.db import models

# Create your models here.
class Userprofile(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
    ]

    ACTIVITY_CHOICES = [
        ("sedentary", "Sedentary"),
        ("light", "Lightly Active"),
        ("moderate", "Moderately Active"),
        ("active", "Very Active"),
    ]

    GOAL_CHOICES = [
        ("loss", "Weight Loss"),
        ("maintain", "Maintain Weight"),
        ("gain", "Weight Gain"),
    ]

    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    height_cm = models.FloatField(help_text="Height in centimeters")
    weight_kg = models.FloatField(help_text="Weight in kilograms")
    activity_level = models.CharField(max_length=10, choices=ACTIVITY_CHOICES)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile {self.id} ({self.goal})"
    


class CalorieResult(models.Model):
    GOAL_CHOICES = [
        ("loss", "Weight Loss"),
        ("maintain", "Maintain Weight"),
        ("gain", "Weight Gain"),
    ]

    user_profile = models.ForeignKey(
        Userprofile,
        on_delete=models.CASCADE,
        related_name="results"
    )
    bmr = models.FloatField()
    maintenance_calories = models.FloatField()
    target_calories = models.FloatField()
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for Profile {self.user_profile.id}"
    

class DietPlan(models.Model):
    calorie_result = models.OneToOneField(
        CalorieResult,
        on_delete=models.CASCADE,
        related_name="diet_plan"
    )

    breakfast_calories = models.IntegerField()
    lunch_calories = models.IntegerField()
    dinner_calories = models.IntegerField()
    snacks_calories = models.IntegerField()
    guidelines = models.TextField()


    def __str__(self):
        return f"Diet Plan for Result {self.calorie_result.id}"