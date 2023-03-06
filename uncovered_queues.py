import csv

csv_file = open('cover.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

rows = []

line = 0
for row in csv_reader:
    line += 1
    if line > 1:
        if 'O' not in row:
            input(row)