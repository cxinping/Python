# -*- coding: utf-8 -*-
 
import csv

with open('input_data.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile,dialect='excel')
    
    spamwriter.writerow(['rid','square_feet', 'price'])
    spamwriter.writerow(['1', '150', '6450' ])
    spamwriter.writerow(['2', '200', '7450'])
    spamwriter.writerow(['3', '250', '8450' ])
    spamwriter.writerow(['4', '300', '9450'])
    spamwriter.writerow(['5', '350', '11450'])
    spamwriter.writerow(['6', '400', '15450' ])
    spamwriter.writerow(['7', '600', '18450'])

with open('test.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print( row)
    