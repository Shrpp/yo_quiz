import requests

parameters = {
    "amount": 20,
    "category": 15,
    "difficulty": "medium",
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]