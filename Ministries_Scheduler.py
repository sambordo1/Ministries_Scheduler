import xlrd


ushering = []
ushersWeekly = []

nursery = []
nurseryWeekly = []

security = []
securityWeekly = []

parking_patrol = []
parking_patrolWeekly =[]

# pham_driving= []
# sunday_school = []
# sound = []
# choir = []
# orchestra = []
# special_music = []


in_file = ("Ministries.xlsx")

wb = xlrd.open_workbook(in_file)
sheet = wb.sheet_by_index(0)

data = [[sheet.cell_value(r, c) for r in range(sheet.nrows)] for c in range(sheet.ncols)]
for arrays in data:
	headings = arrays[0]
	if headings == "Ushering":
		ushering = arrays
	if headings == "Nursery":
		nursery = arrays
	if headings == "Security":
		security = arrays
	if headings == "Parking Patrol":
		parking_patrol = arrays

	# if headings == "Pham Driving":
	# 	pham_driving = arrays
	# if headings == "Sunday School":
	# 	sunday_school = arrays
	# if headings == "Sound":
	# 	sound = arrays
	# if headings == "Choir":
	# 	choir = arrays
	# if headings == "Orchestra":
	# 	orchestra = arrays
	# if headings == "Special Music":
	# 	special_music = arrays

i = 1
while i < 6:
	ushersWeekly.append(ushering[i])
	i += 1

i = 1
while i < 6:
	nurseryWeekly.append(nursery[i])
	i += 1

i = 1
while i < 6:
	securityWeekly.append(security[i])
	i += 1

i = 1
while i < 6:
	parking_patrolWeekly.append(parking_patrol[i])
	i += 1

no_conflict = list(set(ushersWeekly) - set(nurseryWeekly))
print(no_conflict)

conflicts = list(set(ushersWeekly).intersection(set(nurseryWeekly)))
print(conflicts)




