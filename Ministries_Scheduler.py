import xlrd

sound = []
sound1 = []
sound2 = []
sound3 = []
sound4 = []

pham = []
pham1 = []
pham2 = []
pham3 = []
pham4 = []

security = []
security1 = []
security2 = []
security3 = []
security4 = []

ushers = []
ushers1 = []
ushers2 = []
ushers3 = []
ushers4 = []

nursery = []
nursery1 = []
nursery2 = []
nursery3 = []
nursery4 = []


in_file = ("Ministries.xlsx")

wb = xlrd.open_workbook(in_file)
sheet = wb.sheet_by_index(0)

data = [[sheet.cell_value(r, c) for r in range(sheet.nrows)] for c in range(sheet.ncols)]
for arrays in data:
	headings = arrays[0]
	if headings == "Ushering":
		ushers = arrays
		while ("" in ushers):
			ushers.remove("")
	if headings == "Nursery":
		nursery = arrays
		while ("" in nursery):
			nursery.remove("")
	if headings == "Security":
		security = arrays
		while ("" in security):
			security.remove("")
	if headings == "Parking Patrol":
		parking_patrol = arrays
		while ("" in parking_patrol):
			parking_patrol.remove("")
	if headings == "Pham Driving":
		pham = arrays
		while ("" in pham):
			pham.remove("")
	if headings == "Sunday School":
		sunday_school = arrays
	if headings == "Sound":
		sound = arrays
		while ("" in sound):
			sound.remove("")

#----------------------------Sound----------------------------------------------------
s = 1
while s < 3:
	sound1.append(sound[s])
	s += 1
while 3 <= s < 5:
	sound2.append(sound[s])
	s += 1
while 5 <= s < 7:
	sound3.append(sound[s])
	s += 1
while 7 <= s < 9:
	sound4.append(sound[s])
	s += 1


#----------------------------Pham Driving---------------------------------------------
p = 1
conflict = ""
while p == 1:
	if (pham[p]) not in sound1:
		pham1.append(pham[p])
		p += 1
	if (pham[p]) in sound1:
		conflict = pham[p]
		pham.remove(pham[p])
		pham.append(conflict)
while p == 2:
	if (pham[p]) not in sound2:
		pham2.append(pham[p])
		p += 1
	if (pham[p]) in sound2:
		conflict = pham[p]
		pham.remove(pham[p])
		pham.append(conflict)
while p == 3:
	if (pham[p]) not in sound3:
		pham3.append(pham[p])
		p += 1
	if (pham[p]) in sound3:
		conflict = pham[p]
		pham.remove(pham[p])
		pham.append(conflict)
while p == 4:
	if (pham[p]) not in sound4:
		pham4.append(pham[p])
		p += 1
	if (pham[p]) in sound4:
		conflict = pham[p]
		pham.remove(pham[p])
		pham.append(conflict)


#----------------------------Security-------------------------------------------------
s = 1
conflict = ""
while s < 4:
	if (security[s]) not in sound1:
		if (security[s]) not in pham1:
			security1.append(security[s])
			s += 1
	if (security[s]) in sound1:
		conflict = security[s]
		security.remove(security[s])
		security.append(conflict)
	if (security[s]) in pham1:
		conflict = security[s]
		security.remove(security[s])
		security.append(conflict)

while 4 <= s < 7:
	if (security[s]) not in sound2:
		if (security[s]) not in pham2:
			security2.append(security[s])
			s += 1
	if (security[s]) in sound2:
		conflict = security[s]
		security.remove(security[s])
		security.append(conflict)
	if (security[s]) in pham2:
		conflict = security[s]
		security.remove(security[s])
		security.append(conflict)
while 7 <= s < 10:
	if (security[s]) not in sound3:
		if (security[s]) not in pham3:
			security3.append(security[s])
			s += 1
	if (security[s]) in sound3:
		conflict = security[s]
		security.remove(security[s])
		security.append(conflict)
	if (security[s]) in pham3:
		conflict = security[s]
		security.remove(security[s])
		security.append(conflict)
while 10 <= s < 13:
	if (security[s]) not in sound4:
		if (security[s]) not in pham4:
			security4.append(security[s])
			s += 1
	if (security[s]) in sound4:
		conflict = security[s]
		security.remove(security[s])
		security.append(conflict)
	if (security[s]) in pham4:
		conflict = security[s]
		security.remove(security[s])
		security.append(conflict)


