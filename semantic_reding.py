from csv import DictWriter

with open('./users.csv', 'w') as file:

    csv_writer = DictWriter(file, filenames=header)

    header = ('statefileID','Election_State',	'General_Election_2020',	'General_Election_2020_Date',
    	'General_Election_2020_Method',	'Democratic_Primary_2020',	'Democratic_Primary_2020_Date',	'Democratic_Primary_2020_Method',	'Election_Party')
    data = (
        ('OH0011081468','OH',	'Y',	'11/04/2020',	'voted',	'Y',	'05/05/2020',	'voted',	'Independent'),
        ('OH0011133376','OH', ' ',	 ' ', ' ',  'Y',	'05/05/2020',	'voted',	   'Democrat'),
        ('OH0012547963','OH',	'Y',	'11/04/2020',	'voted',' ', '',' ',    'Democrat'),
        ('OH0018244625','OH',	'Y',	'11/04/2020',	'absentee','Y',	'05/05/2020',	'absentee',	'Democrat'),
        ('OH0012349329','OH',	'Y',	'11/04/2020',	'early', 	 'Y',	'05/05/2020',	'early',	    'Democrat')
    )

    csv_writer.writerow ({
     'statefileID':'OH0011081468',
     'Election_State':	'OH',
     'General_Election_2020' :'Y',	
     'General_Election_2020_Date' : '11/04/2020',
     'General_Election_2020_Method' :	'voted',
     'Democratic_Primary_2020' : 'Y',	
     'Democratic_Primary_2020_Date' : '05/05/2020',
    'Democratic_Primary_2020_Method':  'voted' ,	
     'Election_Party' : 'Independent'
 


 })