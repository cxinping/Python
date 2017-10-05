# -*- coding: utf-8 -*-
 
import csv

with open('test.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile,dialect='excel')
    
    spamwriter.writerow(['a', '1', '1', '2', '2'])
    spamwriter.writerow(['b', '3', '3', '6', '4'])
    spamwriter.writerow(['c', '7', '7', '10', '4'])
    spamwriter.writerow(['d', '11','11','11', '1'])
    spamwriter.writerow(['e', '12','12','14', '3'])
    
with open('test.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print( row)
    