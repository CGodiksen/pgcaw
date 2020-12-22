import requests

from datetime import datetime, timedelta
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

    @staticmethod
    def current_streak(daily_contributions):
        """
        Return the length of the current commit streak as well as the two dates specifying the period.
        The output is a three-tuple with the format (streak_length, from, to). If the user is not on a streak then
        from and to will be None.
        """
        list.reverse(daily_contributions)

        to_date = None
        from_date = None
        streak_counter = 0

        current_day = daily_contributions.pop(0)
        # If the user is currently on a streak then find out when the streak started.
        if current_day[1] > 0:
            to_date = current_day[0]
            streak_counter += 1
            for day in daily_contributions:
                if day[1] > 0:
                    streak_counter += 1
                else:
                    from_date = day[0] + timedelta(days=1)
                    break

        return streak_counter, from_date, to_date

    def longest_streak(self, daily_contributions):
        """
        Return the length of the longest commit streak as well as the two dates specifying the period.
        The output is a three-tuple with the format (streak_length, from, to). If the user has never committed then
        from and to will be None.
        """
        # Remove all days without contributions.
        active_days = list(filter(lambda day: day[1] > 0, daily_contributions))

        # Iterate through remaining days to find all streaks of any length.

        # Return the longest streak, if any exist.


test = Contributions("cgodiksen")
daily = test.daily_contributions()
print(test.longest_streak(daily))
