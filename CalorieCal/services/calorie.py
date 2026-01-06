def calculate_bmr(age, gender, weight_kgm, height_cm):
    if gender == "male":
        return 10 * weight_kgm + 6.25 * height_cm - 5 * age + 5
    else:
        return 10 * weight_kgm + 6.25 * height_cm - 5 * age - 161


def get_activity_multiplier(activity_level):
    multipliers = {
        "sedentary": 1.2,
        "lightly": 1.375,
        "moderately": 1.55,
        "active": 1.725,
    }
    return multipliers.get(activity_level, 1.2)  # Default to sedentary if not found


def calculate_maintenance_calories(bmr, activity_level):
    multiplier = get_activity_multiplier(activity_level)
    return bmr * multiplier


def calculate_target_calories(maintenance_calories, goal):
    if goal == "loss":
        return maintenance_calories - 400
    elif goal == "gain":
        return maintenance_calories + 400
    return maintenance_calories
