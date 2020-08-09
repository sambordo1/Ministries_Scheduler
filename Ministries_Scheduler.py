import xlrd
from itertools import cycle, islice
import csv
import sys

week1 =[]
week2 =[]
week3 =[]
week4 =[]
week5 =[]
week6 =[]
week7 =[]
week8 =[]
week9 =[]
week10=[]
week11=[]
week12=[]
week13=[]
week14=[]
week15=[]
week16=[]
week17=[]
week18=[]
week19=[]
week20=[]
week21=[]
week22=[]
week23=[]
week24=[]

output_file = "Ministries_Schedule.csv"
in_file = ("Ministries.xlsx")
numWeeks = 24

#--------------------------------Reading in ministry arrays -------------------------------------
wb = xlrd.open_workbook(in_file)
sheet = wb.sheet_by_index(0)

data = [[sheet.cell_value(r, c) for r in range(sheet.nrows)] for c in range(sheet.ncols)]
for arrays in data:
	headings = arrays[0]

#------------------------------------------------------
	if headings == "Sound":
		sound = arrays
		del sound[0]
		while ("" in sound):
			sound.remove("")
#--------------------------------------------------
	if headings == "Pham Driving":
		pham = arrays
		del pham[0]
		while ("" in pham):
			pham.remove("")
#-------------------------------------------------
	if headings == "Security":
		security = arrays
		del security[0]
		while ("" in security):
			security.remove("")
#------------------------------------------------
	if headings == "Ushering":
		ushers = arrays
		del ushers[0]
		while ("" in ushers):
			ushers.remove("")
#-------------------------------------------------
	if headings == "Nursery AM":
		nurseryAM = arrays
		del nurseryAM[0]
		while ("" in nurseryAM):
			nurseryAM.remove("")
#-------------------------------------------------
	if headings == "Nursery PM":
		nurseryPM = arrays
		del nurseryPM[0]
		while ("" in nurseryPM):
			nurseryPM.remove("")
#-------------------------------------------------
	if headings == "Nursery Captains AM":
		nurseryCaptAM = arrays
		del nurseryCaptAM[0]
		while ("" in nurseryCaptAM):
			nurseryCaptAM.remove("")
#-------------------------------------------------
	if headings == "Nursery Captains PM":
		nurseryCaptPM = arrays
		del nurseryCaptPM[0]
		while ("" in nurseryCaptPM):
			nurseryCaptPM.remove("")
#--------------------------------------------------
	if headings == "Parking Patrol":
		parking_patrol = arrays
		del parking_patrol[0]
		while ("" in parking_patrol):
			parking_patrol.remove("")
#------------------------------------------------------------------------------------------------




#----------------------------------------Sound---------------------------------------------------
if sound:
	x = 2 * numWeeks # (2 per week * number of weeks)
	i = -1
	soundloop = list( islice( cycle(sound), i+1, i+1+x))

#------------------------------------------------------------------------------------------------
#----------------------------------------Pham---------------------------------------------------

x = 1 * numWeeks # (1 per week * number of weeks)
i = -1
phamloop = list( islice( cycle(pham), i+1, i+1+x))

#------------------------------------------------------------------------------------------------
#----------------------------------------Security---------------------------------------------------

x = 3 * numWeeks # (3 per week * number of weeks)
i = -1
securityloop = list( islice( cycle(security), i+1, i+1+x))

#------------------------------------------------------------------------------------------------
#----------------------------------------Ushers--------------------------------------------------

x = 5 * numWeeks # (5 per week * number of weeks)
i = -1
usherloop = list( islice( cycle(ushers), i+1, i+1+x))

#------------------------------------------------------------------------------------------------
#----------------------------------------Nursery--------------------------------------------------

x = 4 * numWeeks # (5 per week * number of weeks)
i = -1
nurseryloopAM = list( islice( cycle(nurseryAM), i+1, i+1+x))

#------------------------------------------------------------------------------------------------
#----------------------------------------Nursery--------------------------------------------------

x = 4 * numWeeks # (5 per week * number of weeks)
i = -1
nurseryloopPM = list( islice( cycle(nurseryPM), i+1, i+1+x))

#------------------------------------------------------------------------------------------------
#----------------------------------------Nursery--------------------------------------------------

