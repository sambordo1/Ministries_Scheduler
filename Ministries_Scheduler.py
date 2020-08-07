import xlrd
from itertools import cycle, islice

#-------------------------------Variables and Arrays----------------------------------------------
numWeeks = 24

sound1 = []
pham1 = []
security1 = []
usher1 = []
nursery1 = []
parking1 = []

sound2 = []
pham2 = []
security2 = []
usher2 = []
nursery2 = []
parking2 = []

sound3 = []
pham3 = []
security3 = []
usher3 = []
nursery3 = []
parking3 = []

sound4 = []
pham4 = []
security4 = []
usher4 = []
nursery4 = []
parking4 = []

sound5 = []
pham5 = []
security5 = []
usher5 = []
nursery5 = []
parking5 = []

#------------------------------------------------------------------------------------------------

#--------------------------------Reading in ministry arrays -------------------------------------
in_file = ("Ministries.xlsx")

wb = xlrd.open_workbook(in_file)
sheet = wb.sheet_by_index(0)

data = [[sheet.cell_value(r, c) for r in range(sheet.nrows)] for c in range(sheet.ncols)]
for arrays in data:
	headings = arrays[0]
#------------------------------------------------
	if headings == "Ushering":
		ushers = arrays
		del ushers[0]
		while ("" in ushers):
			ushers.remove("")
#-------------------------------------------------
	if headings == "Nursery":
		nursery = arrays
		del nursery[0]
		while ("" in nursery):
			nursery.remove("")
#-------------------------------------------------
	if headings == "Security":
		security = arrays
		del security[0]
		while ("" in security):
			security.remove("")
#--------------------------------------------------
	if headings == "Parking Patrol":
		parking_patrol = arrays
		del parking_patrol[0]
		while ("" in parking_patrol):
			parking_patrol.remove("")
#--------------------------------------------------
	if headings == "Pham Driving":
		pham = arrays
		del pham[0]
		while ("" in pham):
			pham.remove("")
#---------------------------------------------------
	if headings == "Sunday School":
		sunday_school = arrays
		del sunday_school[0]
		while ("" in sunday_school):
			sunday_school.remove("")
#------------------------------------------------------
	if headings == "Sound":
		sound = arrays
		del sound[0]
		while ("" in sound):
			sound.remove("")
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

x = 5 * numWeeks # (5 per week * number of weeks)
i = -1
nurseryloop = list( islice( cycle(nursery), i+1, i+1+x))

#------------------------------------------------------------------------------------------------
#----------------------------------------Parking Patrol------------------------------------------

x = 5 * numWeeks # (5 per week * number of weeks)
i = -1
patrolloop = list( islice( cycle(parking_patrol), i+1, i+1+x))

#------------------------------------------------------------------------------------------------

#------------------------------Function Call-----------------------------------------------------


