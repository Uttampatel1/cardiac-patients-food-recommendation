from flask import Flask, render_template, request
from food_recommendation_system import FoodRecommendationSystem  # Assuming you have the FoodRecommendationSystem class in a separate file

app = Flask(__name__)
recommendation_system = FoodRecommendationSystem()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        age = int(request.form['age'])
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        activity_level = request.form['activity_level']

        # Perform calculations or additional processing if needed

        # Example: Health conditions based on the input (for demonstration purposes)
        health_conditions = ["cardiac"]

        # Get food recommendations
        recommended_foods = recommendation_system.recommend_food(health_conditions)

        # Render the template with the recommendations
        return render_template('index.html', recommended_foods=recommended_foods)

    # Render the initial form
    return render_template('index.html', recommended_foods=None)

if __name__ == '__main__':
    app.run(debug=True)
