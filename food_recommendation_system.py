class FoodRecommendationSystem:
    def __init__(self):
        self.recommended_foods = []

    def recommend_food(self, health_conditions):
        self.recommended_foods = []

        # Rule-based recommendations based on health conditions
        if "cardiac" in health_conditions:
            self.recommended_foods.extend(self.limit_saturated_and_trans_fats())
            self.recommended_foods.extend(self.emphasize_whole_grains())
            self.recommended_foods.extend(self.encourage_fruits_and_vegetables())
            self.recommended_foods.extend(self.control_sodium_intake())
            self.recommended_foods.extend(self.monitor_cholesterol())
            self.recommended_foods.extend(self.control_portion_sizes())

        return self.recommended_foods

    def limit_saturated_and_trans_fats(self):
        return ["Avocados", "Nuts", "Seeds", "Olive oil", "Fatty fish", "Lean proteins"]

    def emphasize_whole_grains(self):
        return ["Whole grains (brown rice, quinoa, oats, whole wheat)", "High-fiber foods"]

    def encourage_fruits_and_vegetables(self):
        return ["Colorful fruits and vegetables", "At least 5 servings a day"]

    def control_sodium_intake(self):
        return ["Fresh fruits and vegetables", "Herbs and spices", "Low-sodium or no added salt foods"]

    def monitor_cholesterol(self):
        return ["Foods rich in soluble fiber", "Omega-3 rich foods"]

    def control_portion_sizes(self):
        return ["Moderate portions", "Maintain a healthy weight"]

# Example of using the recommendation system
if __name__ == "__main__":
    health_conditions = ["cardiac"]
    
    recommendation_system = FoodRecommendationSystem()
    recommended_foods = recommendation_system.recommend_food(health_conditions)

    print("Recommended Foods for Cardiac Health:")
    for food in recommended_foods:
        print("- " + food)
