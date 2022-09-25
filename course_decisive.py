'''
This program takes the course GPA in the last fall semester by going to the 
evaluation pages of the courses given. It then lists all courses in descending 
order and creates a list of possible courses to take.

WARNING: When spring is added to the eval page, it will take the fall period 
because we limit the td index. We need to update.
'''

import operator
import re
import requests
from bs4 import BeautifulSoup

# MANDA. + TECH. PHYS102 CS342 CS353 EEE391 CS473 IE400 CS476 CS411 CS421 CS429 CS464 CS465 CS481 CS489 CS490 CS681 EEE485 IE452 MATH202 MATH260 MATH323 MBG209 MBG326
# GENERAL ADA131 ADA263 AMER115 AMER195 AMER476 ARCH321 ARCH341 ARCH411 ARCH418 ARCH463 ARCH465 CHEM201 CHEM461 COMD203 COMD210 COMD321 COMD341 COMD355 COMD357 COMD361 COMD364 COMD433 COMD437 COMD439 COMD451 COMD471 COMD527 CS489 CS490 ECON101 ECON102 ECON103 ECON107 ECON108 ECON203 ECON205 ECON207 ECON221 ECON225 ECON439 EDEB401 EDEB405 EDEB415 EDEB432 EEE485 ELIT139 ELIT143 ENG117 FA103 FA171 FA207 FA211 FA213 FA215 FA217 FA219 FA223 FA271 FA361 FA421 GRA131 GRA209 GRA211 GRA215 GRA217 GRA218 GRA223 GRA225 GRA324 GRA341 GRA421 HART111 HART117 HART120 HART125 HART221 HART222 HART227 HART231 HART239 HART305 HART352 HART372 HART409 HART423 HART434 HART436 HCIV101 HCIV102 HIST411 HIST413 HIST417 HIST431 HUM331 IAED221 IAED322 IAED341 IAED391 IAED392 IAED394 IAED397 IAED461 IAED463 IAED492 IE102 IE202 IE342 IE452 IE490 IR101 IR205 IR227 IR236 IR303 IR305 IR311 IR331 IR333 IR338 IR358 IR413 IR439 IR464 IR492 LAUD221 LAUD251 LAUD357 LAUD421 LAUD471 LAUD481 LAW103 LAW105 LAW203 LAW205 LAW210 LAW211 LAW313 LAW315 LAW411 LNG111 LNG121 LNG131 LNG141 LNG161 LNG221 LNG231 LNG241 LNG331 MAN211 MAN216 MAN262 MAN333 MAN467 MATH202 MATH220 MATH223 MATH240 MATH250 MATH260 MATH264 MATH323 MBG209 MBG301 MBG326 MBG416 MBG488 ME570 MSC110 PHIL101 PHIL103 PHIL201 PHIL203 PHIL303 PHIL304 PHIL308 PHIL401 PHYS252 POLS101 POLS104 POLS201 POLS229 POLS303 POLS304 POLS305 POLS306 POLS346 POLS420 POLS437 POLS449 POLS452 POLS465 POLS473 POLS480 POLS490 POLS560 POLS4560 PSYC100 PSYC101 PSYC102 PSYC103 PSYC200 PSYC220 PSYC230 PSYC240 SOC101 THR103 THR105 THR227 THR327 THR331 THR431

print("For the program to work, you must be connected to bilkent-vpn or be able to access the base_url.")
print("base_url = https://stars.bilkent.edu.tr/evalreport/index.php?mode=crs&crsCode=\n")
print("You can use general_decisive.py to list the General Elective courses you can take.\n")
print("IF GPA is 0 or TEXT, THERE IS NO RECORD IN THE SELECTED SEMESTER!")
semester = input("Please choose your semester (e.g Fall or Spring):")
courses = input("Please enter possible courses (e.g CS101 CS102 ...):")
courses_list = courses.split()
base_url = "https://stars.bilkent.edu.tr/evalreport/index.php?mode=crs&crsCode="
course_gpa_dict = {}

