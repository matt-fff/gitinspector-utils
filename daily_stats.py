import sys
import json
import os
from datetime import datetime
from terminaltables import AsciiTable

def print_dailies(statistics):

    start_date = datetime.strptime(
        os.environ['START_DATE'], "%a %b %d %H:%M:%S %Z %Y"
    )

    days_passed = (datetime.utcnow() - start_date).days
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
