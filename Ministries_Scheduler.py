import xlrd
from itertools import cycle, islice
import csv
import sys
import pandas as pd


#--------------------------- Getting Sunday Dates in specified year -----------------------------

def allsundays(year):
    return pd.date_range(start=str(year), end=str(year+1), 
                         freq='W-SUN').strftime('%m/%d/%Y').tolist()

#------------------------------------------------------------------------------------------------
year = 2020
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
week25=[]
week26=[]
week27=[]
week28=[]
week29=[]
week30=[]
week31=[]
week32=[]
week33=[]
week34=[]
week35=[]
week36=[]
week37=[]
week38=[]
week39=[]
week40=[]
week41=[]
week42=[]
week43=[]
week44=[]
week45=[]
week46=[]
week47=[]
week48=[]
week49=[]
week50=[]
week51=[]
week52=[]


output_file = "Ministries_Schedule.csv"
in_file = ("Ministries.xlsx")
numWeeks = 52

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

def call_weekly_Mins(weekNum):
	weekly_Min(soundloop, 2, weekNum)
	weekly_Min(phamloop, 1, weekNum)
	weekly_Min(securityloop, 3, weekNum)
	weekly_Min(usherloop, 5, weekNum)
	weekly_Min(nurseryloopAM, 4, weekNum)
	weekly_Min(nurseryloopPM, 4, weekNum)
	weekly_Min(nurseryloopCaptAM, 2, weekNum)
	weekly_Min(nurseryloopCaptPM, 2, weekNum)
	weekly_Min(patrolloop, 4, weekNum)



call_weekly_Mins(week1)
call_weekly_Mins(week2)
call_weekly_Mins(week3)
call_weekly_Mins(week4)
call_weekly_Mins(week5)
call_weekly_Mins(week6)
call_weekly_Mins(week7)
call_weekly_Mins(week8)
call_weekly_Mins(week9)
call_weekly_Mins(week10)
call_weekly_Mins(week11)
call_weekly_Mins(week12)
call_weekly_Mins(week13)
call_weekly_Mins(week14)
call_weekly_Mins(week15)
call_weekly_Mins(week16)
call_weekly_Mins(week17)
call_weekly_Mins(week18)
call_weekly_Mins(week19)
call_weekly_Mins(week20)
call_weekly_Mins(week21)
call_weekly_Mins(week22)
call_weekly_Mins(week23)
call_weekly_Mins(week24)
call_weekly_Mins(week25)
call_weekly_Mins(week26)
call_weekly_Mins(week27)
call_weekly_Mins(week28)
call_weekly_Mins(week29)
call_weekly_Mins(week30)
call_weekly_Mins(week31)
call_weekly_Mins(week32)
call_weekly_Mins(week33)
call_weekly_Mins(week34)
call_weekly_Mins(week35)
call_weekly_Mins(week36)
call_weekly_Mins(week37)
call_weekly_Mins(week38)
call_weekly_Mins(week39)
call_weekly_Mins(week40)
call_weekly_Mins(week41)
call_weekly_Mins(week42)
call_weekly_Mins(week43)
call_weekly_Mins(week44)
call_weekly_Mins(week45)
call_weekly_Mins(week46)
call_weekly_Mins(week47)
call_weekly_Mins(week48)
call_weekly_Mins(week49)
call_weekly_Mins(week50)
call_weekly_Mins(week51)
call_weekly_Mins(week52)

#--------------------------- OUTPUT to CSV file -------------------------------------------
with open(output_file,'a') as csvfile:
	csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
	csvfile.truncate(0)
	#open csv file and remove contents

#---------------------- Function Call to format csv output ---------------------------------
	def output_to_csv(weekNum, sunday_date_num):
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
		week_string = []
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

		
		week_string = allsundays(year)[sunday_date_num - 1]
		row1 = [week_string]
		row2 = ["Sound", "Pham Driving", "Security", "Ushering", "Nursery AM", "Nursery Captains AM ", "Nursery PM", "Nursery Captains PM", "Parking Patrol AM", "Parking Patrol PM"]
		row3 = [soundList, phamList, securityList, usherList, nurseryAMList, nurseryCaptAMList, nurseryPMList, nurseryCaptPMList, parkingListAM, parkingListPM]
		csvwriter.writerow(row1)
		csvwriter.writerow(row2)
		csvwriter.writerow(row3)
		csvwriter.writerow("")
#---------------------------------------------------------------------------------------------
#------------------------------- Function Calls per week -------------------------------------

	print("Schedule is for " + str(len(allsundays(2020))) + " weeks" + " for the year " + str(year))

	output_to_csv(week1, 1)
	output_to_csv(week2, 2)
	output_to_csv(week3, 3)
	output_to_csv(week4, 4)
	output_to_csv(week5, 5)
	output_to_csv(week6, 6)
	output_to_csv(week7, 7)
	output_to_csv(week8, 8)
	output_to_csv(week9, 9)
	output_to_csv(week10, 10)
	output_to_csv(week11, 11)
	output_to_csv(week12, 12)
	output_to_csv(week13, 13)
	output_to_csv(week14, 14)
	output_to_csv(week15, 15)
	output_to_csv(week16, 16)
	output_to_csv(week17, 17)
	output_to_csv(week18, 18)
	output_to_csv(week19, 19)
	output_to_csv(week20, 20)
	output_to_csv(week21, 21)
	output_to_csv(week22, 22)
	output_to_csv(week23, 23)
	output_to_csv(week24, 24)
	output_to_csv(week25, 25)
	output_to_csv(week26, 26)
	output_to_csv(week27, 27)
	output_to_csv(week28, 28)
	output_to_csv(week29, 29)
	output_to_csv(week30, 30)
	output_to_csv(week31, 31)
	output_to_csv(week32, 32)
	output_to_csv(week33, 33)
	output_to_csv(week34, 34)
	output_to_csv(week35, 35)
	output_to_csv(week36, 36)
	output_to_csv(week37, 37)
	output_to_csv(week38, 38)
	output_to_csv(week39, 39)
	output_to_csv(week40, 40)
	output_to_csv(week41, 41)
	output_to_csv(week42, 42)
	output_to_csv(week43, 43)
	output_to_csv(week44, 44)
	output_to_csv(week45, 45)
	output_to_csv(week46, 46)
	output_to_csv(week47, 47)
	output_to_csv(week48, 48)
	output_to_csv(week49, 49)
	output_to_csv(week50, 50)
	output_to_csv(week51, 51)
	output_to_csv(week52, 52)

#--------------------------------------------------------------------------------------------