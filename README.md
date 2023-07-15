# Dr_Internship
Technical test for an internship

This project consists of three Python scripts: **top_1day.py**, **top_7days.py**, and **main.py**. 

### How to run the project ? 

To run the project, you need to execute the **main.py** script in the terminal, using the command **python main.py**. Another possible command is : python3 main.py.

### Constraints/Objectives : 

I included the dr_internship.zip, a zip file containing : 
- as many files as needed (scripts, programs, functions, etc...)
- a README file describing the solution implemented, how to run it every day to compute the files.
My solution uses **700 MiB max**, as we can see in the report_memory.txt

*** 

When you run main.py, it will create four directories and produce a report_memory.txt file. Here is the directory structure:

- Main directory (root):

    - **top_1day.py**
    - **top_7days.py**
    - **main.py**
    - **report_memory.txt**
    - *Country_top50* (directory): Contains files named **country_top50_YYYYMMDD.txt** with the top 50 songs listened in a specific country each day.
    - *Users_top50* (directory): Contains files named **user_top50_YYYYMMDD.txt** with the top 50 songs most listened to by each user each day.
    - *Country_top50_7days* (directory): Contains files named **country_top50_7days_YYYYMMDD.txt** with the top 50 songs listened in a specific country in the last 7 days before YYYYMMDD.
    - *Users_top50_7days* (directory): Contains files named **user_top50_7days_YYYYMMDD.txt** with the top 50 songs most listened to by each user in the last 7 days before YYYYMMDD.

The **report_memory.txt** file is a text file that represents the report memory of the most recent execution of the main.py script. It contains information about the memory usage during the execution of the script.

The **top_1day.py** script generates two types of files each day:
- country_top50_YYYYMMDD.txt: Contains the top 50 songs listened to in a specific country. Each row in the file follows the format: country|sng_id1:n1,sng_id2:n2,sng_id3:n3,...,sng_id50:n50, where country is the country ISO code, and sng_id1:n1 represents the identifier of the song with the corresponding number of streams, sng_id2:n2 represents the second most listened song, and so on.
- user_top50_YYYYMMDD.txt: Contains the top 50 songs most listened to by each user. Each row follows the format: user_id|sng_id1:n1,sng_id2:n2,sng_id3:n3,...,sng_id50:n50, where user_id is the identifier of the user, and the song identifiers and stream counts are listed similarly to the country file.

Similarly, the **top_7days.py** script generates two types of files each day:
- country_top50_7days_YYYYMMDD.txt: Contains the top 50 songs listened to in a specific country in the last 7 days before YYYYMMDD.
- user_top50_7days_YYYYMMDD.txt: Contains the top 50 songs most listened to by each user in the last 7 days before YYYYMMDD.

### Disclaimer : 

Due to being provided with only the sample_listen_2021-12-01.log file, it was not possible to determine the country's top 50 songs for the 7 days before the specified date. However, a file named country_top50_7days_20211201.txt is still created, even though it may not be representative. So the contents of this file country_top50_7days_20211201.txt represent the top 50 songs listened to in the country on December 1, 2021, due to the lack of data. 
