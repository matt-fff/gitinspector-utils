pull-repos=$(shell cd ./git-repos && find . -maxdepth 1 -type d | grep '[A-Za-Z]' | sed 's/\.\///' | xargs -I % sh -c "mv % %.bak; git -C %.bak config --get remote.origin.url | xargs git clone && rm -rf %.bak")
monthly-report=$(shell cd ./git-repos && ls | xargs -t gitinspector -T --weeks=true --since=\"$(shell date --date='00:00 last month' +%Y-%m-%d)\" -F html > ../git-reports/month-to-date.html)
weekly-report=$(shell cd ./git-repos && ls | xargs -t gitinspector --since=\"$(shell date --date='00:00 last week' +%Y-%m-%d)\" -F html > ../git-reports/week-to-date.html)
show-reports=$(shell chromium $(shell pwd)/git-reports/week-to-date.html $(shell pwd)/git-reports/month-to-date.html)
git-avg=$(shell export END_DATE=$(shell date --date='00:00 today' +%Y-%m-%d) && cd ./git-repos && ls | xargs -t gitinspector --since="\$START_DATE" --until="\$END_DATE" -F json | ._venv/bin/python ./daily_stats.py)
git-avg-weekly=$(shell export START_DATE=$(shell date --date='00:00 last week' +%Y-%m-%d) && $(call git-avg))
git-avg-monthly=$(shell export START_DATE=$(shell date --date='00:00 last month' +%Y-%m-%d) && $(call git-avg))

.PHONY: pull-repos monthly-report weekly-report show-reports run-reports git-avg git-avg-weekly git-avg-monthly
git-avg-weekly:
	$(call git-avg-weekly)
git-avg-monthly:
	$(call git-avg-monthly)
restore-backup-repos:
	cd ./git-repos && find . -maxdepth 1 -type d | grep '.bak' | sed 's/\.bak//' | xargs -P 8 -I % mv %.bak %
pull-repos:
	$(call pull-repos)
weekly-report:
	$(call weekly-report)
monthly-report:
	$(call monthly-report)
show-reports:
	$(call show-reports)
run-reports:
	$(call pull-repos) && $(call weekly-report) && $(call monthly-report) && $(call show-reports)
