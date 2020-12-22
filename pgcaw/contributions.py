import requests
from bs4 import BeautifulSoup


class Contributions:
    def __init__(self, username):
        url = f"https://github.com/users/{username}/contributions"
        r = requests.get(url)
        self.contributions_soup = BeautifulSoup(r.text, "html.parser")

    def total_contributions(self):
        # Find the h2 title text that contains the total contributions.
        title = self.contributions_soup.find("h2").text

        # Extracting the number from the title.
        return int(title.strip().split("contributions")[0].strip().replace(",", ""))


test = Contributions("cgodiksen")
print(test.total_contributions())
