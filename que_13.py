# Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22John,54 Love Ave,21

import csv

def make_csv(file_name,csv_value):
    with open(file_name,'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['name','address','age'])
        writer.writerows(csv_value)

csv_values= [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

make_csv('que_13.csv',csv_values)