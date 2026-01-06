def generate_diet_plan(target_calories, goal):
    meal_distribuiton = {
        "breakfast": 0.25,
        "lunch": 0.35,
        "dinner": 0.30,
        "snacks": 0.10,
    }

    plan = {
        "breakfast": int(target_calories * meal_distribuiton["breakfast"]),
        "lunch": int(target_calories * meal_distribuiton["lunch"]),
        "dinner": int(target_calories * meal_distribuiton["dinner"]),
        "snacks": int(target_calories * meal_distribuiton["snacks"]),
    }

    guidelines = {
        "loss": [
            "Maintain a small calorie deficit",
            "Increase protein intake",
            "Stay physically active",
            "Avoid crash dieting",
        ],
        "gain": [
            "Eat calorie-dense nutritious food",
            "Focus on strength training",
            "Track weekly progress",
            "Ensure proper sleep and recovery",
        ],
        "maintain": [
            "Maintain balanced meals",
            "Stay consistent with activity",
            "Avoid frequent junk food",
            "Focus on lifestyle balance",
        ],
    }

    return plan, guidelines.get(goal, [])
