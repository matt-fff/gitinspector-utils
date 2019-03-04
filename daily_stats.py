import sys
import json
import os
from datetime import datetime
from terminaltables import AsciiTable

def format_date(date_str):
    return datetime.date(datetime.strptime(
        date_str, "%Y-%m-%d"
    ))


def print_dailies(statistics, start_date, end_date):

    days_passed = (end_date - start_date).days
    authors = statistics["gitinspector"]["changes"]["authors"]
    dailies = [
        ["Author", "Commits/Day", "Inserts/Day", "Deletes/Day"]
    ]
    for author in authors:
        dailies.append(
            [author["name"]] + ['{0:.3g}'.format(author[key] / days_passed) for key in [
                "commits", "insertions", "deletions"
            ]]
        )

    dailies.sort()
    print(AsciiTable(dailies).table)


if __name__ == "__main__":
    STATS = sys.stdin.read()
    print(sys.argv)
    start_date = format_date(os.environ.get('START_DATE', sys.argv[1]))
    end_date = format_date(os.environ.get('END_DATE', sys.argv[2]))
    print_dailies(json.loads(STATS), start_date, end_date)
