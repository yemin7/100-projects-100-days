import requests
from quiz_brain import QuizBrain
from ui import QuizInterface

parameters = {
    "amount": 10,
    "category": 9,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

data = response.json()['results']


quiz_brain = QuizBrain(data)
quiz_ui = QuizInterface(quiz_brain)
