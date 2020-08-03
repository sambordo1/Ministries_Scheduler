import pandas
  

ushering = []
nursery = []
security = []
parking_patrol = []
pham_driving= []
sunday_school = []
sound = []
choir = []
orchestra = []
special_music = []


excel_data_df = pandas.read_excel('Ministries.xlsx')
excel_data_df = excel_data_df.fillna('')


ushering = (excel_data_df['Ushering'].tolist())
nursery = (excel_data_df['Nursery'].tolist())


def create_schedule(usherList, nurseryList):
	for each in usherList:
		print(each)
	for each in nurseryList:
		print(each)



create_schedule(ushering, nursery)