# add each course gpa pair to dict from url
for course in courses_list:
   codeAndNum_list = re.findall("[A-Z]+|[0-9]+", course)
   code = codeAndNum_list[0]
   num = codeAndNum_list[1]
   url = base_url + code + "&crsNum=" + num
   html = requests.get(url).text
   soup = BeautifulSoup(html, "lxml")
   td = soup.select('td')
   count = 2
   flag = False
   for name, value in zip(td, td[2:]):
      if semester in name.text:
          flag = True
      if flag and count % 8 == 5:
          course_gpa_dict[course] = value.text
          break
      count += 1

# sort the list by descending order
course_gpa_dict_desc = dict( sorted(course_gpa_dict.items(), key=operator.itemgetter(1), reverse=True))

# print courses in descending order
print("Course" + "\t", "GPA")
for key, val in course_gpa_dict_desc.items():
        print(key + "\t", val)

# MANDA. + TECH. RESULT
'''
Course	 GPA
CS429	 Class Size:
CS681	 Class Size:
CS489	 4.00###3.30 ort
CS490	 3.93###3.00 ort
EEE391	 2.81
CS421	 2.81
IE400	 2.71
CS465	 2.68
MBG326	 2.64
MATH260	 2.61
EEE485	 2.54
CS342	 2.53
CS411	 2.53
MBG209	 2.41
CS473	 2.34
CS464	 2.32
CS353	 2.28
CS481	 2.10
CS476	 1.98
PHYS102	 1.90
MATH323	 1.58
MATH202	 0.91
'''

# GENERAL RESULT
'''
GRA209	 3.80
HIST417	 3.60
FA207	 3.58
GRA421	 3.56
LAUD471	 3.56
EDEB405	 3.55
HIST431	 3.53
POLS346	 3.48
FA219	 3.47
FA103	 3.46
IR492	 3.46
FA217	 3.45
ARCH465	 3.44
POLS420	 3.44
LAUD481	 3.43
FA211	 3.41
HART409	 3.40
HART423	 3.40
THR327	 3.40
THR431	 3.40
FA421	 3.39
THR103	 3.38
HIST411	 3.37
PHIL304	 3.35
THR331	 3.35
GRA223	 3.34
COMD364	 3.33
LNG241	 3.33
HCIV102	 3.32
FA213	 3.31
POLS473	 3.28
POLS452	 3.27
FA223	 3.26
MBG416	 3.25
POLS201	 3.25
IAED492	 3.23
THR227	 3.23
LNG231	 3.22
THR105	 3.22
HART221	 3.20
POLS229	 3.18
MSC110	 3.16
IAED322	 3.14
IR439	 3.14
MBG488	 3.14
IAED391	 3.13
FA215	 3.12
PHIL103	 3.12
GRA215	 3.10
COMD357	 3.09
GRA225	 3.09
POLS306	 3.09
COMD471	 3.06
IAED394	 3.05
PHIL401	 3.05
FA271	 3.04
GRA211	 3.03
IR358	 3.03
GRA131	 3.01
LAW411	 3.00
HCIV101	 2.96
COMD451	 2.95
HART117	 2.95
LNG161	 2.95
PHIL203	 2.95
IAED397	 2.94
GRA324	 2.93
GRA217	 2.92
IAED392	 2.92
LNG141	 2.91
MAN467	 2.91
COMD433	 2.90
MBG301	 2.90
ARCH418	 2.85
ELIT139	 2.85
LAW211	 2.85
LNG111	 2.84
PHIL101	 2.84
POLS104	 2.84
POLS303	 2.82
HIST413	 2.79
ARCH321	 2.78
IR311	 2.78
LNG221	 2.78
GRA341	 2.77
ARCH411	 2.76
ELIT143	 2.76
LNG131	 2.76
LAUD221	 2.75
POLS304	 2.75
GRA218	 2.74
PSYC230	 2.72
LAW210	 2.71
HART125	 2.70
POLS465	 2.70
AMER195	 2.69
LAUD251	 2.68
POLS480	 2.68
COMD210	 2.67
POLS490	 2.67
COMD321	 2.66
IAED221	 2.66
MATH220	 2.66
POLS449	 2.66
HART436	 2.65
PSYC102	 2.65
MBG326	 2.64
AMER115	 2.63
ARCH341	 2.63
COMD203	 2.62
COMD341	 2.62
HART120	 2.62
HART239	 2.62
FA361	 2.61
MAN333	 2.61
MATH260	 2.61
IE102	 2.60
MAN211	 2.59
CHEM201	 2.58
CHEM461	 2.58
PSYC101	 2.58
PHIL303	 2.56
PSYC240	 2.56
ECON207	 2.55
EEE485	 2.54
FA171	 2.54
HART305	 2.54
COMD437	 2.52
IAED463	 2.52
SOC101	 2.52
IR227	 2.51
IR333	 2.51
LAW313	 2.51
PSYC220	 2.51
LNG121	 2.49
PSYC100	 2.47
PHIL201	 2.44
ADA131	 2.43
MAN262	 2.43
ECON108	 2.42
ECON439	 2.42
ENG117	 2.42
LAW105	 2.42
IE342	 2.41
MBG209	 2.41
POLS305	 2.41
MATH250	 2.39
COMD355	 2.37
HART111	 2.36
MAN216	 2.36
IR101	 2.31
IR413	 2.30
MATH223	 2.30
MATH240	 2.30
PSYC103	 2.30
IR338	 2.29
POLS101	 2.28
PSYC200	 2.27
LAW103	 2.23
ECON205	 2.22
IE202	 2.22
IR236	 2.22
IR205	 2.18
ECON102	 2.17
LAW205	 2.12
ECON101	 2.11
ADA263	 2.10
MATH264	 2.10
ECON107	 2.07
ECON221	 2.06
IR305	 2.06
ECON103	 2.02
ECON203	 1.98
HART231	 1.96
ECON225	 1.90
LAW315	 1.90
IR303	 1.79
LAW203	 1.72
MATH323	 1.58
MATH202	 0.91
COMD361	 0.00
IAED341	 0.00
'''