x = 2 * numWeeks # (5 per week * number of weeks)
i = -1
nurseryloopCaptAM = list( islice( cycle(nurseryCaptAM), i+1, i+1+x))

#------------------------------------------------------------------------------------------------
#----------------------------------------Nursery--------------------------------------------------

x = 2 * numWeeks # (5 per week * number of weeks)
i = -1
nurseryloopCaptPM = list( islice( cycle(nurseryCaptPM), i+1, i+1+x))

#------------------------------------------------------------------------------------------------
#----------------------------------------Parking Patrol------------------------------------------

x = 4 * numWeeks # (5 per week * number of weeks)
i = -1
patrolloop = list( islice( cycle(parking_patrol), i+1, i+1+x))

#------------------------------------------------------------------------------------------------

#----------------------Function to Schedule without conflict-------------------------------------

def weekly_Min(ministryloop, numNeeded, weekLoop):

	person_counter = 0
	for index in range(len(ministryloop)):
		while(person_counter <= (numNeeded - 1)):
			if ministryloop[index] not in weekLoop:
				weekLoop.append(ministryloop[index])
				ministryloop.pop(index)
				person_counter += 1
			else:
				break
#------------------------------------------------------------------------------------------------
				
#----------------------Calling weekly_min to fill weekly arrays----------------------------------
weekly_Min(soundloop, 2, week1)
weekly_Min(phamloop, 1, week1)
weekly_Min(securityloop, 3, week1)
weekly_Min(usherloop, 5, week1)
weekly_Min(nurseryloopAM, 4, week1)
weekly_Min(nurseryloopPM, 4, week1)
weekly_Min(nurseryloopCaptAM, 2, week1)
weekly_Min(nurseryloopCaptPM, 2, week1)
weekly_Min(patrolloop, 4, week1)

weekly_Min(soundloop, 2, week2)
weekly_Min(phamloop, 1, week2)
weekly_Min(securityloop, 3, week2)
weekly_Min(usherloop, 5, week2)
weekly_Min(nurseryloopAM, 4, week2)
weekly_Min(nurseryloopPM, 4, week2)
weekly_Min(nurseryloopCaptAM, 2, week2)
weekly_Min(nurseryloopCaptPM, 2, week2)
weekly_Min(patrolloop, 4, week2)

weekly_Min(soundloop, 2, week3)
weekly_Min(phamloop, 1, week3)
weekly_Min(securityloop, 3, week3)
weekly_Min(usherloop, 5, week3)
weekly_Min(nurseryloopAM, 4, week3)
weekly_Min(nurseryloopPM, 4, week3)
weekly_Min(nurseryloopCaptAM, 2, week3)
weekly_Min(nurseryloopCaptPM, 2, week3)
weekly_Min(patrolloop, 4, week3)

weekly_Min(soundloop, 2, week4)
weekly_Min(phamloop, 1, week4)
weekly_Min(securityloop, 3, week4)
weekly_Min(usherloop, 5, week4)
weekly_Min(nurseryloopAM, 4, week4)
weekly_Min(nurseryloopPM, 4, week4)
weekly_Min(nurseryloopCaptAM, 2, week4)
weekly_Min(nurseryloopCaptPM, 2, week4)
weekly_Min(patrolloop, 4, week4)

weekly_Min(soundloop, 2, week5)
weekly_Min(phamloop, 1, week5)
weekly_Min(securityloop, 3, week5)
weekly_Min(usherloop, 5, week5)
weekly_Min(nurseryloopAM, 4, week5)
weekly_Min(nurseryloopPM, 4, week5)
weekly_Min(nurseryloopCaptAM, 2, week5)
weekly_Min(nurseryloopCaptPM, 2, week5)
weekly_Min(patrolloop, 4, week5)

weekly_Min(soundloop, 2, week6)
weekly_Min(phamloop, 1, week6)
weekly_Min(securityloop, 3, week6)
weekly_Min(usherloop, 5, week6)
weekly_Min(nurseryloopAM, 4, week6)
weekly_Min(nurseryloopPM, 4, week6)
weekly_Min(nurseryloopCaptAM, 2, week6)
weekly_Min(nurseryloopCaptPM, 2, week6)
weekly_Min(patrolloop, 4, week6)

