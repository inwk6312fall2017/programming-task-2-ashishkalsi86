import csv
def crime_count():
 with open(file, 'r') as myfile:
 crime_csv = csv.reader(myfile , delimiter = ',')
 crime_types = []
 crime_id = []
 crime_count = []

 for row in crime_csv:
   crime_types = row[8]
   crime_id = row[2]
   crime_count = row[7]
   crime_types.append(crime_type)
   crime_id.append(crime_id)
   crime_count.append(crime_count)
  print("crime_type" , \t , "crime_id" , \t , "crime_count")
  print("*********" , \t , "********" , \t , "********")
  

crime_count()
