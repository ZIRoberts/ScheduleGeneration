# ScheduleGeneration
Terminal base schedule generation program made with python.

Motive:
The driving motive be hind this project is so then
students will no longer have to spend time creating their own schedules or
worrying whether or not they chose their best schedule. By running the example
file you will see that I had 36 possible schedules for one of my semesters.
I only had the time to make and compare a total of 4 schedules.

How to use:
Navigate to the generation.py file and open it. On line 8 you input the name of
the csv (comma separated variable) file you whish to use as an input, by default
this is "example.csv". This csv file must be in the same folder and match the same
layout as the "exmaple.csv".

To run the program you must navigate to its file directory via Terminal and
then type 'python.exe generation.py' and the output will be printed to the
Terminal

Future Plans/Stages of Progression:
1. Refactor required layout for input csv
2. Print output schedules as csv files
3. Make GUI and have output displayed graphically
4. Have it scrape the YCP schedule of classes page to get all class information
   instead of requiring an input csv file
5. Make it so you can sort your course how ever want, what time you want to
   have a specific course, what professor you want, etc.
