from nutritionix import Nutritionix
from sheety_sheet import SheetySheet

APP_ID = ""
API_KEY = ""

GENDER = "male"
WEIGHT_KG = 0  # Number
HEIGHT_CM = 0  # Number
AGE = 0  # Number

sheety = SheetySheet()

user_input = input("Tell me which exercise you did: ")

nutritionix_v2 = Nutritionix(APP_ID, API_KEY)
post_nutritionix = nutritionix_v2.post_exercise(user_input, GENDER, WEIGHT_KG, HEIGHT_CM, AGE)
print(post_nutritionix.text)
json_data = post_nutritionix.json()['exercises']
for item in json_data:
    exercise = item['name']
    duration = item['duration_min']
    calories = item['nf_calories']
    response = sheety.post_workout(exercise, duration, calories)
    print(response.text)
