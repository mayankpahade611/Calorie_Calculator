import ollama

def get_meal_recommendation(calories, goal, meal_type):


    prompt = f"""
You are a proffesional nutrition assistant.

User goal: {goal}
Meal: {meal_type}
Target calories: {calories} kcal

Suggest foods and portions briefly.
"""
    

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response["message"]["content"]