#----------------------------Ushers---------------------------------------------------
u = 1
while u < 6:
	if (ushers[u]) not in sound1:
		if (ushers[u]) not in pham1:
			if (ushers[u]) not in security1:
				ushers1.append(ushers[u])
				u += 1
	if (ushers[u]) in sound1:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
	if (ushers[u]) in pham1:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
	if (ushers[u]) in security1:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
while 6 <= u < 11:
	if (ushers[u]) not in sound2:
		if (ushers[u]) not in pham2:
			if (ushers[u]) not in security2:
				ushers2.append(ushers[u])
				u += 1
	if (ushers[u]) in sound2:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
	if (ushers[u]) in pham2:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
	if (ushers[u]) in security2:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
while 11 <= u < 16:
	if (ushers[u]) not in sound3:
		if (ushers[u]) not in pham3:
			if (ushers[u]) not in security3:
				ushers3.append(ushers[u])
				u += 1
	if (ushers[u]) in sound3:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
	if (ushers[u]) in pham3:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
	if (ushers[u]) in security3:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
while 16 <= u < 21:
	if (ushers[u]) not in sound4:
		if (ushers[u]) not in pham4:
			if (ushers[u]) not in security4:
				ushers4.append(ushers[u])
				u += 1
	if (ushers[u]) in sound4:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
	if (ushers[u]) in pham4:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)
	if (ushers[u]) in security4:
		conflict = ushers[u]
		ushers.remove(ushers[u])
		ushers.append(conflict)


#------------------------------Nursery--------------------------------------------------

n = 1
while n < 7:
	if (nursery[n]) not in sound1:
		if (nursery[n]) not in pham1:
			if (nursery[n]) not in security1:
				if (nursery[n]) not in ushers1:
					nursery1.append(nursery[n])
					n += 1
	if (nursery[n]) in sound1:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in pham1:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in security1:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in ushers1:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
while 7 <= n < 13:
	if (nursery[n]) not in sound2:
		if (nursery[n]) not in pham2:
			if (nursery[n]) not in security2:
				if (nursery[n]) not in ushers2:
					nursery2.append(nursery[n])
					n += 1
	if (nursery[n]) in sound2:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in pham2:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in security2:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in ushers2:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
while 13 <= n < 19:
	if (nursery[n]) not in sound3:
		if (nursery[n]) not in pham3:
			if (nursery[n]) not in security3:
				if (nursery[n]) not in ushers3:
					nursery3.append(nursery[n])
					n += 1
	if (nursery[n]) in sound3:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in pham3:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in security3:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in ushers3:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
while 19 <= n < 25:
	if (nursery[n]) not in sound4:
		if (nursery[n]) not in pham4:
			if (nursery[n]) not in security4:
				if (nursery[n]) not in ushers4:
					nursery4.append(nursery[n])
					n += 1
	if (nursery[n]) in sound4:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in pham4:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in security4:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)
	if (nursery[n]) in ushers4:
		conflict = nursery[n]
		nursery.remove(nursery[n])
		nursery.append(conflict)


#--------------------------------------------------------------------------------------

print("Week 1: ")
print("Sound: " + ', '.join(sound1))
print("Pham Driving: " + ', '.join(pham1))
print("Security: " + ', '.join(security1))
print("Ushers: " + ', '.join(ushers1))
print("Nursery: " + ', '.join(nursery1))
print('---------------------------------')
print("Week 2: ")
print("Sound: " + ', '.join(sound2))
print("Pham Driving: " + ', '.join(pham2))
print("Security: " + ', '.join(security2))
print("Ushers: " + ', '.join(ushers2))
print("Nursery: " + ', '.join(nursery2))
print('---------------------------------')
print("Week 3: ")
print("Sound: " + ', '.join(sound3))
print("Pham Driving: " + ', '.join(pham3))
print("Security: " + ', '.join(security3))
print("Ushers: " + ', '.join(ushers3))
print("Nursery: " + ', '.join(nursery3))
print('---------------------------------')
print("Week 4: ")
print("Sound: " + ', '.join(sound4))
print("Pham Driving: " + ', '.join(pham4))
print("Security: " + ', '.join(security4))
print("Ushers: " + ', '.join(ushers4))
print("Nursery: " + ', '.join(nursery4))



# print(sound)
# print(pham)
# print(security)
# print(ushers)
# print(nursery)



