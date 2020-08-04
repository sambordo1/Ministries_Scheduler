import xlrd


ushering = []
ushersWeekly = []

nursery = []
nurseryWeekly = []

security = []
securityWeekly = []

parking_patrol = []
parking_patrolWeekly =[]

pham_driving= []
pham_drivingWeekly = []

sunday_school = []
sunday_schoolWeekly = []

sound = []
soundWeekly = []

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
	if headings == "Pham Driving":
		pham_driving = arrays
	if headings == "Sunday School":
		sunday_school = arrays
	if headings == "Sound":
		sound = arrays

	# if headings == "Choir":
	# 	choir = arrays
	# if headings == "Orchestra":
	# 	orchestra = arrays
	# if headings == "Special Music":
	# 	special_music = arrays

#----------------------------Ushering------------------------------------
u = 1
while u < 6:
	ushersWeekly.append(ushering[u])
	u += 1
#-------------------------------------------------------------------------

#----------------------------Nursery--------------------------------------
n =1
max = 6	
while n < max:
	if (nursery[n]) not in ushersWeekly:
		nurseryWeekly.append(nursery[n])
		n += 1
	if (nursery[n]) in ushersWeekly:
		n+=1
		max += 1
#-------------------------------------------------------------------------

#----------------------------Security-------------------------------------
s =1
max = 6	
while s < max:
	if (security[s]) not in ushersWeekly:
		if (security[s]) not in nurseryWeekly:
			securityWeekly.append(security[s])
			s += 1
	if (security[s]) in ushersWeekly:
		s+=1
		max += 1
	if (nursery[s]) in nurseryWeekly:
		s+=1
		max += 1
#--------------------------------------------------------------------------

#--------------------------Parking Patrol----------------------------------
p =1
max = 6	
while p < max:
	if (parking_patrol[p]) not in ushersWeekly:
		if (parking_patrol[p]) not in nurseryWeekly:
			if (parking_patrol[p]) not in securityWeekly:
				parking_patrolWeekly.append(parking_patrol[p])
				p += 1
	if (parking_patrol[p]) in ushersWeekly:
		p+=1
		max += 1
	if (parking_patrol[p]) in nurseryWeekly:
		p+=1
		max += 1
	if (parking_patrol[p]) in securityWeekly:
		p+=1
		max += 1
#---------------------------------------------------------------------------

#--------------------------Pham Driving-------------------------------------
d =1
max = 6	
while d < max:
	if (pham_driving[d]) not in ushersWeekly:
		if (pham_driving[d]) not in nurseryWeekly:
			if (pham_driving[d]) not in securityWeekly:
				if(pham_driving[d]) not in parking_patrolWeekly:
					pham_drivingWeekly.append(pham_driving[d])
					d += 1
	if (pham_driving[d]) in ushersWeekly:
		d+=1
		max += 1
	if (pham_driving[d]) in nurseryWeekly:
		d+=1
		max += 1
	if (pham_driving[d]) in securityWeekly:
		d+=1
		max += 1
	if (pham_driving[d]) in parking_patrolWeekly:
		d+=1
		max += 1
#-----------------------------------------------------------------------------

#------------------------Sunday School----------------------------------------
s =1
max = 6	
while s < max:
	if (sunday_school[s]) not in ushersWeekly:
		if (sunday_school[s]) not in nurseryWeekly:
			if (sunday_school[s]) not in securityWeekly:
				if(sunday_school[s]) not in parking_patrolWeekly:
					if(sunday_school[s]) not in pham_drivingWeekly:
						sunday_schoolWeekly.append(sunday_school[s])
						s += 1
	if (sunday_school[s]) in ushersWeekly:
		s+=1
		max += 1
	if (sunday_school[s]) in nurseryWeekly:
		s+=1
		max += 1
	if (sunday_school[s]) in securityWeekly:
		s+=1
		max += 1
	if (sunday_school[s]) in parking_patrolWeekly:
		s+=1
		max += 1
	if (sunday_school[s]) in pham_drivingWeekly:
		s+=1
		max += 1
#------------------------------------------------------------------------------

#-------------------------- Sound ---------------------------------------------
s =1
max = 6	
while s < max:
	if (sound[s]) not in ushersWeekly:
		if (sound[s]) not in nurseryWeekly:
			if (sound[s]) not in securityWeekly:
				if(sound[s]) not in parking_patrolWeekly:
					if(sound[s]) not in pham_drivingWeekly:
						if(sound[s]) not in sunday_schoolWeekly:
							soundWeekly.append(sound[s])
							s += 1
	if (sound[s]) in ushersWeekly:
		s+=1
		max += 1
	if (sound[s]) in nurseryWeekly:
		s+=1
		max += 1
	if (sound[s]) in securityWeekly:
		s+=1
		max += 1
	if (sound[s]) in parking_patrolWeekly:
		s+=1
		max += 1
	if (sound[s]) in pham_drivingWeekly:
		s+=1
		max += 1
	if (sound[s]) in sunday_schoolWeekly:
		s+=1
		max += 1
#--------------------------------------------------------------------------------

#--------------------------- Weekly ministries printed----------------------------	
print(ushersWeekly)
print(nurseryWeekly)
print(securityWeekly)
print(parking_patrolWeekly)
print(pham_drivingWeekly)
print(sunday_schoolWeekly)
print(soundWeekly)
#---------------------------------------------------------------------------------







