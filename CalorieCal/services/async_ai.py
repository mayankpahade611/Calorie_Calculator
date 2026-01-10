import threading
from .ai_recommendation import get_meal_recommendation
from CalorieCal.models import DietPlan

def generate_ai_async(diet_plan_id, calories, goal):

    def task():
        try:
            text = get_meal_recommendation(
                calories=calories,
                goal=goal,
                meal_type="full day"
            )

            plan = DietPlan.objects.get(id=diet_plan_id)
            plan.ai_suggestion = text
            plan.save()

        except Exception as e:
            print("Error:", e)

    thread = threading.Thread(target=task)
    thread.start()