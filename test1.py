import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "motor/1", {"action1": "Right", "action2": "Left", "action3": "Forward", "action4": "Backward", "action5": "Stop"})
print(response.json())
input()
response = requests.get(BASE + "motor/1")
print(response.json())