#MANDA + TECH
'''
Course	 GPA
CS415	 2.92
CS461	 2.91
EEE391	 2.81
CS421	 2.81
CS453	 2.76
CS484	 2.75
IE400	 2.71
CS465	 2.68
MBG326	 2.64
MATH260	 2.61
EEE485	 2.54
CS342	 2.53
CS411	 2.53
CS413	 2.46
MBG209	 2.41
CS473	 2.34
CS464	 2.32
CS353	 2.28
CS458	 2.15
CS481	 2.10
CS476	 1.98
PHYS102	 1.90
'''

#GENERAL
'''
EDEB401	 3.93
GRA351	 3.88
HIST313	 3.86
POLS464	 3.86
MSC373	 3.85
SFL405	 3.83
GRA209	 3.80
HIST315	 3.78
MSC113	 3.78
IR495	 3.72
ECON443	 3.70
MSC425	 3.70
FA214	 3.69
IAED491	 3.65
HIST417	 3.60
MSC326	 3.59
FA207	 3.58
GRA421	 3.56
LAUD471	 3.56
EDEB405	 3.55
THR203	 3.55
HIST431	 3.53
MBG473	 3.50
COMD356	 3.48
POLS346	 3.48
ADA412	 3.47
FA219	 3.47
FA103	 3.46
IR492	 3.46
FA217	 3.45
THR228	 3.45
ARCH465	 3.44
POLS420	 3.44
ECON318	 3.43
ECON400	 3.43
LAUD481	 3.43
MSC323	 3.43
THR303	 3.43
LNG191	 3.42
FA211	 3.41
MAN437	 3.41
ME481	 3.41
THR205	 3.41
HART409	 3.40
HART423	 3.40
THR327	 3.40
THR431	 3.40
FA421	 3.39
LNG113	 3.39
MAN451	 3.39
THR103	 3.38
HIST411	 3.37
PSYC434	 3.36
PHIL304	 3.35
THR331	 3.35
GRA207	 3.34
GRA223	 3.34
COMD364	 3.33
LNG241	 3.33
HCIV102	 3.32
FA213	 3.31
ARCH466	 3.30
POLS343	 3.30
HIST481	 3.29
LAW101	 3.29
MBG470	 3.29
POLS473	 3.28
POLS452	 3.27
SFL207	 3.27
FA223	 3.26
MBG418	 3.26
MSC173	 3.26
MSC213	 3.26
SFL431	 3.26
MBG416	 3.25
POLS201	 3.25
POLS309	 3.25
EEE443	 3.24
GRA323	 3.23
IAED492	 3.23
THR227	 3.23
COMD346	 3.22
LNG231	 3.22
THR105	 3.22
COMD461	 3.20
HART221	 3.20
LNG134	 3.19
ARCH317	 3.18
GRA210	 3.18
LNG143	 3.18
MAN433	 3.18
MSC273	 3.18
MSC473	 3.18
POLS229	 3.18
ECON351	 3.17
EDEB419	 3.15
FA107	 3.14
GRA333	 3.14
IAED322	 3.14
IE479	 3.14
IR439	 3.14
MBG488	 3.14
IAED391	 3.13
PSYC310	 3.13
FA215	 3.12
PHIL103	 3.12
PSYC330	 3.12
MATH110	 3.11
PSYC206	 3.11
GRA215	 3.10
LNG142	 3.10
COMD357	 3.09
GRA225	 3.09
LAW413	 3.09
POLS306	 3.09
POLS331	 3.09
IAED415	 3.07
MAN421	 3.07
SFL101	 3.07
COMD350	 3.06
COMD471	 3.06
ECON206	 3.06
ELIT421	 3.06
IE443	 3.06
IE469	 3.06
IAED394	 3.05
PHIL401	 3.05
COMD331	 3.04
FA271	 3.04
IR349	 3.04
PSYC433	 3.04
GRA211	 3.03
IR358	 3.03
ELIT359	 3.02
ELIT377	 3.02
GRA131	 3.01
ENG312	 3.00
HART343	 3.00
LAW411	 3.00
MSC374	 3.00
PSYC482	 3.00
CHEM320	 2.99
COMD310	 2.99
ECON409	 2.99
ELIT209	 2.99
IR470	 2.99
PHYS420	 2.99
POLS238	 2.99
COMD442	 2.97
LAW307	 2.97
MAN410	 2.97
ME440	 2.97
PSYC430	 2.97
HART225	 2.96
HCIV101	 2.96
MAN414	 2.96
AMER343	 2.95
COMD451	 2.95
HART117	 2.95
IE440	 2.95
LAW304	 2.95
LNG161	 2.95
PHIL203	 2.95
PSYC350	 2.95
ELIT463	 2.94
IAED397	 2.94
MAN439	 2.94
GRA324	 2.93
POLS324	 2.93
POLS411	 2.93
GRA217	 2.92
IAED392	 2.92
AMER293	 2.91
LNG141	 2.91
MAN462	 2.91
MAN467	 2.91
COMD363	 2.90
COMD433	 2.90
HART426	 2.90
MBG301	 2.90
PSYC360	 2.90
CHEM301	 2.89
EEE473	 2.89
POLS357	 2.89
COMD434	 2.88
EDEB413	 2.88
GRA313	 2.88
MATH453	 2.88
CHEM323	 2.87
ELIT273	 2.87
LAUD371	 2.87
IR494	 2.86
PSYC435	 2.86
ARCH418	 2.85
COMD207	 2.85
ELIT139	 2.85
LAW211	 2.85
LAW403	 2.85
PSYC405	 2.85
LNG111	 2.84
MATH443	 2.84
PHIL101	 2.84
PHYS371	 2.84
POLS104	 2.84
AMER384	 2.83
AMER427	 2.83
IE448	 2.83
PHYS453	 2.83
AMER383	 2.82
MAN401	 2.82
MAN404	 2.82
POLS303	 2.82
IE376	 2.81
IE432	 2.81
IE468	 2.81
LNG122	 2.81
PSYC431	 2.81
AMER459	 2.80
MATH302	 2.80
PSYC320	 2.80
HIST413	 2.79
IE482	 2.79
IR477	 2.79
ARCH321	 2.78
IR311	 2.78
LAW303	 2.78
LNG221	 2.78
GRA341	 2.77
POLS431	 2.77
ARCH411	 2.76
ELIT143	 2.76
LNG131	 2.76
PSYC205	 2.76
'''