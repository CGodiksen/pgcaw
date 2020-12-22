import requests
from bs4 import BeautifulSoup


class Contributions:
    def __init__(self, username):
        url = f"https://github.com/users/{username}/contributions"
        r = requests.get(url)

        self.contributions_soup = BeautifulSoup(r.text, "html.parser")
