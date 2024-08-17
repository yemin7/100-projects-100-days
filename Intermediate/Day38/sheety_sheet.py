import requests
from datetime import datetime as dt


def get_date_time():
    today = dt.now()
    t_date = today.strftime("%d/%m/%Y")
    t_time = today.strftime("%H:%M:%S")
    return t_date, t_time


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["Authorization"] = "Bearer " + self.token
        return r


class SheetySheet:
    def __init__(self):
        self.url = ""  # Spreadsheet api
        self.token = ""  # Auth token

    def get_last_id(self):
        result = requests.get(self.url, auth=BearerAuth(self.token)).json()
        return result['workouts'][-1]['id']

    def post_workout(self, exercise, duration, calories):
        id = self.get_last_id() + 1
        t_date, t_time = get_date_time()

        body = {
            'workout': {
                "date": t_date,
                "time": t_time,
                "exercise": exercise.title(),
                "duration": duration,
                "calories": calories,
                "id": id
            }
        }
        return requests.post(url=self.url, json=body, auth=BearerAuth(self.token))
