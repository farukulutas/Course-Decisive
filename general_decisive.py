import requests
from bs4 import BeautifulSoup

# To filter the general elective courses you can take.
# Select all courses in base_url and paste them into general_courses.TXT.

base_url = "https://stars.bilkent.edu.tr/srs-v2/curriculum/courses/electives/elective-code/CS_GE/offered-courses/0"
course_gpa_dict = {}

html = requests.get(base_url).text
soup = BeautifulSoup(html, "lxml")
td = soup.select('td')

# Using readlines()
file1 = open('general_courses.TXT', 'r')
Lines = file1.readlines()
courses_list = []
res_str = ""

# Strips the newline character
for line in Lines:
    if line[0] == " ":
        continue

    res = line.split()
    if res[-1] == "Satisfied":
        res_str += res[1] + res[2] + " "

print(res_str)
print("END")
