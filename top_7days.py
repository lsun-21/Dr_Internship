from memory_profiler import profile
from datetime import datetime, timedelta
import os
import re
from collections import defaultdict

file_path = open('report_memory.txt', 'w+')
@profile(stream=file_path)
def parse_log_file(log_file):
    data = []
    with open(log_file, 'r') as file:
        for line in file:
            try:
                id, song_counts = line.strip().split('|')
                song_counts = song_counts.split(',')
                song_counts = [count.split(':') for count in song_counts]
                song_counts = [(sng_id, int(count)) for sng_id, count in song_counts]
                data.append((id, song_counts))
            except ValueError:
                continue  # Skip corrupted rows
    return data

@profile(stream=file_path)
def top50_7days(current_day_file):
    if re.search(r'(country_top50_)', current_day_file) :
        log_directory = 'Country_top50'
    elif re.search(r'(user_top50_)', current_day_file) :
        log_directory = 'User_top50'
    else :
        raise ValueError('Log file name not found')
    file_name = os.path.basename(current_day_file)

    date_match = re.search(r'(\d{4})(\d{2})(\d{2})', file_name)
    if date_match:
        year = int(date_match.group(1))
        month = int(date_match.group(2))
        day = int(date_match.group(3))
    else:
        return None
    date_match = None

    # Determine the date range for the last 7 days
    current_date = datetime(year, month, day)
    date_range_start = current_date - timedelta(days=7)

    # Collect and process log files for the last 7 days
    relevant_log_files = []

    for file in os.listdir(log_directory):
        if file.startswith('country_top50_') or file.startswith('user_top50_'):
            try:
                log_date = datetime.strptime(file[-12:-4], "%Y%m%d")
                if date_range_start < log_date <= current_date:
                    relevant_log_files.append(file)
            except ValueError:
                continue  # Skip log files with invalid date format
    
    current_date = None
    date_range_start = None

    # Aggregate song stream counts for the last 7 days
    stream_counts = defaultdict(lambda: defaultdict(int))

    for log_file in relevant_log_files:
        log_file_path = os.path.join(log_directory, log_file)
        daily_data = parse_log_file(log_file_path)
        for id, song_counts in daily_data:
            for sng_id, count in song_counts:
                stream_counts[id][sng_id] += count

    relevant_log_files = None

    # Compute Top 50 Songs per Id 
    top_songs = {}
    for id, song_counts in stream_counts.items():
        top_songs[id] = sorted(song_counts.items(), key=lambda x: x[1], reverse=True)[:50]

    stream_counts = None 

    return top_songs

@profile(stream=file_path)
def write_7days_top50(log_file):
    date_match = re.search(r'(\d{4})(\d{2})(\d{2})', log_file)
    if date_match:
        year = int(date_match.group(1))
        month = int(date_match.group(2))
        day = int(date_match.group(3))
    else : 
        return None

    date_match = None 
    top_songs = top50_7days(log_file)

    # Write Output to Files
    if re.search(r'(country_top50_)', log_file) :
        countries_output_directory = 'Country_top50_7days'
        os.makedirs(countries_output_directory, exist_ok=True)

        # Write top 50 songs per country to file
        country_output_file = os.path.join(countries_output_directory, f'country_top50_7days_{year}{month:02d}{day:02d}.txt')
        with open(country_output_file, 'w') as file:
            for country, songs in top_songs.items():
                song_string = ','.join([f'{sng_id}:{count}' for sng_id, count in songs])
                file.write(f'{country}|{song_string}\n')

        country_output_file = None 
        countries_output_directory = None
    
    elif re.search(r'(user_top50_)', log_file) :
        users_output_directory = 'User_top50_7days'
        os.makedirs(users_output_directory, exist_ok=True)

        # Write top 50 songs per user to one global file (optional)
        users_output_file = os.path.join(users_output_directory, f'user_top50_7days_{year}{month:02d}{day:02d}.txt')
        with open(users_output_file, 'w') as file:
            for user_id, songs in top_songs.items():
                song_string = ','.join([f'{sng_id}:{count}' for sng_id, count in songs])
                file.write(f'{user_id}|{song_string}\n')

        users_output_file = None 
        users_output_directory = None
    
    top_songs = None
    
    return None