weekly_Min(soundloop, 2, week7)
weekly_Min(phamloop, 1, week7)
weekly_Min(securityloop, 3, week7)
weekly_Min(usherloop, 5, week7)
weekly_Min(nurseryloopAM, 4, week7)
weekly_Min(nurseryloopPM, 4, week7)
weekly_Min(nurseryloopCaptAM, 2, week7)
weekly_Min(nurseryloopCaptPM, 2, week7)
weekly_Min(patrolloop, 4, week7)

weekly_Min(soundloop, 2, week8)
weekly_Min(phamloop, 1, week8)
weekly_Min(securityloop, 3, week8)
weekly_Min(usherloop, 5, week8)
weekly_Min(nurseryloopAM, 4, week8)
weekly_Min(nurseryloopPM, 4, week8)
weekly_Min(nurseryloopCaptAM, 2, week8)
weekly_Min(nurseryloopCaptPM, 2, week8)
weekly_Min(patrolloop, 4, week8)

weekly_Min(soundloop, 2, week9)
weekly_Min(phamloop, 1, week9)
weekly_Min(securityloop, 3, week9)
weekly_Min(usherloop, 5, week9)
weekly_Min(nurseryloopAM, 4, week9)
weekly_Min(nurseryloopPM, 4, week9)
weekly_Min(nurseryloopCaptAM, 2, week9)
weekly_Min(nurseryloopCaptPM, 2, week9)
weekly_Min(patrolloop, 4, week9)

weekly_Min(soundloop, 2, week10)
weekly_Min(phamloop, 1, week10)
weekly_Min(securityloop, 3, week10)
weekly_Min(usherloop, 5, week10)
weekly_Min(nurseryloopAM, 4, week10)
weekly_Min(nurseryloopPM, 4, week10)
weekly_Min(nurseryloopCaptAM, 2, week10)
weekly_Min(nurseryloopCaptPM, 2, week10)
weekly_Min(patrolloop, 4, week10)

weekly_Min(soundloop, 2, week11)
weekly_Min(phamloop, 1, week11)
weekly_Min(securityloop, 3, week11)
weekly_Min(usherloop, 5, week11)
weekly_Min(nurseryloopAM, 4, week11)
weekly_Min(nurseryloopPM, 4, week11)
weekly_Min(nurseryloopCaptAM, 2, week11)
weekly_Min(nurseryloopCaptPM, 2, week11)
weekly_Min(patrolloop, 4, week11)

weekly_Min(soundloop, 2, week12)
weekly_Min(phamloop, 1, week12)
weekly_Min(securityloop, 3, week12)
weekly_Min(usherloop, 5, week12)
weekly_Min(nurseryloopAM, 4, week12)
weekly_Min(nurseryloopPM, 4, week12)
weekly_Min(nurseryloopCaptAM, 2, week12)
weekly_Min(nurseryloopCaptPM, 2, week12)
weekly_Min(patrolloop, 4, week12)

weekly_Min(soundloop, 2, week13)
weekly_Min(phamloop, 1, week13)
weekly_Min(securityloop, 3, week13)
weekly_Min(usherloop, 5, week13)
weekly_Min(nurseryloopAM, 4, week13)
weekly_Min(nurseryloopPM, 4, week13)
weekly_Min(nurseryloopCaptAM, 2, week13)
weekly_Min(nurseryloopCaptPM, 2, week13)
weekly_Min(patrolloop, 4, week13)

weekly_Min(soundloop, 2, week14)
weekly_Min(phamloop, 1, week14)
weekly_Min(securityloop, 3, week14)
weekly_Min(usherloop, 5, week14)
weekly_Min(nurseryloopAM, 4, week14)
weekly_Min(nurseryloopPM, 4, week14)
weekly_Min(nurseryloopCaptAM, 2, week14)
weekly_Min(nurseryloopCaptPM, 2, week14)
weekly_Min(patrolloop, 4, week14)

weekly_Min(soundloop, 2, week15)
weekly_Min(phamloop, 1, week15)
weekly_Min(securityloop, 3, week15)
weekly_Min(usherloop, 5, week15)
weekly_Min(nurseryloopAM, 4, week15)
weekly_Min(nurseryloopPM, 4, week15)
weekly_Min(nurseryloopCaptAM, 2, week15)
weekly_Min(nurseryloopCaptPM, 2, week15)
weekly_Min(patrolloop, 4, week15)

