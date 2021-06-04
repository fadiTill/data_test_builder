from pprint import pprint

with open('./users.csv') as file:

   csv_reader = DictReader(file) 
   data = list(csv_reader)
   for row in data:
       pprint(row)
   for row in data:
       pprint(row)