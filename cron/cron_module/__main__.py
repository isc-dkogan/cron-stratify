from crontab import CronTab
from datetime import datetime

mem_cron = CronTab(tab="""
  * * * * 1-5 python3 cron_module/run_stratify.py
""")

for result in mem_cron.run_scheduler():
  print(f'Ran stratify at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
  print(f"Standard Out: {result}")