weekly_Min(soundloop, 2, week16)
weekly_Min(phamloop, 1, week16)
weekly_Min(securityloop, 3, week16)
weekly_Min(usherloop, 5, week16)
weekly_Min(nurseryloopAM, 4, week16)
weekly_Min(nurseryloopPM, 4, week16)
weekly_Min(nurseryloopCaptAM, 2, week16)
weekly_Min(nurseryloopCaptPM, 2, week16)
weekly_Min(patrolloop, 4, week16)

weekly_Min(soundloop, 2, week17)
weekly_Min(phamloop, 1, week17)
weekly_Min(securityloop, 3, week17)
weekly_Min(usherloop, 5, week17)
weekly_Min(nurseryloopAM, 4, week17)
weekly_Min(nurseryloopPM, 4, week17)
weekly_Min(nurseryloopCaptAM, 2, week17)
weekly_Min(nurseryloopCaptPM, 2, week17)
weekly_Min(patrolloop, 4, week17)

weekly_Min(soundloop, 2, week18)
weekly_Min(phamloop, 1, week18)
weekly_Min(securityloop, 3, week18)
weekly_Min(usherloop, 5, week18)
weekly_Min(nurseryloopAM, 4, week18)
weekly_Min(nurseryloopPM, 4, week18)
weekly_Min(nurseryloopCaptAM, 2, week18)
weekly_Min(nurseryloopCaptPM, 2, week18)
weekly_Min(patrolloop, 4, week18)

weekly_Min(soundloop, 2, week19)
weekly_Min(phamloop, 1, week19)
weekly_Min(securityloop, 3, week19)
weekly_Min(usherloop, 5, week19)
weekly_Min(nurseryloopAM, 4, week19)
weekly_Min(nurseryloopPM, 4, week19)
weekly_Min(nurseryloopCaptAM, 2, week19)
weekly_Min(nurseryloopCaptPM, 2, week19)
weekly_Min(patrolloop, 4, week19)

weekly_Min(soundloop, 2, week20)
weekly_Min(phamloop, 1, week20)
weekly_Min(securityloop, 3, week20)
weekly_Min(usherloop, 5, week20)
weekly_Min(nurseryloopAM, 4, week20)
weekly_Min(nurseryloopPM, 4, week20)
weekly_Min(nurseryloopCaptAM, 2, week20)
weekly_Min(nurseryloopCaptPM, 2, week20)
weekly_Min(patrolloop, 4, week20)

weekly_Min(soundloop, 2, week21)
weekly_Min(phamloop, 1, week21)
weekly_Min(securityloop, 3, week21)
weekly_Min(usherloop, 5, week21)
weekly_Min(nurseryloopAM, 4, week21)
weekly_Min(nurseryloopPM, 4, week21)
weekly_Min(nurseryloopCaptAM, 2, week21)
weekly_Min(nurseryloopCaptPM, 2, week21)
weekly_Min(patrolloop, 4, week21)

weekly_Min(soundloop, 2, week22)
weekly_Min(phamloop, 1, week22)
weekly_Min(securityloop, 3, week22)
weekly_Min(usherloop, 5, week22)
weekly_Min(nurseryloopAM, 4, week22)
weekly_Min(nurseryloopPM, 4, week22)
weekly_Min(nurseryloopCaptAM, 2, week22)
weekly_Min(nurseryloopCaptPM, 2, week22)
weekly_Min(patrolloop, 4, week22)

weekly_Min(soundloop, 2, week23)
weekly_Min(phamloop, 1, week23)
weekly_Min(securityloop, 3, week23)
weekly_Min(usherloop, 5, week23)
weekly_Min(nurseryloopAM, 4, week23)
weekly_Min(nurseryloopPM, 4, week23)
weekly_Min(nurseryloopCaptAM, 2, week23)
weekly_Min(nurseryloopCaptPM, 2, week23)
weekly_Min(patrolloop, 4, week23)

