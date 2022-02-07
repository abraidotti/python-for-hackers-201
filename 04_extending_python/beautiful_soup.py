# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup

page = requests.get("https://247ctf.com/scoreboard")
# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.text)

# notice differences here:
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.find("a"))

for line in soup.find_all("a"):
    print(line)
    print(line.get("href"))

print(soup.find(id="fetch-error"))
print(soup.find(class_="nav-link"))
print(soup.find("a", class_="nav-link"))

table = soup.find("table")
# print(table)
table_body = table.find("tbody")
rows = table_body.find_all("tr")

for row in rows:
    # print("---")
    # print(row)
    columns = [x.text.strip() for x in row.find_all("td")]
    # print(columns)
    print("{} is in {} place with {} points".format(columns[2], columns[0], columns[4]))
