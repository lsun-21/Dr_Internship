import top_1day
import top_7days

log_file = 'sample_listen-2021-12-01_2Mlines.log'
top_1day.write_1day_top50(log_file)

top_7days.write_7days_top50('country_top50_20211201.txt') # To uncomment if the main has already been run once
top_7days.write_7days_top50('user_top50_20211201.txt') # To uncomment if the main has already been run once
