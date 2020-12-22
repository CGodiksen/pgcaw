import requests

from datetime import datetime
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
        days = self.contributions_soup.find_all("rect", class_="day")

        dates = [datetime.strptime(day["data-date"], "%Y-%m-%d").date() for day in days]
        number_contributions = [int(day["data-count"]) for day in days]

        return list(zip(dates, number_contributions))

    def current_streak(self):
        """
        Return the length of the current commit streak as well as the two dates specifying the period.
        The output is a three-tuple with the format (streak_length, from, to).
        """

    def longest_streak(self):
        """
        Return the length of the longest commit streak as well as the two dates specifying the period.
        The output is a three-tuple with the format (streak_length, from, to).
        """


test = Contributions("cgodiksen")
print(test.daily_contributions())