def fill_Ministries(week, array, arrayloop, numNeeded):
	i = 0
	if(week == 1):
		for p in range(len(arrayloop)):
			while(i <= (numNeeded - 1)):
				if arrayloop[p] not in sound1:
					if arrayloop[p] not in pham1:
						if arrayloop[p] not in security1:
							if arrayloop[p] not in usher1:
								if arrayloop[p] not in nursery1:
									if arrayloop[p] not in parking1:
										array.append(arrayloop[p])
										arrayloop.pop(p)
										i += 1
									else:
										break
								else:	
									break
							else:
								break
						else:
							break
					else:
						break
				else:
					break
	if (week == 2):
		for p in range(len(arrayloop)):
			while(i <= (numNeeded - 1)):
				if arrayloop[p] not in sound2:
					if arrayloop[p] not in pham2:
						if arrayloop[p] not in security2:
							if arrayloop[p] not in usher2:
								if arrayloop[p] not in nursery2:
									if arrayloop[p] not in parking2:
										array.append(arrayloop[p])
										arrayloop.pop(p)
										i += 1
									else:
										break
								else:
									break		
							else:
								break
						else:
							break
					else:
						break
				else:
					break
	if (week == 3):
		for p in range(len(arrayloop)):
			while(i <= (numNeeded - 1)):
				if arrayloop[p] not in sound3:
					if arrayloop[p] not in pham3:
						if arrayloop[p] not in security3:
							if arrayloop[p] not in usher3:
								if arrayloop[p] not in nursery3:
									if arrayloop[p] not in parking3:
										array.append(arrayloop[p])
										arrayloop.pop(p)
										i += 1
									else:
										break
								else:
									break
							else:
								break
						else:
							break
					else:
						break
				else:
					break
	if (week == 4):
		for p in range(len(arrayloop)):
			while(i <= (numNeeded - 1)):
				if arrayloop[p] not in sound4:
					if arrayloop[p] not in pham4:
						if arrayloop[p] not in security4:
							if arrayloop[p] not in usher4:
								if arrayloop[p] not in nursery4:
									if arrayloop[p] not in parking4:
										array.append(arrayloop[p])
										arrayloop.pop(p)
										i += 1
									else:
										break
								else:
									break
							else:
								break
						else:
							break
					else:
						break
				else:
					break
	if (week == 5):
		for p in range(len(arrayloop)):
			while(i <= (numNeeded - 1)):
				if arrayloop[p] not in sound5:
					if arrayloop[p] not in pham5:
						if arrayloop[p] not in security5:
							if arrayloop[p] not in usher5:
								if arrayloop[p] not in nursery5:
									if arrayloop[p] not in parking5:
										array.append(arrayloop[p])
										arrayloop.pop(p)
										i += 1
									else:
										break
								else:
									break
							else:
								break
						else:
							break
					else:
						break
				else:
					break
# -----------------------------------------------------------------------------------------------
fill_Ministries(1, sound1, soundloop, 2)
fill_Ministries(1, pham1, phamloop, 1)
fill_Ministries(1, security1, securityloop, 3)
fill_Ministries(1, usher1, usherloop, 5)
fill_Ministries(1, nursery1, nurseryloop, 6)
fill_Ministries(1, parking1, patrolloop, 5)

fill_Ministries(2, sound2, soundloop, 2)
fill_Ministries(2, pham2, phamloop, 1)
fill_Ministries(2, security2, securityloop, 3)
fill_Ministries(2, usher2, usherloop, 5)
fill_Ministries(2, nursery2, nurseryloop, 6)
fill_Ministries(2, parking2, patrolloop, 5)

fill_Ministries(3, sound3, soundloop, 2)
fill_Ministries(3, pham3, phamloop, 1)
fill_Ministries(3, security3, securityloop, 3)
fill_Ministries(3, usher3, usherloop, 5)
fill_Ministries(3, nursery3, nurseryloop, 6)
fill_Ministries(3, parking3, patrolloop, 5)

fill_Ministries(4, sound4, soundloop, 2)
fill_Ministries(4, pham4, phamloop, 1)
fill_Ministries(4, security4, securityloop, 3)
fill_Ministries(4, usher4, usherloop, 5)
fill_Ministries(4, nursery4, nurseryloop, 6)
fill_Ministries(4, parking4, patrolloop, 5)

fill_Ministries(5, sound5, soundloop, 2)
fill_Ministries(5, pham5, phamloop, 1)
fill_Ministries(5, security5, securityloop, 3)
fill_Ministries(5, usher5, usherloop, 5)
fill_Ministries(5, nursery5, nurseryloop, 6)
fill_Ministries(5, parking5, patrolloop, 5)

print("------Week 1--------------------")
print(sound1)
print(pham1)
print(security1)
print(usher1)
print(nursery1)
print(parking1)
print("-----Week 2---------------------")
print(sound2)
print(pham2)
print(security2)
print(usher2)
print(nursery2)
print(parking2)
print("----Week 3-----------------------")
print(sound3)
print(pham3)
print(security3)
print(usher3)
print(nursery3)
print(parking3)
print("----Week 4-----------------------")
print(sound4)
print(pham4)
print(security4)
print(usher4)
print(nursery4)
print(parking4)
print("----Week 5-----------------------")
print(sound5)
print(pham5)
print(security5)
print(usher5)
print(nursery5)
print(parking5)


