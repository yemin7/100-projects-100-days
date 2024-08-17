import requests

class Nutritionix:
    def __init__(self, app_id, app_key):
        self.url = "https://trackapi.nutritionix.com"
        self.exercise_endpoint = "v2/natural/exercise"
        self.app_id = app_id
        self.app_key = app_key

    def post_exercise(self, prompt, gender, weight, height, age):
        headers = {
            'Content-Type': 'application/json',
            'x-app-id': self.app_id,
            'x-app-key': self.app_key
        }
        body = {
            "query": prompt,
            "gender": gender,
            "weight_kg": weight,
            "height_cm": height,
            "age": age
        }
        return requests.post(url=f"{self.url}/{self.exercise_endpoint}", json=body, headers=headers)
