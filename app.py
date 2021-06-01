from csv import writer 
#reader

with open('./users.csv', 'w') as file:
    csv_writer = writer(file, delimiter='\t', lineterminator='\n')
    header = ('statefileID','Election_State',	'General_Election_2020',	'General_Election_2020_Date',	'General_Election_2020_Method',	'Democratic_Primary_2020',	'Democratic_Primary_2020_Date',	'Democratic_Primary_2020_Method',	'Election_Party')
    data = (
        ('OH0011081468','OH',	'Y',	'11/04/2020',	'voted',	'Y',	'05/05/2020',	'voted',	'Independent'),
        ('OH0011133376','OH', ' ',	 ' ', ' ',  'Y',	'05/05/2020',	'voted',	   'Democrat'),
        ('OH0012547963','OH',	'Y',	'11/04/2020',	'voted',' ', '',' ',    'Democrat'),
        ('OH0018244625','OH',	'Y',	'11/04/2020',	'absentee','Y',	'05/05/2020',	'absentee',	'Democrat'),
        ('OH0012349329','OH',	'Y',	'11/04/2020',	'early', 	 'Y',	'05/05/2020',	'early',	    'Democrat')
    )
    csv_writer.writerow(header)
    for row in data:
       csv_writer.writerow(row)
       csv_writer.writerows(data)

with open('./users.csv') as file:
    csv_reader = reader(file, delimiter='\t')
    for row in csv_reader:
        print(row)


#with open('./users.csv') as file:
    #csv_reader = reader(file, delimiter='\t')
    #for row in csv_reader:
        #print(row)
   