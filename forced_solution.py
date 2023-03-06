import csv

csv_file = open('cover.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

rows = []

forced = 0

line = 0
for row in csv_reader:
    if line == 0:
        paths = row
    line += 1
    if line > 1:
        if row.count('O') == 1 and row[2] == 'O': # if the solution we're concerned with is at index 2
            print(row[0]) # the queue
            forced += 1

print(forced)