import csv
with open("file1.csv",mode="r") as file:
	csv_file=csv.reader(file)
	for x in csv_file:
		print(x)