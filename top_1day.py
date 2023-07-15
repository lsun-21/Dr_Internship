from memory_profiler import profile
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
                sng_id, user_id, country = line.strip().split('|')
                data.append((sng_id, user_id, country))
            except ValueError:
                continue  # Skip corrupted rows
    return data


@profile(stream=file_path)
def top50_1day(log_file):
    daily_data = parse_log_file(log_file)

    # Data Processing
    stream_counts_country = defaultdict(lambda: defaultdict(int))
    stream_counts_user = defaultdict(lambda: defaultdict(int))

    for sng_id, user_id, country in daily_data:
        stream_counts_country[country][sng_id] += 1
        stream_counts_user[user_id][sng_id] += 1

    daily_data = None

    # Compute Top 50 Songs per Country
    top_songs_country = {}
    for country, song_counts in stream_counts_country.items():
        top_songs_country[country] = sorted(song_counts.items(), key=lambda x: x[1], reverse=True)[:50]

    stream_counts_country = None

    # Compute Top 50 Songs per User (Optional)
    top_songs_user = {}
    for user_id, song_counts in stream_counts_user.items():
        top_songs_user[user_id] = sorted(song_counts.items(), key=lambda x: x[1], reverse=True)[:50]

    stream_counts_user = None 

    return top_songs_country, top_songs_user


@profile(stream=file_path)
def write_1day_top50(log_file):
    date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})|(\d{4})(\d{2})(\d{2})', log_file)
    if date_match:
        groups = date_match.groups()
        year = int(groups[0]) if groups[0] else int(groups[3])
        month = int(groups[1]) if groups[1] else int(groups[4])
        day = int(groups[2]) if groups[2] else int(groups[5])
    else:
        raise ValueError('Date not found in log file name')

    date_match = None 
    top_songs_country, top_songs_user = top50_1day(log_file)

    # Write Output to Files
    countries_output_directory = 'Country_top50'
    users_output_directory = 'User_top50'

    os.makedirs(countries_output_directory, exist_ok=True)
    os.makedirs(users_output_directory, exist_ok=True)

    # Write top 50 songs per country to file
    country_output_file = os.path.join(countries_output_directory, f'country_top50_{year}{month:02d}{day:02d}.txt')
    with open(country_output_file, 'w') as file:
        for country, songs in top_songs_country.items():
            song_string = ','.join([f'{sng_id}:{count}' for sng_id, count in songs])
            file.write(f'{country}|{song_string}\n')

    country_output_file = None 
    top_songs_country = None

    # Write top 50 songs per user to one global file (optional)
    users_output_file = os.path.join(users_output_directory, f'user_top50_{year}{month:02d}{day:02d}.txt')
    with open(users_output_file, 'w') as file:
        for user_id, songs in top_songs_user.items():
            song_string = ','.join([f'{sng_id}:{count}' for sng_id, count in songs])
            file.write(f'{user_id}|{song_string}\n')

    users_output_file = None 
    top_songs_user = None

    return None
