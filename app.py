from flask import Flask, render_template, request
from food_recommendation_system import FoodRecommendationSystem

app = Flask(__name__)
recommendation_system = FoodRecommendationSystem()

def calculate_bmi(weight, height):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return round(bmi, 2)

def calculate_bmr(age, weight, height, gender):
    if gender.lower() == 'male':
        bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.75 * age)
    elif gender.lower() == 'female':
        bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
    else:
        raise ValueError("Invalid gender")
    return round(bmr, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = int(request.form['age'])
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        activity_level = request.form['activity_level']
        gender = request.form['gender']

        bmi = calculate_bmi(weight, height)
        bmr = calculate_bmr(age, weight, height, gender)

        health_conditions = ["cardiac"]
        calorie_intake = request.form.get('calorie_intake')

        recommended_foods = recommendation_system.recommend_food(health_conditions, bmi, bmr, calorie_intake)

        return render_template('index.html', recommended_foods=recommended_foods, bmi=bmi, bmr=bmr)

    return render_template('index.html', recommended_foods=None, bmi=None, bmr=None)

if __name__ == '__main__':
    app.run(debug=True)
