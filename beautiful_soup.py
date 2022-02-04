import requests

page = requests.get("https://247ctf.com/scoreboard")
print(page.text)
