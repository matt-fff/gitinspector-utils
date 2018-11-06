import sys
import json
import os
from datetime import datetime
from terminaltables import AsciiTable

def get_env_date(env_name):
    return datetime.date(datetime.strptime(
        os.environ[env_name], "%a %b %d %H:%M:%S %Z %Y"
    ))


def print_dailies(statistics):

    start_date = get_env_date('START_DATE')
    end_date = get_env_date('END_DATE')

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
    print_dailies(json.loads(STATS))
