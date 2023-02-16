import csv
with open("file1.csv",mode='r') as file:
	fileDict=csv.DictReader(file)
	for x in fileDict:
		print(x['ID'], x['BRAND'])