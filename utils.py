from exceptions import *
from datetime import datetime as dt
from teams.models import Team


def data_processing(data: dict) -> dict | str:
    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    current_year = dt.now().year
    first_cup_date = dt.strptime(data["first_cup"], "%Y-%m-%d").date()
    first_cup_year = first_cup_date.year

    if first_cup_year < 1930 or first_cup_year > current_year or (first_cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    if data["titles"] > (current_year - first_cup_year) / 4:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

    try:
        ...
    except NegativeTitlesError as err:
        return err.message
    except InvalidYearCupError as err:
        return err.message
    except ImpossibleTitlesError as err:
        return err.message


print(Team)
