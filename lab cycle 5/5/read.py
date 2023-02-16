import csv
dic=[{"BRAND:","Apple", "MODEL:","iPhone"}, {"BRAND:","Google", "MODEL:","pixel"},
 {"BRAND:","mi", "MODEL:","note 10 pro"}]
with open("file2.csv",mode='w') as file:
	fileDict=csv.DictWriter(file,fieldnames=["BRAND","MODEL"])
	fileDict.writeheader()
	fileDict.writerows(dic)
	file.close()
with open("file2.csv",mode='r') as file1:
	csvfile=csv.reader(file2)
	for x in csvfile:
		print(x)
file2.close()
