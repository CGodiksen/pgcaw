# PGCAW: The Python Github Calendar API Wrapper
PGCAW is a very simple API wrapper for the github contributions calendar. The wrapper supports extracting data about any given users contribution history, 
such as total contributions in the last year and daily contribution numbers. 

## Installation
The recommended way to install [PGCAW](https://pypi.org/project/pgcaw/) is using pip.
```
pip install pgcaw
```

## Usage
To gather data about a specific Github user you first need to create a `Contributions` instance, initialized with the given users username.
```python
>>> import pgcaw
>>> contributions = pgcaw.Contributions("CGodiksen")
```
Using this instance you can now get data related to the users Github calendar.
```python
>>> contributions.total()
1758
>>> contributions.daily()
[(datetime.date(2020, 12, 20), 1), (datetime.date(2020, 12, 21), 1), (datetime.date(2020, 12, 22), 16)]
```
Notice that `daily()` returns a list of tuples with the format `[(date, number_contributions_on_date)]`.

The class also contains some utility methods used to extract further information from the contributions graph.
```python
>>> daily = contributions.daily()
>>> contributions.current_streak(daily)
(23, datetime.date(2020, 1, 12), datetime.date(2020, 12, 23))
>>> contributions.longest_streak(daily)
(105, datetime.date(2020, 8, 10), datetime.date(2020, 11, 23))
```
Note here that both `current_streak()` and `longest_streak()` returns a tuple with the format `(streak_length, from_date, to_date)`.
If the given user is not currently on a streak then `current_streak()` will return `(0, None, None)`.
The same applies for `longest_streak()` if the user has not made any contributions.