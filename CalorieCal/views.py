from django.shortcuts import render, redirect

from .forms import UserProfileForm
from .models import CalorieResult, DietPlan
from .services.calorie import (
    calculate_bmr,
    calculate_maintenance_calories,
    calculate_target_calories,
)
from .services.planner import generate_diet_plan

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


@login_required
def calorie_input_view(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            bmr = calculate_bmr(
                profile.age,
                profile.gender,
                profile.height_cm,
                profile.weight_kg,
            )

            maintenance = calculate_maintenance_calories(
                bmr,
                profile.activity_level,
            )

            target = calculate_target_calories(
                maintenance,
                profile.goal,
            )

            result = CalorieResult.objects.create(
                user_profile=profile,
                bmr=round(bmr, 2),
                maintenance_calories=round(maintenance, 2),
                target_calories=round(target, 2),
                goal=profile.goal,
            )

            # Diet Plan
            plan, guidelines = generate_diet_plan(target, profile.goal)

            diet_plan = DietPlan.objects.create(
                calorie_result=result,
                breakfast_calories=plan["breakfast"],
                lunch_calories=plan["lunch"],
                dinner_calories=plan["dinner"],
                snacks_calories=plan["snacks"],
                guidelines="\n".join(guidelines),
            )

            return redirect("result", result_id=result.id)

    else:
        form = UserProfileForm()

    return render(request, "CalorieCal/input.html", {"form": form})


def result_view(request, result_id):
    result = CalorieResult.objects.select_related("user_profile").get(id=result_id)

    plan = result.diet_plan

    guidelines = plan.guidelines.split("\n")

    context = {
        "result": result,
        "plan": plan,
        "guidelines": guidelines,
    }

    return render(request, "CalorieCal/result.html", context)




def signup_view(request):

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("input")   

    else:
        form = SignupForm()

    return render(request, "CalorieCal/signup.html", {"form": form})


def history_view(request):

    results = (
        CalorieResult.objects
        .filter(user_profile__user=request.user)    
        .select_related("user_profile")
        .order_by("-created_at")
    )

    return render(request, "CalorieCal/history.html", {"results": results})