weekly_Min(soundloop, 2, week24)
weekly_Min(phamloop, 1, week24)
weekly_Min(securityloop, 3, week24)
weekly_Min(usherloop, 5, week24)
weekly_Min(nurseryloopAM, 4, week24)
weekly_Min(nurseryloopPM, 4, week24)
weekly_Min(nurseryloopCaptAM, 2, week24)
weekly_Min(nurseryloopCaptPM, 2, week24)
weekly_Min(patrolloop, 4, week24)

#--------------------------- OUTPUT to CSV file -------------------------------------------
with open(output_file,'a') as csvfile:
	csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
	csvfile.truncate(0)
	#open csv file and remove contents

#---------------------- Function Call to format csv output ---------------------------------
	def output_to_csv(weekNum, week_string):
		soundWeek = []
		phamWeek = []
		securityWeek = []
		usherWeek = []
		nurseryAMWeek = []
		nurseryPMWeek = []
		nurseryCaptAMWeek = []
		nurseryCaptPMWeek = []
		parkingWeekAM = []
		parkingWeekPM = []
		for i in range(len(weekNum)):
			if 0 <= i <= 1:
				soundWeek.append(weekNum[i])
			if i == 2:
				phamWeek.append(weekNum[i])
			if 3 <= i <= 5:
				securityWeek.append(weekNum[i])
			if 6 <= i <= 10:
				usherWeek.append(weekNum[i])
			if 11 <= i <= 14:
				nurseryAMWeek.append(weekNum[i])
			if 15 <= i <= 18:
				nurseryPMWeek.append(weekNum[i])
			if 19 <= i <= 20:
				nurseryCaptAMWeek.append(weekNum[i])
			if 21 <= i <= 22:
				nurseryCaptPMWeek.append(weekNum[i])
			if 23 <= i <= 24:
				parkingWeekAM.append(weekNum[i])
			if 25 <= i <= 26:
				parkingWeekPM.append(weekNum[i])
		soundList = '\n'.join(soundWeek)
		phamList = '\n'.join(phamWeek)
		securityList = '\n'.join(securityWeek)
		usherList = '\n'.join(usherWeek)
		nurseryAMList = '\n'.join(nurseryAMWeek)
		nurseryPMList = '\n'.join(nurseryPMWeek)
		nurseryCaptAMList = '\n'.join(nurseryCaptAMWeek)
		nurseryCaptPMList = '\n'.join(nurseryCaptPMWeek)
		parkingListAM = '\n'.join(parkingWeekAM)
		parkingListPM = '\n'.join(parkingWeekPM)

		row1 = [week_string]
		row2 = ["Sound", "Pham Driving", "Security", "Ushering", "Nursery AM", "Nursery Captains AM ", "Nursery PM", "Nursery Captains PM", "Parking Patrol AM", "Parking Patrol PM"]
		row3 = [soundList, phamList, securityList, usherList, nurseryAMList, nurseryCaptAMList, nurseryPMList, nurseryCaptPMList, parkingListAM, parkingListPM]
		csvwriter.writerow(row1)
		csvwriter.writerow(row2)
		csvwriter.writerow(row3)
		csvwriter.writerow("")
#---------------------------------------------------------------------------------------------
#------------------------------- Function Calls per week -------------------------------------

	output_to_csv(week1, "Week 1")
	output_to_csv(week2, "Week 2")
	output_to_csv(week3, "Week 3")
	output_to_csv(week4, "Week 4")
	output_to_csv(week5, "Week 5")
	output_to_csv(week6, "Week 6")
	output_to_csv(week7, "Week 7")
	output_to_csv(week8, "Week 8")
	output_to_csv(week9, "Week 9")
	output_to_csv(week10, "Week 10")
	output_to_csv(week11, "Week 11")
	output_to_csv(week12, "Week 12")
	output_to_csv(week13, "Week 13")
	output_to_csv(week14, "Week 14")
	output_to_csv(week15, "Week 15")
	output_to_csv(week16, "Week 16")
	output_to_csv(week17, "Week 17")
	output_to_csv(week18, "Week 18")
	output_to_csv(week19, "Week 19")
	output_to_csv(week20, "Week 20")
	output_to_csv(week21, "Week 21")
	output_to_csv(week22, "Week 22")
	output_to_csv(week23, "Week 23")
	output_to_csv(week24, "Week 24")

	
#--------------------------------------------------------------------------------------------
