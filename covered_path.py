import csv

csv_file = open('cover.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

rows = []

line = 0
for row in csv_reader:
    if line == 0:
        paths = row
    line += 1
    if line > 1:
        if row[0] == 'TISJLZO':
            for i in range(1, len(row)):
                if row[i] == 'O':
                    print(paths[i])