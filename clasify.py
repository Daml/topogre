import csv
import sys

classes = {}

with open('mobilier_classes.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        classes[row.pop(0)] = row


with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        key = row[2][0:6]
        if key in classes:
            row.extend(classes[key])
        else:
            sys.stderr.write("Unknow class %s\n" % key)
            row.extend(['NULL', 'NULL'])
        print ','.join(row)
