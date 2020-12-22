import requests
from bs4 import BeautifulSoup


class Contributions:
    def __init__(self, username):
        url = f"https://github.com/users/{username}/contributions"
        r = requests.get(url)
        self.contributions_soup = BeautifulSoup(r.text, "html.parser")

    def total_contributions(self):
        """Return the total contributions in the last year."""
        # Find the h2 title text that contains the total contributions.
        title = self.contributions_soup.find("h2").text

        # Extracting the number from the title.
        return int(title.strip().split("contributions")[0].strip().replace(",", ""))

    def daily_contributions(self):
        """
        Return a list of tuples, each with the format (date, number_contributions_on_date). The list has an element
        for each day in the last year.
        """
        

test = Contributions("cgodiksen")
print(test.total_contributions())
